import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variable
api_key = os.getenv('GROQ_API_KEY')

# Define the API endpoint
url = "https://api.groq.com/v1/models/llama-3.2-90b-vision-preview/completions"

# Define the request payload
payload = {
    "messages": [{"role": "user", "content": "Say hello"}]
}

# Define the headers
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Make the API request
response = requests.post(url, json=payload, headers=headers)

# Print the response
print(response.json())