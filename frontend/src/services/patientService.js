import api from './api';

export const patientService = {
  // Get all patients
  getPatients: async (params = {}) => {
    const response = await api.get('/patients', { params });
    return response.data;
  },

  // Get patient by ID
  getPatient: async (id) => {
    const response = await api.get(`/patients/${id}`);
    return response.data;
  },

  // Create new patient
  createPatient: async (patientData) => {
    const response = await api.post('/patients', patientData);
    return response.data;
  },

  // Update patient
  updatePatient: async (id, patientData) => {
    const response = await api.put(`/patients/${id}`, patientData);
    return response.data;
  },

  // Delete patient
  deletePatient: async (id) => {
    const response = await api.delete(`/patients/${id}`);
    return response.data;
  },

  // Search patients
  searchPatients: async (query) => {
    const response = await api.get('/patients', { 
      params: { search: query } 
    });
    return response.data;
  },
};
