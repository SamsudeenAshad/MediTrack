from motor.motor_asyncio import AsyncIOMotorClient
from app.config.settings import settings
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class Database:
    client: AsyncIOMotorClient = None
    database = None

db = Database()

# Get current time as string for demo data
now = datetime.utcnow().isoformat()

# Demo users for testing
demo_users = [
    {
        "_id": "1",
        "username": "admin",
        "email": "admin@meditrack.com",
        "password_hash": "$2b$12$QgEzpNpFI3foQCpXrEpaZuwWFjfOQY.uPmzBHaFrBhcgcyscu3zmO",  # admin123
        "role": "admin",
        "profile": {
            "firstName": "Admin",
            "lastName": "User",
            "title": "System Administrator"
        },
        "isActive": True,
        "lastLogin": None,
        "createdAt": now
    },
    {
        "_id": "2",
        "username": "doctor",
        "email": "doctor@meditrack.com",
        "password_hash": "$2b$12$kIvRvrTonbEt4nPOyAezG.t2E/HQbj.2LYk0VHbsHA65P8M1wQeMi",  # doctor123
        "role": "doctor",
        "profile": {
            "firstName": "Dr. John",
            "lastName": "Smith",
            "title": "Cardiologist",
            "specialization": "Cardiology",
            "licenseNumber": "MD123456"
        },
        "isActive": True,
        "lastLogin": None,
        "createdAt": now
    },
    {
        "_id": "3",
        "username": "nurse",
        "email": "nurse@meditrack.com",
        "password_hash": "$2b$12$He.SGA6aikcEhSEFMGahzeIt2tZ7/aIm9NkNoN.Hhgs.TwIsPeIzy",  # nurse123
        "role": "nurse",
        "profile": {
            "firstName": "Jane",
            "lastName": "Doe",
            "title": "Registered Nurse",
            "department": "Emergency",
            "licenseNumber": "RN789012"
        },
        "isActive": True,
        "lastLogin": None,
        "createdAt": now
    }
]

# Simple in-memory database for demo (fallback when MongoDB is not available)
mock_database = {
    "users": demo_users.copy(),  # Initialize with demo users
    "patients": [],
    "vitals": [],
    "appointments": [],
    "prescriptions": [],
    "reports": []
}

async def connect_to_mongo():
    """Create database connection"""
    try:
        db.client = AsyncIOMotorClient(settings.DATABASE_URL)
        db.database = db.client.get_database("meditrack")
        
        # Test the connection
        await db.client.admin.command('ping')
        logger.info("Successfully connected to MongoDB")
        
    except Exception as e:
        logger.warning(f"Failed to connect to MongoDB: {e}")
        logger.info("Using mock database for demo purposes")
        db.database = None

async def close_mongo_connection():
    """Close database connection"""
    if db.client:
        db.client.close()
        logger.info("Disconnected from MongoDB")

async def get_database():
    """Get database instance"""
    if db.database:
        return db.database
    else:
        # Return mock database interface
        return MockDatabase()

class MockDatabase:
    """Mock database for demo purposes"""
    
    def __init__(self):
        self.data = mock_database
    
    def __getattr__(self, name):
        # Return a mock collection
        return MockCollection(name, self.data.get(name, []))

class MockCollection:
    """Mock MongoDB collection for demo purposes"""
    
    def __init__(self, name, data):
        self.name = name
        self.data = data
        self._id_counter = len(data) + 1
    
    async def find_one(self, query):
        """Find one document"""
        if "_id" in query:
            doc_id = str(query["_id"])
            for doc in self.data:
                if str(doc.get("_id")) == doc_id:
                    return doc
        elif "$or" in query:
            # Handle $or queries (for login)
            for doc in self.data:
                for condition in query["$or"]:
                    if all(doc.get(key) == value for key, value in condition.items()):
                        return doc
        else:
            # Handle simple field queries
            for doc in self.data:
                if all(doc.get(key) == value for key, value in query.items()):
                    return doc
        return None
    
    def find(self, query=None):
        """Find documents"""
        return MockCursor(self.data, query)
    
    async def insert_one(self, document):
        """Insert one document"""
        document["_id"] = str(self._id_counter)
        self._id_counter += 1
        self.data.append(document)
        return MockInsertResult(document["_id"])
    
    async def update_one(self, filter_query, update_query):
        """Update one document"""
        # Simple implementation
        return MockUpdateResult()

class MockCursor:
    """Mock MongoDB cursor"""
    
    def __init__(self, data, query=None):
        self.data = data
        self.query = query or {}
    
    def skip(self, n):
        return self
    
    def limit(self, n):
        return self
    
    async def to_list(self, length=None):
        """Convert cursor to list"""
        return self.data[:length] if length else self.data

class MockInsertResult:
    """Mock insert result"""
    
    def __init__(self, inserted_id):
        self.inserted_id = inserted_id

class MockUpdateResult:
    """Mock update result"""
    
    def __init__(self):
        self.modified_count = 1
