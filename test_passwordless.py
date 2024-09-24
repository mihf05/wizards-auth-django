import requests
import json

# Define the API endpoint
url = 'http://localhost:8000/api/passwordless/send-token/'

# Define the payload (email of the test user)
payload = {
    'email': 'testuser4@example.com'
}

# Convert payload to JSON
json_payload = json.dumps(payload)

# Set the headers
headers = {
    'Content-Type': 'application/json'
}

try:
    # Send POST request
    response = requests.post(url, data=json_payload, headers=headers)

    # Check the response
    if response.status_code == 200:
        print("Login token sent successfully.")
        print("Response:", response.json())
    else:
        print("Failed to send login token.")
        print("Status code:", response.status_code)
        print("Response:", response.text)

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)

# Note: This script assumes that the Django server is running on localhost:8000
# Make sure to run the Django server before executing this script
