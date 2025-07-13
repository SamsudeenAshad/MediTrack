from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "mongodb://localhost:27017/meditrack"
    
    # Security
    SECRET_KEY: str = "your-secret-key-here-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # CORS
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:5173"]
    
    # File Upload
    UPLOAD_DIR: str = "./uploads"
    MAX_FILE_SIZE: int = 10485760  # 10MB
    
    # Email (Optional)
    EMAIL_HOST: str = "smtp.gmail.com"
    EMAIL_PORT: int = 587
    EMAIL_USERNAME: str = ""
    EMAIL_PASSWORD: str = ""
    
    # Application
    APP_NAME: str = "MediTrack"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
