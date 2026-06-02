# API Automation Testing Project with FastAPI & Pytest

## Overview

This project demonstrates a professional API automation testing framework built around a custom backend API developed using FastAPI and SQLAlchemy.

Instead of testing a public dummy API, a dedicated backend system was created to simulate an enterprise-style environment where:

- Authentication and Authorization are implemented (JWT tokens)
- Users can only access their own resources
- User management APIs are protected
- Database persistence is used
- Real-world API security and behavior can be validated

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
├── test_authentication_authorization.py
└── conftest.py

---

## Why Build a Custom Backend?

In enterprise environments, QA engineers often test internal APIs rather than public mock services.

This project replicates that reality by:

- Creating controlled API endpoints
- Implementing authentication flows
- Enforcing authorization rules
- Storing real data in a database
- Allowing full backend behavior validation

This enables:

- Secure API flows
- Reliable test automation
- Database-level verification
- Negative testing
- Schema validation
- Real-world workflow testing

---

## Features Implemented

- User registration API
- Login API with JWT token generation
- Secure password hashing (bcrypt)
- Protected endpoints using authentication middleware
- Authorization (user can only access their own data)
- Database persistence validation
- Duplicate user handling
- Error handling & negative scenarios
- JSON schema validation
- End-to-end API + DB verification

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
- Fetch user by ID )protected endpoint)

### Authentication Tests
- Valid login returns JWT token
- Invalid login returns 401 Unauthorized

### Authorization Tests
- User can access only their own data
- Accessing other users returns 403 Forbidden
- Invalid user IDs return 404 Not Found

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
- Implementing authorization (access control rules)
- Building enterprise-style API workflows
- Automating REST API testing
- Validating backend + database together
- Handling authentication flows
- Writing scalable Pytest frameworks
- Implementing schema validation

---

## Project Goal

To simulate a real enterprise backend environment and apply professional API automation testing practices - similar to what QA Automation Engineers and SDETs perform in production systems, including authentication, authorization, and database validation workflows.

