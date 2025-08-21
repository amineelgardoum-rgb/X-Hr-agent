

# X-HR Agent MVP

An AI-Powered Recruitment Platform for SMEs, designed to streamline the hiring process from CV parsing to candidate matching.

This repository contains the full specification and runnable Minimum Viable Product (MVP) code for the X-HR Agent, a recruitment platform targeting Small and Medium-sized Enterprises. The project aims to leverage AI to automate tedious recruitment tasks, provide explainable matching, and offer a simple, intuitive workflow for users without dedicated HR staff.

---

## ✨ Core Features

*   **🤖 AI-Powered CV Processing:** Ingests resumes in multiple formats (PDF, DOCX, images) and uses OCR and NER to extract structured data like skills, experience, and contact information.
*   **🎯 Explainable Job Matching:** Utilizes a hybrid model combining semantic similarity (via text embeddings) and direct skill overlap to rank candidates. Crucially, it provides a clear rationale for each match score.
*   **🗣️ Interview Simulation:** Employs an LLM to generate job-relevant questions and provides a preliminary screening of candidates through a text-based simulated interview.
*   **📊 SME-Focused Dashboard:** A clean, intuitive UI for managing job postings, viewing ranked candidate lists, and tracking applicants. Includes basic analytics on hiring performance.

---

## 🛠️ Tech Stack & Architecture

The project follows a modern, containerized microservices architecture to ensure scalability and separation of concerns.

*   **Frontend:**
    *   **Framework:** React (with Vite)
    *   **Styling:** Tailwind CSS (or as specified)
    *   **API Communication:** Axios
*   **Backend (API Gateway):**
    *   **Framework:** Python 3.8+ with FastAPI
    *   **Data Validation:** Pydantic
    *   **ASGI Server:** Uvicorn
*   **Database:**
    *   **Primary:** MongoDB (for storing jobs, candidates, user data)
    *   **Object Storage:** MinIO / S3 (for storing raw CV files)
*   **AI Services:**
    *   **NLP/NER:** spaCy
    *   **Embeddings:** SentenceTransformers (or similar)
    *   **Interview Sim:** A fine-tuned Large Language Model (e.g., from Hugging Face)
*   **Deployment:**
    *   **Containerization:** Docker & Docker Compose
    *   **Web Server (Frontend):** Vite

---

## 🚀 Getting Started: Running the MVP

These instructions will guide you through running the simplified MVP codebase on your local machine.

### Prerequisites

*   [Git](https://git-scm.com/)
*   [Node.js](https://nodejs.org/) (v16 or higher)
*   [Python](https://www.python.org/) (v3.8 or higher) and `pip`

### 1. Installation

First, clone the repository and navigate into the project directory.

```bash
git clone https://github.com/amineelgardoum-rgb/X-Hr-agent
cd X-Hr-agent
```

Next, set up the backend and frontend environments in two separate terminals.

**Terminal 1: Backend Setup**

```bash
# Navigate to the backend directory
cd backend

# Create and activate a Python virtual environment
python -m venv venv
# On Windows:
# .\venv\Scripts\activate
# On macOS/Linux:
# source venv/bin/activate

# Install the required Python packages
pip install -r requirements.txt
```

**Terminal 2: Frontend Setup**

```bash
# Navigate to the frontend directory
cd frontend

# Install the required Node.js packages
npm install
```

### 2. Running the Application

Now, start both the backend and frontend servers.

**Terminal 1: Start the Backend**

```bash
# Make sure you are in the `backend` directory with the venv activated
uvicorn app.main:app --reload
```

Your FastAPI server should now be running at `http://127.0.0.1:8000`.

**Terminal 2: Start the Frontend**

```bash
# Make sure you are in the `frontend` directory
npm run dev
```

Your React application should automatically open in your browser at `http://localhost:5173`.

### 3. Using the MVP

1. The dashboard will load in your browser.
2. Use the "Create a New Job" card to define a job title.
3. Use the "Upload a Candidate CV" card to upload a dummy file.
4. The status message at the top will provide feedback on each action.

---

## 📁 Project Structure

The codebase is organized into two main parts: `backend` and `frontend`, with a professional, scalable structure.

### Backend Structure

```
backend/
├── app/                  # Main application source code
│   ├── api/              # API endpoints (routers)
│   │   ├── endpoints/    # Individual files for each resource (jobs.py, cvs.py)
│   │   └── api_v1.py     # Gathers all endpoint routers
│   ├── schemas/          # Pydantic schemas for data validation
│   ├── services/         # Business logic (e.g., calling AI models)
│   └── main.py           # Main FastAPI app entry point
└── requirements.txt      # Python dependencies
```

### Frontend Structure

```
frontend/
├── public/               # Static assets
├── src/                  # Main application source code
│   ├── api/              # Functions for calling the backend (jobService.js)
│   ├── components/       # Reusable UI components
│   ├── pages/            # Top-level components for each view (DashboardPage.jsx)
│   ├── App.jsx           # Main component with routing logic
│   └── main.jsx          # Application entry point
├── package.json          # Project dependencies and scripts
└── vite.config.js        # Vite build configuration
```

---

## 🔮 Future Work (Deferred Features)

The current MVP provides the core foundation. Future development will focus on:

- Video interview analysis
- Chrome extension for sourcing candidates
- Advanced bias detection and mitigation tools
- Real-time job board scraping

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.



