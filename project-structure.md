# MediTrack - Project Structure

## 📁 Folder Structure

```
MediTrack/
├── backend/                    # FastAPI Backend
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py            # FastAPI app entry point
│   │   ├── config/
│   │   │   ├── __init__.py
│   │   │   ├── database.py    # MongoDB connection
│   │   │   └── settings.py    # Environment variables
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── user.py        # User model
│   │   │   ├── patient.py     # Patient model
│   │   │   ├── doctor.py      # Doctor model
│   │   │   ├── vital.py       # Vitals model
│   │   │   ├── prescription.py
│   │   │   ├── appointment.py
│   │   │   └── report.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py        # Authentication routes
│   │   │   ├── patients.py    # Patient CRUD
│   │   │   ├── doctors.py     # Doctor CRUD
│   │   │   ├── vitals.py      # Vitals monitoring
│   │   │   ├── prescriptions.py
│   │   │   ├── appointments.py
│   │   │   ├── reports.py
│   │   │   └── analytics.py   # Medical analytics
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── auth_service.py
│   │   │   ├── patient_service.py
│   │   │   ├── notification_service.py
│   │   │   └── analytics_service.py
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py        # JWT utilities
│   │   │   ├── validators.py  # Data validation
│   │   │   └── helpers.py     # Common utilities
│   │   └── middleware/
│   │       ├── __init__.py
│   │       ├── cors.py
│   │       └── auth_middleware.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
├── frontend/                   # React Frontend
│   ├── public/
│   │   ├── index.html
│   │   └── favicon.ico
│   ├── src/
│   │   ├── components/
│   │   │   ├── common/
│   │   │   │   ├── Header.jsx
│   │   │   │   ├── Sidebar.jsx
│   │   │   │   ├── Layout.jsx
│   │   │   │   └── LoadingSpinner.jsx
│   │   │   ├── auth/
│   │   │   │   ├── LoginForm.jsx
│   │   │   │   └── PrivateRoute.jsx
│   │   │   ├── dashboard/
│   │   │   │   ├── DoctorDashboard.jsx
│   │   │   │   ├── NurseDashboard.jsx
│   │   │   │   └── AdminDashboard.jsx
│   │   │   ├── patients/
│   │   │   │   ├── PatientList.jsx
│   │   │   │   ├── PatientProfile.jsx
│   │   │   │   ├── PatientForm.jsx
│   │   │   │   └── MedicalHistory.jsx
│   │   │   ├── vitals/
│   │   │   │   ├── VitalsChart.jsx
│   │   │   │   ├── VitalsForm.jsx
│   │   │   │   └── VitalsDashboard.jsx
│   │   │   ├── appointments/
│   │   │   │   ├── AppointmentCalendar.jsx
│   │   │   │   └── AppointmentForm.jsx
│   │   │   └── reports/
│   │   │       ├── ReportsList.jsx
│   │   │       └── ReportUpload.jsx
│   │   ├── pages/
│   │   │   ├── LoginPage.jsx
│   │   │   ├── DashboardPage.jsx
│   │   │   ├── PatientsPage.jsx
│   │   │   ├── VitalsPage.jsx
│   │   │   ├── AppointmentsPage.jsx
│   │   │   └── ReportsPage.jsx
│   │   ├── services/
│   │   │   ├── api.js         # Axios configuration
│   │   │   ├── authService.js
│   │   │   ├── patientService.js
│   │   │   ├── vitalsService.js
│   │   │   └── appointmentService.js
│   │   ├── context/
│   │   │   ├── AuthContext.jsx
│   │   │   └── ThemeContext.jsx
│   │   ├── hooks/
│   │   │   ├── useAuth.js
│   │   │   └── useApi.js
│   │   ├── utils/
│   │   │   ├── constants.js
│   │   │   ├── formatters.js
│   │   │   └── validators.js
│   │   ├── styles/
│   │   │   ├── globals.css
│   │   │   └── components.css
│   │   ├── App.jsx
│   │   └── index.js
│   ├── package.json
│   ├── tailwind.config.js
│   └── Dockerfile
├── docker-compose.yml
├── README.md
└── docs/
    ├── api-documentation.md
    ├── database-schema.md
    └── deployment-guide.md
```

## 🎯 Key Architecture Decisions

1. **Separation of Concerns**: Clear separation between backend and frontend
2. **Modular Structure**: Each feature has its own components, services, and routes
3. **Role-Based Access**: Different dashboards for different user types
4. **Scalable Design**: Easy to add new features and modules
5. **Docker Ready**: Containerized for easy deployment
