from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
import os
from dotenv import load_dotenv

from app.config.database import connect_to_mongo, close_mongo_connection
from app.config.settings import settings
from app.routes import auth, patients, doctors, vitals, prescriptions, appointments, reports, analytics

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="MediTrack API",
    description="Smart Patient Monitoring & Medical Records System",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS.split(','),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files for uploads
if not os.path.exists("uploads"):
    os.makedirs("uploads")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# Database events
@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()

# Health check endpoint
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION
    }

# API Routes
app.include_router(auth.router, prefix="/api/v1/auth", tags=["authentication"])
app.include_router(patients.router, prefix="/api/v1/patients", tags=["patients"])
app.include_router(doctors.router, prefix="/api/v1/doctors", tags=["doctors"])
app.include_router(vitals.router, prefix="/api/v1/vitals", tags=["vitals"])
app.include_router(prescriptions.router, prefix="/api/v1/prescriptions", tags=["prescriptions"])
app.include_router(appointments.router, prefix="/api/v1/appointments", tags=["appointments"])
app.include_router(reports.router, prefix="/api/v1/reports", tags=["reports"])
app.include_router(analytics.router, prefix="/api/v1/analytics", tags=["analytics"])

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Welcome to MediTrack API",
        "docs": "/docs",
        "health": "/health"
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG
    )
