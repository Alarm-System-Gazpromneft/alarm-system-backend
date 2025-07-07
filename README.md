# Alarm System Backend

This is the backend service for the Alarm System project. It provides RESTful APIs for managing alarms, users, and notifications.

## Features

- User authentication and authorization
- Alarm creation, update, and deletion
- Notification handling
- API endpoints for frontend integration

## Requirements

- Python 3.10+
- FastAPI
- PostgreSQL

## Setup

1. Clone the repository.
2. Install dependencies:  
    `pip install -r requirements.txt`
3. Configure environment variables.
4. Run the server:  
    `uvicorn app.main:app --reload`