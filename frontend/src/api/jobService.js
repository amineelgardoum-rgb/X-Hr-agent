
import axios from 'axios';
const API_URL = 'http://localhost:8000/api/v1';

export const createJob = (jobData) => {
    return axios.post(`${API_URL}/jobs/`, jobData);
};

export const uploadCV = (formData) => {
    return axios.post(`${API_URL}/cvs/upload/`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
    });
};