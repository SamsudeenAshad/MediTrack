# MediTrack API Routes Plan

## 🔗 Base URL
```
Development: http://localhost:8000/api/v1
Production: https://meditrack-api.com/api/v1
```

## 🔐 Authentication Routes
```
POST   /auth/login                 # User login
POST   /auth/logout                # User logout
POST   /auth/refresh               # Refresh JWT token
GET    /auth/me                    # Get current user info
POST   /auth/forgot-password       # Password reset request
POST   /auth/reset-password        # Reset password with token
```

## 👥 User Management Routes
```
GET    /users                      # Get all users (Admin only)
POST   /users                      # Create new user (Admin only)
GET    /users/{user_id}            # Get user by ID
PUT    /users/{user_id}            # Update user
DELETE /users/{user_id}            # Delete user (Admin only)
PATCH  /users/{user_id}/role       # Change user role (Admin only)
```

## 🏥 Doctor Routes
```
GET    /doctors                    # Get all doctors
POST   /doctors                    # Create doctor profile
GET    /doctors/{doctor_id}        # Get doctor by ID
PUT    /doctors/{doctor_id}        # Update doctor profile
DELETE /doctors/{doctor_id}        # Delete doctor (Admin only)
GET    /doctors/{doctor_id}/patients # Get doctor's patients
GET    /doctors/{doctor_id}/schedule # Get doctor's schedule
```

## 🧑‍⚕️ Patient Routes
```
GET    /patients                   # Get all patients (with pagination & filters)
POST   /patients                   # Create new patient
GET    /patients/{patient_id}      # Get patient by ID
PUT    /patients/{patient_id}      # Update patient info
DELETE /patients/{patient_id}      # Delete patient (Admin only)
GET    /patients/search           # Search patients by name/ID
GET    /patients/{patient_id}/history # Get complete medical history
GET    /patients/{patient_id}/vitals  # Get patient vitals
GET    /patients/{patient_id}/prescriptions # Get patient prescriptions
GET    /patients/{patient_id}/appointments # Get patient appointments
```

## 📊 Vitals Monitoring Routes
```
GET    /vitals                     # Get all vitals (with filters)
POST   /vitals                     # Record new vitals
GET    /vitals/{vital_id}          # Get specific vital record
PUT    /vitals/{vital_id}          # Update vital record
DELETE /vitals/{vital_id}          # Delete vital record
GET    /vitals/patient/{patient_id} # Get vitals for specific patient
GET    /vitals/patient/{patient_id}/latest # Get latest vitals
GET    /vitals/alerts              # Get vitals alerts (out of range)
POST   /vitals/bulk                # Bulk upload vitals
```

## 💊 Prescription Routes
```
GET    /prescriptions              # Get all prescriptions
POST   /prescriptions              # Create new prescription
GET    /prescriptions/{prescription_id} # Get prescription by ID
PUT    /prescriptions/{prescription_id} # Update prescription
DELETE /prescriptions/{prescription_id} # Delete prescription
GET    /prescriptions/patient/{patient_id} # Get patient prescriptions
GET    /prescriptions/doctor/{doctor_id}   # Get doctor's prescriptions
POST   /prescriptions/{prescription_id}/refill # Request refill
```

## 📅 Appointment Routes
```
GET    /appointments               # Get all appointments
POST   /appointments               # Create new appointment
GET    /appointments/{appointment_id} # Get appointment by ID
PUT    /appointments/{appointment_id} # Update appointment
DELETE /appointments/{appointment_id} # Cancel appointment
GET    /appointments/patient/{patient_id} # Get patient appointments
GET    /appointments/doctor/{doctor_id}   # Get doctor appointments
GET    /appointments/today         # Get today's appointments
POST   /appointments/{appointment_id}/reschedule # Reschedule appointment
PATCH  /appointments/{appointment_id}/status     # Update appointment status
```

## 📄 Reports & Documents Routes
```
GET    /reports                    # Get all reports
POST   /reports                    # Upload new report
GET    /reports/{report_id}        # Get report by ID
PUT    /reports/{report_id}        # Update report
DELETE /reports/{report_id}        # Delete report
GET    /reports/patient/{patient_id} # Get patient reports
POST   /reports/upload             # Upload file (PDF, images)
GET    /reports/{report_id}/download # Download report file
GET    /reports/types              # Get report types/categories
```

## 📈 Analytics & Dashboard Routes
```
GET    /analytics/overview         # Dashboard overview stats
GET    /analytics/patients/stats   # Patient statistics
GET    /analytics/vitals/trends    # Vitals trends analysis
GET    /analytics/appointments/stats # Appointment statistics
GET    /analytics/doctors/workload # Doctor workload analysis
GET    /analytics/alerts           # System alerts & notifications
GET    /analytics/reports/summary  # Reports summary
```

## 🔔 Notification Routes
```
GET    /notifications              # Get user notifications
POST   /notifications              # Create notification
GET    /notifications/{notification_id} # Get specific notification
PATCH  /notifications/{notification_id}/read # Mark as read
DELETE /notifications/{notification_id}      # Delete notification
GET    /notifications/unread       # Get unread notifications count
POST   /notifications/mark-all-read # Mark all as read
```

## 🔍 Search & Filter Routes
```
GET    /search/global              # Global search across all entities
GET    /search/patients            # Search patients
GET    /search/doctors             # Search doctors
GET    /search/reports             # Search reports
GET    /search/prescriptions       # Search prescriptions
```

## 📱 Mobile/Patient Portal Routes (Optional)
```
POST   /patient-portal/register    # Patient self-registration
GET    /patient-portal/profile     # Get patient profile
PUT    /patient-portal/profile     # Update patient profile
GET    /patient-portal/appointments # Get patient appointments
GET    /patient-portal/reports     # Get patient reports
GET    /patient-portal/vitals      # Get patient vitals
POST   /patient-portal/appointment-request # Request appointment
```

## 🔧 System Routes
```
GET    /health                     # Health check endpoint
GET    /version                    # API version info
GET    /docs                       # API documentation (Swagger)
```

## 📋 Route Permissions

| Role    | Permissions |
|---------|-------------|
| Admin   | Full access to all routes |
| Doctor  | Read/Write patients, vitals, prescriptions, appointments, reports |
| Nurse   | Read/Write vitals, Read patients, Limited appointment access |
| Patient | Read own data only (patient portal routes) |

## 🔒 Authentication Required
All routes except `/auth/login`, `/health`, and `/docs` require JWT authentication.

## 📄 Response Format
```json
{
  "success": true,
  "data": {...},
  "message": "Operation successful",
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 100,
    "totalPages": 10
  }
}
```

## ❌ Error Response Format
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [...]
  }
}
```
