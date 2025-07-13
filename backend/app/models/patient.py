from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime
from bson import ObjectId
from .user import PyObjectId, Gender, Address

class EmergencyContact(BaseModel):
    name: str
    relationship: str
    phone: str

class InsuranceInfo(BaseModel):
    provider: str
    policyNumber: str
    groupNumber: Optional[str] = None

class PersonalInfo(BaseModel):
    firstName: str
    lastName: str
    dateOfBirth: datetime
    gender: Gender
    phone: str
    email: Optional[EmailStr] = None
    emergencyContact: EmergencyContact
    address: Address

class MedicalInfo(BaseModel):
    bloodType: Optional[str] = None
    height: Optional[float] = None  # cm
    weight: Optional[float] = None  # kg
    allergies: List[str] = []
    chronicConditions: List[str] = []
    medications: List[str] = []
    insuranceInfo: Optional[InsuranceInfo] = None

class Patient(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    patientId: str = Field(..., unique=True)
    personalInfo: PersonalInfo
    medicalInfo: MedicalInfo
    assignedDoctor: Optional[PyObjectId] = None
    registrationDate: datetime = Field(default_factory=datetime.utcnow)
    lastVisit: Optional[datetime] = None
    isActive: bool = True
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    updatedAt: datetime = Field(default_factory=datetime.utcnow)
    createdBy: Optional[PyObjectId] = None

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class PatientCreate(BaseModel):
    personalInfo: PersonalInfo
    medicalInfo: Optional[MedicalInfo] = MedicalInfo()
    assignedDoctor: Optional[str] = None

class PatientUpdate(BaseModel):
    personalInfo: Optional[PersonalInfo] = None
    medicalInfo: Optional[MedicalInfo] = None
    assignedDoctor: Optional[str] = None
    lastVisit: Optional[datetime] = None
    isActive: Optional[bool] = None

class PatientResponse(BaseModel):
    id: str
    patientId: str
    personalInfo: PersonalInfo
    medicalInfo: MedicalInfo
    assignedDoctor: Optional[str] = None
    registrationDate: datetime
    lastVisit: Optional[datetime] = None
    isActive: bool
    createdAt: datetime
