Sure! Below is a sample README file for the provided APIs:

# Flask User API

This repository contains a Flask-based RESTful API for user management. The API allows users to register, login, update their information, get their details, and delete their account. It is secured using JWT (JSON Web Tokens) for user authentication.

## Getting Started

These instructions will guide you on how to set up and run the API on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or higher
- MongoDB (running locally or using MongoDB Atlas)

### Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/Rajkumar-B-55/Flask_Mongo
cd Flask_Mongo
```

2. Create and activate a virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Set up environment variables:

   Create a `.env` file in the project root and add the following configurations:

```plaintext
ENVIRONMENT=DEV
DB_NAME =----dbname---
DB_PASSWORD =----@@##!!---
DB_USERNAME = ---username---
DB_HOST = ----localhost---
DB_PORT = 0000
DB_COLLECTION =---collection__
JWT_SECRET_KEY=---secret__key
```

### Usage

1. Run the Flask application:

```bash
python3 main_server.py
```

The API will be available at `http://127.0.0.1:5000/api/v1/`.

2. API Endpoints:

   - `POST /api/v1/register`: Register a new user.

   - `POST /api/v1/login`: Authenticate and get an access token for a registered user.

   - `PUT /api/v1/update`: Update user information. Requires authentication.

   - `GET /api/v1/get`: Get user details. Requires authentication.

   - `DELETE /api/v1/delete`: Delete user account. Requires authentication.

   **Note**: For protected endpoints (`update`, `get`, `delete`), you need to include the `Authorization` header in your request with a valid JWT token. Obtain the token by successfully logging in with a registered user.

