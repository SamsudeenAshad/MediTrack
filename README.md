# 🏥 MediTrack - Smart Patient Monitoring & Medical Records System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![React](https://img.shields.io/badge/React-18+-61DAFB.svg)](https://reactjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-009688.svg)](https://fastapi.tiangolo.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-7.0+-47A248.svg)](https://www.mongodb.com/)

A comprehensive healthcare management platform built with **MongoDB**, **FastAPI**, and **React** that enables hospitals and clinics to efficiently manage patient records, monitor vitals, schedule appointments, and maintain medical documentation.

## ✨ Features

### 🔐 **Role-Based Access Control**
- **Admin**: Complete system management, user creation, analytics
- **Doctor**: Patient management, prescriptions, appointments, medical records
- **Nurse**: Vitals monitoring, patient updates, daily reports
- **Patient Portal**: Personal health records access (optional)

### 👥 **Patient Management**
- Complete patient profiles with medical history
- Advanced search and filtering capabilities
- Medical record management
- Emergency contact information
- Insurance details tracking

### 📊 **Vitals Monitoring**
- Real-time vital signs tracking (BP, heart rate, temperature, etc.)
- Automated alerts for abnormal readings
- Historical trends and analytics
- Bulk vitals import functionality

### 📅 **Appointment System**
- Intelligent scheduling with doctor availability
- Appointment status management
- Automated reminders and notifications
- Calendar integration

### 📄 **Medical Reports**
- Lab report uploads and management
- PDF and image file support
- Report categorization and search
- Doctor review and annotation system

### 📈 **Analytics Dashboard**
- Real-time system metrics
- Patient statistics and trends
- Medical analytics and insights
- Custom reporting capabilities

## 🛠 Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Frontend** | React 18 + Tailwind CSS | Modern, responsive user interface |
| **Backend** | FastAPI + Python 3.11 | High-performance API with automatic docs |
| **Database** | MongoDB 7.0 | Flexible, scalable document database |
| **Authentication** | JWT + Role-based access | Secure user authentication |
| **File Storage** | Local/Cloud storage | Medical document management |
| **Charts** | Recharts | Data visualization |
| **Deployment** | Docker + Docker Compose | Containerized deployment |

## 🚀 Quick Start

### Prerequisites
- **Docker** and **Docker Compose** installed
- **Node.js 18+** (for local development)
- **Python 3.11+** (for local development)
- **MongoDB 7.0+** (if running locally)

### 🐳 Docker Setup (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/SamsudeenAshad/MediTrack.git
   cd MediTrack
   ```

2. **Environment setup**
   ```bash
   # Copy backend environment file
   cp backend/.env.example backend/.env
   
   # Update backend/.env with your configuration
   # Change SECRET_KEY and other sensitive values
   ```

3. **Start all services**
   ```bash
   docker-compose up -d
   ```

4. **Access the application**
   - **Frontend**: http://localhost:3000
   - **Backend API**: http://localhost:8000
   - **API Documentation**: http://localhost:8000/docs
   - **MongoDB**: localhost:27017

### 🖥 Local Development Setup

#### Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env

# Start the backend server
uvicorn app.main:app --reload --port 8000
```

#### Frontend Setup
```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

## 🔑 Demo Credentials

For testing purposes, you can use these demo credentials:

| Role | Username | Password |
|------|----------|----------|
| Admin | `admin` | `admin123` |
| Doctor | `doctor` | `doctor123` |
| Nurse | `nurse` | `nurse123` |

> **Note**: These are demo credentials. In production, create secure accounts through the admin panel.

## 📁 Project Structure

```
MediTrack/
├── backend/                    # FastAPI Backend
│   ├── app/
│   │   ├── config/            # Database & settings
│   │   ├── models/            # Pydantic models
│   │   ├── routes/            # API endpoints
│   │   ├── services/          # Business logic
│   │   ├── utils/             # Helper functions
│   │   └── main.py            # FastAPI app
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/                   # React Frontend
│   ├── src/
│   │   ├── components/        # React components
│   │   ├── pages/             # Page components
│   │   ├── services/          # API services
│   │   ├── context/           # React context
│   │   └── styles/            # CSS styles
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## 🔌 API Endpoints

### Authentication
- `POST /api/v1/auth/login` - User login
- `GET /api/v1/auth/me` - Get current user
- `POST /api/v1/auth/logout` - User logout

### Patients
- `GET /api/v1/patients` - List patients
- `POST /api/v1/patients` - Create patient
- `GET /api/v1/patients/{id}` - Get patient details
- `PUT /api/v1/patients/{id}` - Update patient

### Vitals
- `GET /api/v1/vitals` - List vital records
- `POST /api/v1/vitals` - Record new vitals
- `GET /api/v1/vitals/patient/{id}` - Patient vitals

### More endpoints available at `/docs` when running the backend

## 🗄 Database Schema

### Key Collections

**Users Collection**
```javascript
{
  "_id": "ObjectId",
  "username": "string",
  "email": "string",
  "role": "admin|doctor|nurse|patient",
  "profile": { /* user profile data */ },
  "isActive": "boolean"
}
```

**Patients Collection**
```javascript
{
  "_id": "ObjectId",
  "patientId": "string",
  "personalInfo": { /* personal details */ },
  "medicalInfo": { /* medical history */ },
  "assignedDoctor": "ObjectId"
}
```

**Vitals Collection**
```javascript
{
  "_id": "ObjectId",
  "patientId": "ObjectId",
  "vitals": { /* vital signs data */ },
  "alerts": [ /* automated alerts */ ],
  "recordedAt": "datetime"
}
```

## 🔧 Configuration

### Environment Variables

**Backend (.env)**
```env
DATABASE_URL=mongodb://localhost:27017/meditrack
SECRET_KEY=your-secret-key-here
ACCESS_TOKEN_EXPIRE_MINUTES=30
ALLOWED_ORIGINS=http://localhost:3000
```

**Frontend**
```env
REACT_APP_API_URL=http://localhost:8000/api/v1
```

## 🚀 Deployment

### Production Deployment

1. **Update environment variables** for production
2. **Build and deploy** using Docker Compose
3. **Set up reverse proxy** (Nginx recommended)
4. **Configure SSL** certificates
5. **Set up backup** strategy for MongoDB

### Cloud Deployment Options

- **Railway**: Easy deployment with built-in PostgreSQL
- **Render**: Full-stack deployment with database
- **Vercel**: Frontend deployment
- **Heroku**: Complete application deployment
- **AWS/Azure/GCP**: Enterprise-grade deployment

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Samudeen Ashad**
- GitHub: [@SamsudeenAshad](https://github.com/SamsudeenAshad)

## 🙏 Acknowledgments

- **FastAPI** for the excellent Python framework
- **React** team for the amazing frontend library
- **MongoDB** for the flexible database solution
- **Tailwind CSS** for the utility-first CSS framework

## 📞 Support

If you have any questions or need help, please:
1. Check the [API documentation](http://localhost:8000/docs)
2. Create an [issue](https://github.com/SamsudeenAshad/MediTrack/issues)
3. Review the project documentation

---

**⭐ If you find this project helpful, please give it a star on GitHub!**
Smart Patient Monitoring &amp; Medical Records System
