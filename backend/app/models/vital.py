from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum
from bson import ObjectId
from .user import PyObjectId

class AlertSeverity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"

class VitalAlert(BaseModel):
    type: str
    message: str
    severity: AlertSeverity

class BloodPressure(BaseModel):
    systolic: int
    diastolic: int

class VitalsData(BaseModel):
    bloodPressure: Optional[BloodPressure] = None
    heartRate: Optional[int] = None  # bpm
    temperature: Optional[float] = None  # Fahrenheit
    respiratoryRate: Optional[int] = None  # breaths per minute
    oxygenSaturation: Optional[int] = None  # percentage
    bloodSugar: Optional[int] = None  # mg/dL
    weight: Optional[float] = None  # kg
    height: Optional[float] = None  # cm

class Vital(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    patientId: PyObjectId
    recordedBy: PyObjectId  # nurse or doctor user ID
    vitals: VitalsData
    notes: Optional[str] = None
    alerts: List[VitalAlert] = []
    recordedAt: datetime = Field(default_factory=datetime.utcnow)
    createdAt: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class VitalCreate(BaseModel):
    patientId: str
    vitals: VitalsData
    notes: Optional[str] = None

class VitalUpdate(BaseModel):
    vitals: Optional[VitalsData] = None
    notes: Optional[str] = None

class VitalResponse(BaseModel):
    id: str
    patientId: str
    recordedBy: str
    vitals: VitalsData
    notes: Optional[str] = None
    alerts: List[VitalAlert] = []
    recordedAt: datetime
    createdAt: datetime

class VitalsBulkCreate(BaseModel):
    vitals: List[VitalCreate]
