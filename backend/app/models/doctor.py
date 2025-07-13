from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from datetime import datetime, time
from bson import ObjectId
from .user import PyObjectId

class Qualification(BaseModel):
    degree: str
    institution: str
    year: int

class DaySchedule(BaseModel):
    startTime: str  # "09:00"
    endTime: str    # "17:00"
    available: bool = True

class WeeklySchedule(BaseModel):
    monday: Optional[DaySchedule] = None
    tuesday: Optional[DaySchedule] = None
    wednesday: Optional[DaySchedule] = None
    thursday: Optional[DaySchedule] = None
    friday: Optional[DaySchedule] = None
    saturday: Optional[DaySchedule] = None
    sunday: Optional[DaySchedule] = None

class Doctor(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    userId: PyObjectId
    licenseNumber: str = Field(..., unique=True)
    specialization: List[str] = []
    department: str
    qualifications: List[Qualification] = []
    experience: int = 0  # years
    consultationFee: float = 0.0
    schedule: Optional[WeeklySchedule] = None
    isAvailable: bool = True
    rating: float = 0.0
    totalPatients: int = 0
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    updatedAt: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class DoctorCreate(BaseModel):
    userId: str
    licenseNumber: str
    specialization: List[str] = []
    department: str
    qualifications: List[Qualification] = []
    experience: int = 0
    consultationFee: float = 0.0
    schedule: Optional[WeeklySchedule] = None

class DoctorUpdate(BaseModel):
    licenseNumber: Optional[str] = None
    specialization: Optional[List[str]] = None
    department: Optional[str] = None
    qualifications: Optional[List[Qualification]] = None
    experience: Optional[int] = None
    consultationFee: Optional[float] = None
    schedule: Optional[WeeklySchedule] = None
    isAvailable: Optional[bool] = None

class DoctorResponse(BaseModel):
    id: str
    userId: str
    licenseNumber: str
    specialization: List[str]
    department: str
    qualifications: List[Qualification]
    experience: int
    consultationFee: float
    schedule: Optional[WeeklySchedule]
    isAvailable: bool
    rating: float
    totalPatients: int
    createdAt: datetime
