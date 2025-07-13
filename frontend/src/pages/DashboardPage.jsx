import React from 'react';
import { useAuth } from '../context/AuthContext';
import { 
  Users, 
  Activity, 
  Calendar, 
  FileText,
  TrendingUp,
  AlertTriangle,
  Clock,
  CheckCircle
} from 'lucide-react';

const DashboardPage = () => {
  const { user, isAdmin, isDoctor, isNurse } = useAuth();

  // Mock data for dashboard stats
  const stats = [
    {
      name: 'Total Patients',
      value: '1,234',
      change: '+12%',
      changeType: 'increase',
      icon: Users,
      color: 'bg-blue-500'
    },
    {
      name: 'Active Appointments',
      value: '56',
      change: '+8%',
      changeType: 'increase',
      icon: Calendar,
      color: 'bg-green-500'
    },
    {
      name: 'Pending Reports',
      value: '23',
      change: '-5%',
      changeType: 'decrease',
      icon: FileText,
      color: 'bg-yellow-500'
    },
    {
      name: 'Critical Alerts',
      value: '4',
      change: '+2',
      changeType: 'increase',
      icon: AlertTriangle,
      color: 'bg-red-500'
    }
  ];

  const recentActivities = [
    {
      id: 1,
      type: 'appointment',
      message: 'New appointment scheduled with Dr. Smith',
      time: '2 minutes ago',
      icon: Calendar,
      color: 'text-blue-600'
    },
    {
      id: 2,
      type: 'vital',
      message: 'High blood pressure alert for Patient #1234',
      time: '15 minutes ago',
      icon: Activity,
      color: 'text-red-600'
    },
    {
      id: 3,
      type: 'report',
      message: 'Lab report completed for Patient #5678',
      time: '1 hour ago',
      icon: FileText,
      color: 'text-green-600'
    },
    {
      id: 4,
      type: 'patient',
      message: 'New patient registration: Jane Doe',
      time: '2 hours ago',
      icon: Users,
      color: 'text-purple-600'
    }
  ];

  const upcomingAppointments = [
    {
      id: 1,
      patient: 'John Smith',
      time: '10:00 AM',
      type: 'Consultation',
      status: 'confirmed'
    },
    {
      id: 2,
      patient: 'Sarah Johnson',
      time: '11:30 AM',
      type: 'Follow-up',
      status: 'pending'
    },
    {
      id: 3,
      patient: 'Michael Brown',
      time: '2:00 PM',
      type: 'Check-up',
      status: 'confirmed'
    }
  ];

  return (
    <div className="p-6">
      {/* Welcome Header */}
      <div className="mb-8">
        <h1 className="text-2xl font-bold text-gray-900">
          Welcome back, {user?.profile?.firstName}!
        </h1>
        <p className="text-gray-600 mt-1">
          Here's what's happening at your clinic today.
        </p>
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        {stats.map((stat) => {
          const Icon = stat.icon;
          return (
            <div key={stat.name} className="card">
              <div className="flex items-center">
                <div className={`p-3 rounded-lg ${stat.color}`}>
                  <Icon className="w-6 h-6 text-white" />
                </div>
                <div className="ml-4">
                  <p className="text-sm font-medium text-gray-600">{stat.name}</p>
                  <div className="flex items-center">
                    <p className="text-2xl font-semibold text-gray-900">{stat.value}</p>
                    <span className={`ml-2 text-sm font-medium ${
                      stat.changeType === 'increase' ? 'text-green-600' : 'text-red-600'
                    }`}>
                      {stat.change}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          );
        })}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Recent Activities */}
        <div className="card">
          <div className="flex items-center justify-between mb-6">
            <h2 className="text-lg font-semibold text-gray-900">Recent Activities</h2>
            <button className="text-sm text-primary-600 hover:text-primary-700">
              View all
            </button>
          </div>
          <div className="space-y-4">
            {recentActivities.map((activity) => {
              const Icon = activity.icon;
              return (
                <div key={activity.id} className="flex items-start space-x-3">
                  <div className={`p-2 rounded-lg bg-gray-100 ${activity.color}`}>
                    <Icon className="w-4 h-4" />
                  </div>
                  <div className="flex-1 min-w-0">
                    <p className="text-sm text-gray-900">{activity.message}</p>
                    <p className="text-xs text-gray-500">{activity.time}</p>
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Upcoming Appointments */}
        <div className="card">
          <div className="flex items-center justify-between mb-6">
            <h2 className="text-lg font-semibold text-gray-900">Today's Appointments</h2>
            <button className="text-sm text-primary-600 hover:text-primary-700">
              View calendar
            </button>
          </div>
          <div className="space-y-4">
            {upcomingAppointments.map((appointment) => (
              <div key={appointment.id} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                <div className="flex items-center space-x-3">
                  <div className="flex items-center justify-center w-8 h-8 bg-primary-100 rounded-full">
                    <Clock className="w-4 h-4 text-primary-600" />
                  </div>
                  <div>
                    <p className="text-sm font-medium text-gray-900">{appointment.patient}</p>
                    <p className="text-xs text-gray-500">{appointment.type}</p>
                  </div>
                </div>
                <div className="text-right">
                  <p className="text-sm font-medium text-gray-900">{appointment.time}</p>
                  <span className={`inline-flex items-center px-2 py-1 rounded-full text-xs font-medium ${
                    appointment.status === 'confirmed' 
                      ? 'bg-green-100 text-green-800' 
                      : 'bg-yellow-100 text-yellow-800'
                  }`}>
                    {appointment.status === 'confirmed' ? (
                      <CheckCircle className="w-3 h-3 mr-1" />
                    ) : (
                      <Clock className="w-3 h-3 mr-1" />
                    )}
                    {appointment.status}
                  </span>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Quick Actions */}
      <div className="mt-8">
        <div className="card">
          <h2 className="text-lg font-semibold text-gray-900 mb-6">Quick Actions</h2>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            <button className="flex flex-col items-center p-4 bg-gray-50 rounded-lg hover:bg-gray-100 transition duration-200">
              <Users className="w-8 h-8 text-primary-600 mb-2" />
              <span className="text-sm font-medium text-gray-900">Add Patient</span>
            </button>
            <button className="flex flex-col items-center p-4 bg-gray-50 rounded-lg hover:bg-gray-100 transition duration-200">
              <Calendar className="w-8 h-8 text-primary-600 mb-2" />
              <span className="text-sm font-medium text-gray-900">Schedule Appointment</span>
            </button>
            <button className="flex flex-col items-center p-4 bg-gray-50 rounded-lg hover:bg-gray-100 transition duration-200">
              <Activity className="w-8 h-8 text-primary-600 mb-2" />
              <span className="text-sm font-medium text-gray-900">Record Vitals</span>
            </button>
            <button className="flex flex-col items-center p-4 bg-gray-50 rounded-lg hover:bg-gray-100 transition duration-200">
              <FileText className="w-8 h-8 text-primary-600 mb-2" />
              <span className="text-sm font-medium text-gray-900">View Reports</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DashboardPage;
