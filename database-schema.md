# MediTrack Database Schema (MongoDB)

## 🗄️ Database Collections Overview

```
MediTrack Database
├── users              # System users (doctors, nurses, admins)
├── patients           # Patient information
├── doctors            # Doctor profiles
├── vitals             # Patient vital signs
├── prescriptions      # Medical prescriptions
├── appointments       # Appointment scheduling
├── reports            # Medical reports and documents
├── notifications      # System notifications
└── audit_logs         # System audit trail
```

## 📊 Collection Schemas

### 1. Users Collection
```json
{
  "_id": "ObjectId",
  "username": "john_doctor",
  "email": "john@hospital.com",
  "password_hash": "hashed_password",
  "role": "doctor | nurse | admin | patient",
  "profile": {
    "firstName": "John",
    "lastName": "Smith",
    "phone": "+1234567890",
    "avatar": "url_to_avatar",
    "dateOfBirth": "1985-03-15",
    "gender": "male | female | other",
    "address": {
      "street": "123 Main St",
      "city": "New York",
      "state": "NY",
      "zipCode": "10001",
      "country": "USA"
    }
  },
  "isActive": true,
  "lastLogin": "2025-07-13T10:30:00Z",
  "createdAt": "2025-01-01T00:00:00Z",
  "updatedAt": "2025-07-13T10:30:00Z",
  "createdBy": "admin_user_id"
}
```

### 2. Patients Collection
```json
{
  "_id": "ObjectId",
  "patientId": "P001234",
  "personalInfo": {
    "firstName": "Jane",
    "lastName": "Doe",
    "dateOfBirth": "1990-05-20",
    "gender": "female",
    "phone": "+1234567890",
    "email": "jane.doe@email.com",
    "emergencyContact": {
      "name": "John Doe",
      "relationship": "spouse",
      "phone": "+1234567891"
    },
    "address": {
      "street": "456 Oak Ave",
      "city": "Boston",
      "state": "MA",
      "zipCode": "02101",
      "country": "USA"
    }
  },
  "medicalInfo": {
    "bloodType": "A+",
    "height": 165,  // cm
    "weight": 60,   // kg
    "allergies": ["penicillin", "shellfish"],
    "chronicConditions": ["diabetes", "hypertension"],
    "medications": ["metformin", "lisinopril"],
    "insuranceInfo": {
      "provider": "Blue Cross",
      "policyNumber": "BC123456789",
      "groupNumber": "GRP001"
    }
  },
  "assignedDoctor": "doctor_object_id",
  "registrationDate": "2025-01-15T09:00:00Z",
  "lastVisit": "2025-07-10T14:30:00Z",
  "isActive": true,
  "createdAt": "2025-01-15T09:00:00Z",
  "updatedAt": "2025-07-13T11:00:00Z",
  "createdBy": "user_id"
}
```

### 3. Doctors Collection
```json
{
  "_id": "ObjectId",
  "userId": "user_object_id",
  "licenseNumber": "MD123456",
  "specialization": ["cardiology", "internal_medicine"],
  "department": "Cardiology",
  "qualifications": [
    {
      "degree": "MD",
      "institution": "Harvard Medical School",
      "year": 2010
    }
  ],
  "experience": 15,  // years
  "consultationFee": 150.00,
  "schedule": {
    "monday": {
      "startTime": "09:00",
      "endTime": "17:00",
      "available": true
    },
    "tuesday": {
      "startTime": "09:00",
      "endTime": "17:00",
      "available": true
    }
    // ... other days
  },
  "isAvailable": true,
  "rating": 4.8,
  "totalPatients": 250,
  "createdAt": "2025-01-01T00:00:00Z",
  "updatedAt": "2025-07-13T10:00:00Z"
}
```

