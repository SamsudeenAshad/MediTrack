from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from app.models.patient import Patient, PatientCreate, PatientUpdate, PatientResponse
from app.config.database import get_database
from app.utils.auth import get_current_user_id, require_role
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

def generate_patient_id() -> str:
    """Generate unique patient ID"""
    timestamp = int(datetime.utcnow().timestamp())
    return f"P{timestamp}"

@router.get("/", response_model=List[PatientResponse])
async def get_patients(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100),
    search: Optional[str] = None,
    db=Depends(get_database),
    current_user_id: str = Depends(get_current_user_id),
    _: str = Depends(require_role(["admin", "doctor", "nurse"]))
):
    """Get all patients with pagination and search"""
    try:
        # Build query
        query = {"isActive": True}
        if search:
            query["$or"] = [
                {"personalInfo.firstName": {"$regex": search, "$options": "i"}},
                {"personalInfo.lastName": {"$regex": search, "$options": "i"}},
                {"patientId": {"$regex": search, "$options": "i"}},
                {"personalInfo.email": {"$regex": search, "$options": "i"}}
            ]
        
        # Get patients
        cursor = db.patients.find(query).skip(skip).limit(limit)
        patients = await cursor.to_list(length=limit)
        
        # Convert to response format
        response = []
        for patient in patients:
            response.append(PatientResponse(
                id=str(patient["_id"]),
                patientId=patient["patientId"],
                personalInfo=patient["personalInfo"],
                medicalInfo=patient["medicalInfo"],
                assignedDoctor=str(patient.get("assignedDoctor")) if patient.get("assignedDoctor") else None,
                registrationDate=patient["registrationDate"],
                lastVisit=patient.get("lastVisit"),
                isActive=patient["isActive"],
                createdAt=patient["createdAt"]
            ))
        
        return response
        
    except Exception as e:
        logger.error(f"Get patients error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )

@router.post("/", response_model=PatientResponse)
async def create_patient(
    patient_data: PatientCreate,
    db=Depends(get_database),
    current_user_id: str = Depends(get_current_user_id),
    _: str = Depends(require_role(["admin", "doctor", "nurse"]))
):
    """Create a new patient"""
    try:
        # Generate patient ID
        patient_id = generate_patient_id()
        
        # Check if patient ID already exists (unlikely but check anyway)
        existing = await db.patients.find_one({"patientId": patient_id})
        while existing:
            patient_id = generate_patient_id()
            existing = await db.patients.find_one({"patientId": patient_id})
        
        # Create patient document
        patient = Patient(
            patientId=patient_id,
            personalInfo=patient_data.personalInfo,
            medicalInfo=patient_data.medicalInfo,
            assignedDoctor=ObjectId(patient_data.assignedDoctor) if patient_data.assignedDoctor else None,
            createdBy=ObjectId(current_user_id)
        )
        
        # Insert patient
        result = await db.patients.insert_one(patient.dict(by_alias=True, exclude={"id"}))
        
        # Get created patient
        created_patient = await db.patients.find_one({"_id": result.inserted_id})
        
        return PatientResponse(
            id=str(created_patient["_id"]),
            patientId=created_patient["patientId"],
            personalInfo=created_patient["personalInfo"],
            medicalInfo=created_patient["medicalInfo"],
            assignedDoctor=str(created_patient.get("assignedDoctor")) if created_patient.get("assignedDoctor") else None,
            registrationDate=created_patient["registrationDate"],
            lastVisit=created_patient.get("lastVisit"),
            isActive=created_patient["isActive"],
            createdAt=created_patient["createdAt"]
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Create patient error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )

@router.get("/{patient_id}", response_model=PatientResponse)
async def get_patient(
    patient_id: str,
    db=Depends(get_database),
    current_user_id: str = Depends(get_current_user_id),
    _: str = Depends(require_role(["admin", "doctor", "nurse"]))
):
    """Get patient by ID"""
    try:
        # Find patient
        patient = await db.patients.find_one({"_id": ObjectId(patient_id)})
        
        if not patient:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Patient not found"
            )
        
        return PatientResponse(
            id=str(patient["_id"]),
            patientId=patient["patientId"],
            personalInfo=patient["personalInfo"],
            medicalInfo=patient["medicalInfo"],
            assignedDoctor=str(patient.get("assignedDoctor")) if patient.get("assignedDoctor") else None,
            registrationDate=patient["registrationDate"],
            lastVisit=patient.get("lastVisit"),
            isActive=patient["isActive"],
            createdAt=patient["createdAt"]
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Get patient error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )
