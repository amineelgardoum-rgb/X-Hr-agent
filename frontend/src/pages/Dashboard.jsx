import React, { useState } from 'react';
import { createJob, uploadCV } from '../api/jobService';

export default function DashboardPage() {
    const [title, setTitle] = useState('');
    const [file, setFile] = useState(null);
    const [message, setMessage] = useState('Welcome! Please create a job or upload a CV.');

    const handleCreateJob = async () => {
        if (!title) {
            setMessage('Please enter a job title.');
            return;
        }
        try {
            const jobData = { title, description: "Default description", requirements: ["Python", "SQL"] };
            const response = await createJob(jobData);
            setMessage(`Job created successfully: ${response.data.title}`);
        } catch (error) {
            setMessage('Error: Failed to create job.');
            console.error(error);
        }
    };
    
    const handleUpload = async () => {
        if (!file) {
            setMessage('Please select a file to upload.');
            return;
        }
        const formData = new FormData();
        formData.append('file', file);
        try {
            const response = await uploadCV(formData);
            setMessage(`Successfully uploaded and parsed CV: ${response.data.filename}`);
        } catch (error) {
            setMessage('Error: Failed to upload CV.');
            console.error(error);
        }
    };

    return (
        <div style={{ maxWidth: '800px', margin: '40px auto', fontFamily: 'Arial, sans-serif' }}>
            <h1>X-HR Agent Dashboard</h1>
            <p style={{ padding: '10px', backgroundColor: '#f0f0f0', borderRadius: '5px' }}>
                <strong>Status:</strong> {message}
            </p>
            
            <div style={{ border: '1px solid #ccc', padding: '20px', marginBottom: '20px', borderRadius: '5px' }}>
                <h2>Create a New Job</h2>
                <input 
                    style={{ padding: '8px', marginRight: '10px' }}
                    onChange={(e) => setTitle(e.target.value)} 
                    placeholder="Enter Job Title" 
                />
                <button style={{ padding: '8px 12px' }} onClick={handleCreateJob}>Create Job</button>
            </div>
            
            <div style={{ border: '1px solid #ccc', padding: '20px', borderRadius: '5px' }}>
                <h2>Upload a Candidate CV</h2>
                <input 
                    type="file" 
                    style={{ marginRight: '10px' }}
                    onChange={(e) => setFile(e.target.files[0])} 
                />
                <button style={{ padding: '8px 12px' }} onClick={handleUpload}>Upload CV</button>
            </div>
        </div>
    );
}