### 4. Vitals Collection
```json
{
  "_id": "ObjectId",
  "patientId": "patient_object_id",
  "recordedBy": "nurse_user_id",
  "vitals": {
    "bloodPressure": {
      "systolic": 120,
      "diastolic": 80
    },
    "heartRate": 75,      // bpm
    "temperature": 98.6,   // Fahrenheit
    "respiratoryRate": 16, // breaths per minute
    "oxygenSaturation": 98, // percentage
    "bloodSugar": 95,     // mg/dL
    "weight": 70,         // kg
    "height": 175         // cm
  },
  "notes": "Patient feeling well",
  "alerts": [
    {
      "type": "high_bp",
      "message": "Blood pressure above normal range",
      "severity": "warning | critical | info"
    }
  ],
  "recordedAt": "2025-07-13T14:30:00Z",
  "createdAt": "2025-07-13T14:30:00Z"
}
```

### 5. Prescriptions Collection
```json
{
  "_id": "ObjectId",
  "patientId": "patient_object_id",
  "doctorId": "doctor_object_id",
  "prescriptionNumber": "RX001234",
  "medications": [
    {
      "name": "Metformin",
      "dosage": "500mg",
      "frequency": "twice daily",
      "duration": "30 days",
      "instructions": "Take with meals",
      "quantity": 60
    }
  ],
  "diagnosis": "Type 2 Diabetes",
  "symptoms": ["increased thirst", "frequent urination"],
  "status": "active | completed | cancelled",
  "prescribedDate": "2025-07-13T10:00:00Z",
  "validUntil": "2025-08-13T10:00:00Z",
  "refillsRemaining": 2,
  "pharmacyNotes": "Patient counseled on medication",
  "createdAt": "2025-07-13T10:00:00Z",
  "updatedAt": "2025-07-13T10:00:00Z"
}
```

### 6. Appointments Collection
```json
{
  "_id": "ObjectId",
  "appointmentId": "APT001234",
  "patientId": "patient_object_id",
  "doctorId": "doctor_object_id",
  "appointmentType": "consultation | follow_up | emergency | check_up",
  "scheduledDate": "2025-07-15T14:00:00Z",
  "duration": 30,  // minutes
  "status": "scheduled | confirmed | in_progress | completed | cancelled | no_show",
  "reason": "Regular check-up",
  "symptoms": ["headache", "fatigue"],
  "notes": "Patient reports improvement",
  "consultationNotes": "Prescribed medication and follow-up in 2 weeks",
  "priority": "normal | urgent | emergency",
  "reminderSent": true,
  "cancelledBy": "patient | doctor | system",
  "cancellationReason": "Patient conflict",
  "createdAt": "2025-07-10T09:00:00Z",
  "updatedAt": "2025-07-13T11:00:00Z",
  "createdBy": "user_id"
}
```

### 7. Reports Collection
```json
{
  "_id": "ObjectId",
  "patientId": "patient_object_id",
  "doctorId": "doctor_object_id",
  "reportType": "lab_test | x_ray | mri | ct_scan | blood_test | other",
  "title": "Blood Test Results",
  "description": "Complete blood count and metabolic panel",
  "testDate": "2025-07-12T08:00:00Z",
  "results": {
    "hemoglobin": 14.5,
    "whiteBloodCells": 7500,
    "platelets": 300000,
    "glucose": 95
  },
  "normalRanges": {
    "hemoglobin": "12.0-15.5",
    "whiteBloodCells": "4000-11000",
    "platelets": "150000-450000",
    "glucose": "70-100"
  },
  "interpretation": "All values within normal limits",
  "files": [
    {
      "fileName": "blood_test_report.pdf",
      "fileUrl": "https://storage.com/reports/blood_test_report.pdf",
      "fileType": "pdf",
      "fileSize": 1024000  // bytes
    }
  ],
  "status": "pending | completed | reviewed",
  "priority": "normal | urgent | stat",
  "reviewedBy": "doctor_user_id",
  "reviewedAt": "2025-07-13T10:00:00Z",
  "createdAt": "2025-07-12T16:00:00Z",
  "updatedAt": "2025-07-13T10:00:00Z"
}
```

