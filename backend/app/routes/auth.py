from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from app.models.user import User, UserCreate, UserLogin, Token, UserResponse
from app.config.database import get_database
from app.utils.auth import verify_password, get_password_hash, create_access_token, verify_token
from app.config.settings import settings
import logging

logger = logging.getLogger(__name__)
router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db=Depends(get_database)):
    """User login endpoint"""
    try:
        # Find user by username or email
        user_doc = await db.users.find_one({
            "$or": [
                {"username": form_data.username},
                {"email": form_data.username}
            ]
        })
        
        if not user_doc:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password"
            )
        
        user = User(**user_doc)
        
        # Verify password
        if not verify_password(form_data.password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password"
            )
        
        # Check if user is active
        if not user.isActive:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Inactive user"
            )
        
        # Create access token
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username, "user_id": str(user.id), "role": user.role},
            expires_delta=access_token_expires
        )
        
        # Update last login
        await db.users.update_one(
            {"_id": user.id},
            {"$set": {"lastLogin": datetime.utcnow()}}
        )
        
        # Prepare user response
        user_response = UserResponse(
            id=str(user.id),
            username=user.username,
            email=user.email,
            role=user.role,
            profile=user.profile,
            isActive=user.isActive,
            lastLogin=user.lastLogin,
            createdAt=user.createdAt
        )
        
        return Token(
            access_token=access_token,
            expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
            user=user_response
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Login error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )

@router.post("/register", response_model=UserResponse)
async def register(user_data: UserCreate, db=Depends(get_database)):
    """User registration endpoint (Admin only in production)"""
    try:
        # Check if username or email already exists
        existing_user = await db.users.find_one({
            "$or": [
                {"username": user_data.username},
                {"email": user_data.email}
            ]
        })
        
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username or email already registered"
            )
        
        # Hash password
        password_hash = get_password_hash(user_data.password)
        
        # Create user document
        user = User(
            username=user_data.username,
            email=user_data.email,
            password_hash=password_hash,
            role=user_data.role,
            profile=user_data.profile
        )
        
        # Insert user
        result = await db.users.insert_one(user.dict(by_alias=True, exclude={"id"}))
        
        # Get created user
        created_user = await db.users.find_one({"_id": result.inserted_id})
        
        return UserResponse(
            id=str(created_user["_id"]),
            username=created_user["username"],
            email=created_user["email"],
            role=created_user["role"],
            profile=created_user["profile"],
            isActive=created_user["isActive"],
            lastLogin=created_user.get("lastLogin"),
            createdAt=created_user["createdAt"]
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Registration error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )

@router.get("/me", response_model=UserResponse)
async def get_current_user(token: str = Depends(oauth2_scheme), db=Depends(get_database)):
    """Get current user information"""
    try:
        # Verify token
        payload = verify_token(token)
        username = payload.get("sub")
        
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials"
            )
        
        # Get user from database
        user_doc = await db.users.find_one({"username": username})
        
        if user_doc is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials"
            )
        
        return UserResponse(
            id=str(user_doc["_id"]),
            username=user_doc["username"],
            email=user_doc["email"],
            role=user_doc["role"],
            profile=user_doc["profile"],
            isActive=user_doc["isActive"],
            lastLogin=user_doc.get("lastLogin"),
            createdAt=user_doc["createdAt"]
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Get current user error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )

@router.post("/logout")
async def logout():
    """User logout endpoint"""
    # In a stateless JWT system, logout is handled client-side
    # You could implement token blacklisting here if needed
    return {"message": "Successfully logged out"}
