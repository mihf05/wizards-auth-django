# Wizards-Outh Django

Wizards-Outh Django is a powerful authentication API built with Django, offering features similar to Clerk.com for seamless user management and authentication.

## Features
- User registration and login
- API key management
- Passwordless authentication
- Multi-factor authentication
- Social login with Google and Facebook

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Steps

1. **Create a Virtual Environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Install the Package**
   To install the package, use the following command:
   ```bash
   pip install wizards-outh-django
   ```

3. **Configure Django Settings**:
   - Add `'users'` to your `INSTALLED_APPS` in `settings.py`.
   - Configure your database settings in `settings.py`.
   - Set up email backend for passwordless authentication.

4. **Apply Migrations**:
   Run the following command to apply migrations:
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:
   Start the Django development server using:
   ```bash
   python manage.py runserver
   ```

6. **Access the API**:
   Open your browser and go to `http://localhost:8000` to access the API.

## Usage Examples

### Register a New User
To register a new user, send a POST request to `/api/register/` with the following JSON payload:
```json
{
  "username": "newuser",
  "password": "password123"
}
```

### Login
To log in, send a POST request to `/api/login/` with the following JSON payload:
```json
{
  "username": "newuser",
  "password": "password123"
}
```

### Generate API Key
To generate a new API key, send a POST request to `/api/api-key/generate/` with an authenticated user.

## API Endpoints

- `POST /api/register/`: Register a new user
- `POST /api/login/`: Log in a user
- `GET /api/protected/`: Access a protected route (requires authentication)
- `POST /api/api-key/generate/`: Generate a new API key (requires authentication)
- `GET /api/api-key/list/`: List all active API keys (requires authentication)
- `POST /api/api-key/deactivate/`: Deactivate an API key (requires authentication)

For more detailed documentation, please refer to the project's GitHub repository.