### 8. Notifications Collection
```json
{
  "_id": "ObjectId",
  "userId": "user_object_id",
  "type": "appointment | vital_alert | report_ready | prescription | system",
  "title": "Vital Signs Alert",
  "message": "Patient John Doe has elevated blood pressure",
  "data": {
    "patientId": "patient_object_id",
    "vitalId": "vital_object_id",
    "alertType": "high_bp"
  },
  "priority": "low | medium | high | critical",
  "isRead": false,
  "readAt": null,
  "actionRequired": true,
  "actionUrl": "/patients/123/vitals",
  "expiresAt": "2025-07-20T00:00:00Z",
  "createdAt": "2025-07-13T14:30:00Z"
}
```

### 9. Audit Logs Collection
```json
{
  "_id": "ObjectId",
  "userId": "user_object_id",
  "action": "CREATE | UPDATE | DELETE | LOGIN | LOGOUT",
  "resource": "patient | prescription | appointment | vital",
  "resourceId": "resource_object_id",
  "details": {
    "field": "bloodPressure",
    "oldValue": "120/80",
    "newValue": "140/90"
  },
  "ipAddress": "192.168.1.100",
  "userAgent": "Mozilla/5.0...",
  "timestamp": "2025-07-13T14:30:00Z"
}
```

## 🔗 Database Relationships

### Relationships Overview:
- **Users** → **Doctors** (1:1 for doctor users)
- **Doctors** → **Patients** (1:Many)
- **Patients** → **Vitals** (1:Many)
- **Patients** → **Prescriptions** (1:Many)
- **Patients** → **Appointments** (1:Many)
- **Patients** → **Reports** (1:Many)
- **Users** → **Notifications** (1:Many)

## 📋 Indexes for Performance

```javascript
// Users Collection
db.users.createIndex({ "email": 1 }, { unique: true })
db.users.createIndex({ "username": 1 }, { unique: true })
db.users.createIndex({ "role": 1 })

// Patients Collection
db.patients.createIndex({ "patientId": 1 }, { unique: true })
db.patients.createIndex({ "personalInfo.email": 1 })
db.patients.createIndex({ "assignedDoctor": 1 })
db.patients.createIndex({ "personalInfo.firstName": 1, "personalInfo.lastName": 1 })

// Vitals Collection
db.vitals.createIndex({ "patientId": 1, "recordedAt": -1 })
db.vitals.createIndex({ "recordedAt": -1 })

// Appointments Collection
db.appointments.createIndex({ "patientId": 1, "scheduledDate": 1 })
db.appointments.createIndex({ "doctorId": 1, "scheduledDate": 1 })
db.appointments.createIndex({ "scheduledDate": 1 })
db.appointments.createIndex({ "status": 1 })

// Prescriptions Collection
db.prescriptions.createIndex({ "patientId": 1, "prescribedDate": -1 })
db.prescriptions.createIndex({ "doctorId": 1, "prescribedDate": -1 })
db.prescriptions.createIndex({ "status": 1 })

// Reports Collection
db.reports.createIndex({ "patientId": 1, "testDate": -1 })
db.reports.createIndex({ "doctorId": 1, "testDate": -1 })
db.reports.createIndex({ "reportType": 1 })

// Notifications Collection
db.notifications.createIndex({ "userId": 1, "createdAt": -1 })
db.notifications.createIndex({ "isRead": 1 })
```

## 🔒 Data Validation Rules

1. **Email addresses** must be unique across users
2. **Patient IDs** must be unique and auto-generated
3. **Vital signs** must be within reasonable ranges
4. **Appointment times** cannot overlap for the same doctor
5. **User roles** must be from predefined enum values
6. **Phone numbers** must follow international format
7. **Medical data** requires proper validation and sanitization
