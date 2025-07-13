import React, { useState } from 'react';
import { useQuery } from 'react-query';
import { patientService } from '../services/patientService';
import { 
  Search, 
  Plus, 
  Filter, 
  MoreVertical,
  Eye,
  Edit,
  Trash2,
  Phone,
  Mail,
  Calendar
} from 'lucide-react';
import toast from 'react-hot-toast';

const PatientsPage = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [currentPage, setCurrentPage] = useState(1);
  const [showAddModal, setShowAddModal] = useState(false);

  // Fetch patients
  const { data: patients, isLoading, error, refetch } = useQuery(
    ['patients', currentPage, searchTerm],
    () => patientService.getPatients({
      skip: (currentPage - 1) * 10,
      limit: 10,
      search: searchTerm
    }),
    {
      keepPreviousData: true,
    }
  );

  // Mock data for demo (since backend might not be running)
  const mockPatients = [
    {
      id: '1',
      patientId: 'P001234',
      personalInfo: {
        firstName: 'John',
        lastName: 'Doe',
        email: 'john.doe@email.com',
        phone: '+1234567890',
        dateOfBirth: '1985-03-15',
        gender: 'male',
        address: {
          street: '123 Main St',
          city: 'New York',
          state: 'NY',
          zipCode: '10001'
        }
      },
      medicalInfo: {
        bloodType: 'A+',
        allergies: ['penicillin'],
        chronicConditions: ['diabetes']
      },
      lastVisit: '2025-07-10',
      isActive: true
    },
    {
      id: '2',
      patientId: 'P001235',
      personalInfo: {
        firstName: 'Jane',
        lastName: 'Smith',
        email: 'jane.smith@email.com',
        phone: '+1234567891',
        dateOfBirth: '1990-07-22',
        gender: 'female',
        address: {
          street: '456 Oak Ave',
          city: 'Boston',
          state: 'MA',
          zipCode: '02101'
        }
      },
      medicalInfo: {
        bloodType: 'O-',
        allergies: ['shellfish'],
        chronicConditions: ['hypertension']
      },
      lastVisit: '2025-07-12',
      isActive: true
    }
  ];

  const displayPatients = patients || mockPatients;

  const handleSearch = (e) => {
    setSearchTerm(e.target.value);
    setCurrentPage(1);
  };

  const handleViewPatient = (patientId) => {
    toast.success(`Viewing patient ${patientId}`);
    // Navigate to patient detail page
  };

  const handleEditPatient = (patientId) => {
    toast.success(`Editing patient ${patientId}`);
    // Open edit modal
  };

  const handleDeletePatient = (patientId) => {
    if (window.confirm('Are you sure you want to delete this patient?')) {
      toast.success(`Patient ${patientId} deleted`);
      // Implement delete functionality
    }
  };

  const calculateAge = (dateOfBirth) => {
    const today = new Date();
    const birthDate = new Date(dateOfBirth);
    let age = today.getFullYear() - birthDate.getFullYear();
    const monthDiff = today.getMonth() - birthDate.getMonth();
    
    if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
      age--;
    }
    
    return age;
  };

  return (
    <div className="p-6">
      {/* Header */}
      <div className="flex items-center justify-between mb-6">
        <div>
          <h1 className="text-2xl font-bold text-gray-900">Patients</h1>
          <p className="text-gray-600 mt-1">Manage patient records and information</p>
        </div>
        <button 
          onClick={() => setShowAddModal(true)}
          className="btn-primary flex items-center space-x-2"
        >
          <Plus className="w-4 h-4" />
          <span>Add Patient</span>
        </button>
      </div>

      {/* Search and Filters */}
      <div className="card mb-6">
        <div className="flex flex-col sm:flex-row gap-4">
          <div className="flex-1 relative">
            <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-4 h-4" />
            <input
              type="text"
              placeholder="Search patients by name, ID, or email..."
              value={searchTerm}
              onChange={handleSearch}
              className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent"
            />
          </div>
          <button className="btn-secondary flex items-center space-x-2">
            <Filter className="w-4 h-4" />
            <span>Filters</span>
          </button>
        </div>
      </div>

      {/* Patients Table */}
      <div className="card">
        {isLoading ? (
          <div className="flex items-center justify-center py-8">
            <div className="animate-spin rounded-full h-8 w-8 border-2 border-primary-600 border-t-transparent"></div>
          </div>
        ) : error ? (
          <div className="text-center py-8">
            <p className="text-red-600 mb-4">Error loading patients</p>
            <button onClick={refetch} className="btn-primary">
              Try Again
            </button>
          </div>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full">
              <thead>
                <tr className="border-b border-gray-200">
                  <th className="text-left py-3 px-4 font-medium text-gray-700">Patient</th>
                  <th className="text-left py-3 px-4 font-medium text-gray-700">Patient ID</th>
                  <th className="text-left py-3 px-4 font-medium text-gray-700">Contact</th>
                  <th className="text-left py-3 px-4 font-medium text-gray-700">Age/Gender</th>
                  <th className="text-left py-3 px-4 font-medium text-gray-700">Last Visit</th>
                  <th className="text-left py-3 px-4 font-medium text-gray-700">Status</th>
                  <th className="text-left py-3 px-4 font-medium text-gray-700">Actions</th>
                </tr>
              </thead>
              <tbody>
                {displayPatients.map((patient) => (
                  <tr key={patient.id} className="border-b border-gray-100 hover:bg-gray-50">
                    <td className="py-4 px-4">
                      <div className="flex items-center space-x-3">
                        <div className="flex items-center justify-center w-10 h-10 bg-primary-100 rounded-full">
                          <span className="text-primary-600 font-medium">
                            {patient.personalInfo.firstName[0]}{patient.personalInfo.lastName[0]}
                          </span>
                        </div>
                        <div>
                          <p className="font-medium text-gray-900">
                            {patient.personalInfo.firstName} {patient.personalInfo.lastName}
                          </p>
                          <p className="text-sm text-gray-500">
                            {patient.medicalInfo.bloodType} • {patient.medicalInfo.allergies.join(', ') || 'No allergies'}
                          </p>
                        </div>
                      </div>
                    </td>
                    <td className="py-4 px-4">
                      <span className="font-mono text-sm text-gray-600">{patient.patientId}</span>
                    </td>
                    <td className="py-4 px-4">
                      <div className="space-y-1">
                        <div className="flex items-center space-x-1 text-sm text-gray-600">
                          <Phone className="w-3 h-3" />
                          <span>{patient.personalInfo.phone}</span>
                        </div>
                        <div className="flex items-center space-x-1 text-sm text-gray-600">
                          <Mail className="w-3 h-3" />
                          <span>{patient.personalInfo.email}</span>
                        </div>
                      </div>
                    </td>
                    <td className="py-4 px-4">
                      <div>
                        <p className="text-sm text-gray-900">
                          {calculateAge(patient.personalInfo.dateOfBirth)} years
                        </p>
                        <p className="text-sm text-gray-500 capitalize">
                          {patient.personalInfo.gender}
                        </p>
                      </div>
                    </td>
                    <td className="py-4 px-4">
                      <div className="flex items-center space-x-1 text-sm text-gray-600">
                        <Calendar className="w-3 h-3" />
                        <span>{new Date(patient.lastVisit).toLocaleDateString()}</span>
                      </div>
                    </td>
                    <td className="py-4 px-4">
                      <span className={`badge ${patient.isActive ? 'badge-success' : 'badge-danger'}`}>
                        {patient.isActive ? 'Active' : 'Inactive'}
                      </span>
                    </td>
                    <td className="py-4 px-4">
                      <div className="flex items-center space-x-2">
                        <button
                          onClick={() => handleViewPatient(patient.patientId)}
                          className="p-1 text-gray-400 hover:text-primary-600 transition duration-200"
                          title="View Patient"
                        >
                          <Eye className="w-4 h-4" />
                        </button>
                        <button
                          onClick={() => handleEditPatient(patient.patientId)}
                          className="p-1 text-gray-400 hover:text-yellow-600 transition duration-200"
                          title="Edit Patient"
                        >
                          <Edit className="w-4 h-4" />
                        </button>
                        <button
                          onClick={() => handleDeletePatient(patient.patientId)}
                          className="p-1 text-gray-400 hover:text-red-600 transition duration-200"
                          title="Delete Patient"
                        >
                          <Trash2 className="w-4 h-4" />
                        </button>
                        <button className="p-1 text-gray-400 hover:text-gray-600 transition duration-200">
                          <MoreVertical className="w-4 h-4" />
                        </button>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

        {/* Pagination */}
        <div className="flex items-center justify-between px-4 py-3 border-t border-gray-200">
          <div className="text-sm text-gray-700">
            Showing 1 to {displayPatients.length} of {displayPatients.length} patients
          </div>
          <div className="flex items-center space-x-2">
            <button
              disabled={currentPage === 1}
              onClick={() => setCurrentPage(currentPage - 1)}
              className="px-3 py-1 text-sm border border-gray-300 rounded hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Previous
            </button>
            <span className="px-3 py-1 text-sm bg-primary-100 text-primary-700 rounded">
              {currentPage}
            </span>
            <button
              onClick={() => setCurrentPage(currentPage + 1)}
              className="px-3 py-1 text-sm border border-gray-300 rounded hover:bg-gray-50"
            >
              Next
            </button>
          </div>
        </div>
      </div>

      {/* Add Patient Modal Placeholder */}
      {showAddModal && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white rounded-lg p-6 w-full max-w-md">
            <h2 className="text-lg font-semibold mb-4">Add New Patient</h2>
            <p className="text-gray-600 mb-4">Patient form will be implemented here.</p>
            <div className="flex justify-end space-x-2">
              <button 
                onClick={() => setShowAddModal(false)}
                className="btn-secondary"
              >
                Cancel
              </button>
              <button 
                onClick={() => {
                  setShowAddModal(false);
                  toast.success('Patient form coming soon!');
                }}
                className="btn-primary"
              >
                Save
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default PatientsPage;
