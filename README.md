# Wizards-Outh Django

A powerful authentication API using Django, similar to Clerk.com.

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

For more detailed documentation, please refer to the official documentation or the project's GitHub repository.
