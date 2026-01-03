# Multi-Agent Code Analysis & Documentation System

This project is a backend system that analyzes a software codebase
and prepares structured documentation for developers and product teams.

## What this project does
- User can sign up and log in
- User can upload a codebase (ZIP file)
- User can create a project
- System starts analysis process
- APIs are documented using Swagger

## Technology Used
- Python
- FastAPI
- SQLite
- Git & GitHub

## How to run this project

Step 1: Clone the project
git clone https://github.com/YOUR_USERNAME/multi-agent-code-docs.git

Step 2: Go into project folder
cd multi-agent-code-docs

Step 3: Create virtual environment
python -m venv venv

Step 4: Activate virtual environment
Windows:
venv\Scripts\activate

Step 5: Install dependencies
cd backend
pip install -r requirements.txt

Step 6: Run the server
uvicorn app.main:app --reload

Step 7: Open browser
http://127.0.0.1:8000/docs

## Current Status
Week 1 completed:
- Authentication
- Project creation
- File validation
- Swagger API docs

## Future Plan
- Multi-agent AI system
- Streamlit UI
- Code analysis agents
- Automatic documentation generation
