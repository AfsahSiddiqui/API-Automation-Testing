# API Automation Testing Project with FastAPI & Pytest

## Overview

This project demonstrates a professional API automation testing framework built around a custom backend API developed using FastAPI and SQLAlchemy.

Instead of testing a public dummy API, a dedicated backend system was created to simulate an enterprise-style environment where:

- Authentication logic exists
- User management is implemented
- Database persistence is involved
- Real-world API behaviors can be validated

This approach provides full control over backend workflows, allowing deeper API testing similar to what is done in real production systems.

The primary goal of this project is:

👉 To perform end-to-end API automation testing on a realistic backend system.

---

## Tech Stack

### Backend (Test System)

- FastAPI
- SQLAlchemy ORM
- SQLite Database
- JWT Token generation
- Password hashing with bcrypt

### Automation & Validation

- Python
- Pytest
- Requests library
- Faker for dynamic test data
- JSON Schema validation
- HTML Reports and Logging for test execution tracking

---

## Python Version

Python 3.10+
(Recommended: Python 3.10 or 3.11 for best compatibility)

---

## Project Architecture

app/
├── auth.py # Authentication & token handling
├── database.py # Database connection & ORM base
├── models.py # SQLAlchemy models
├── schemas.py # Pydantic request/response schemas
└── main.py # FastAPI routes

tests/
├── test_negative_scenarios.py
├── test_schema_validation.py
├── test_user_creation_db_validation.py
└── conftest.py

---

## Why Build a Custom Backend?

In enterprise environments, QA engineers often test internal APIs rather than public mock services.

This project replicates that reality by:

- Creating controlled API endpoints
- Implementing authentication flows
- Storing real data in a database
- Allowing full backend behavior validation

This enables:

- Reliable test automation
- Database-level verification
- Negative testing
- Schema validation
- Real-world workflow testing

---

## Features Implemented

- User creation API
- Secure password hashing
- Login authentication with token generation
- Database persistence validation
- Duplicate user handling
- Error handling & negative scenarios
- API response schema validation
- End-to-end backend verification

---

## Installation

### 1️⃣ Clone the repository

git clone git@github.com:AfsahSiddiqui/API-Automation-Testing.git
cd API-Automation-Testing

---

### 2️⃣ Create virtual environment (recommended)

python -m venv .venv

#### Activate

**Windows:** .venv\Scripts\activate
**Mac/Linux:** source .venv/bin/activate

---

### 3️⃣ Install dependencies

pip install -r requirements.txt

---

## Running the Project

### Start Backend Server

uvicorn app.main:app --reload

Backend will run at:

http://127.0.0.1:8000

---

### Run API Automation Tests

pytest --html=report.html --self-contained-html

---

## Automated Test Coverage

### API Functional Tests

- Create user
- Login user
- Fetch user by ID

### Negative Scenarios

- Login with unregistered email
- Login with invalid password
- Duplicate user creation
- Fetching nonexistent users

### Schema Validation

- Validates API responses using JSON Schema

### Database Validation

- Confirms API actions persist correctly in the database
- Verifies password hashing

---

## Key Learning Outcomes

- Designing testable backend systems
- Building enterprise-style API workflows
- Automating REST API testing
- Validating backend + database together
- Handling authentication flows
- Writing scalable Pytest frameworks
- Implementing schema validation

---

## Project Goal

To simulate a real enterprise backend environment and apply professional API automation testing practices - similar to what QA Automation Engineers and SDETs perform in production systems.

