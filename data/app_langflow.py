import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Your Langflow Flow ID and API key
FLOW_ID = "5c458317-be67-44c8-b306-9ac5c9c08f91"
API_KEY = os.getenv("LANGFLOW_API_KEY")  # ⚠️ paste your real API key here
print('API KEY VALUE:', API_KEY)
# Langflow local URL
URL = f"http://127.0.0.1:7860/api/v1/run/{FLOW_ID}?stream=false"

# Headers with API key
headers = {
    "Content-Type": "application/json",
    "x-api-key": API_KEY
}

# Since your input field is labeled "Text", the key is 'text'
data = {
        "input_value": "Hello Langflow from Python!"
    }

# Send the request
response = requests.post(URL, headers=headers, json=data)
print('response request body:', response.request.body)
# Print the output
if response.status_code == 200:
    print("✅ Response:")
    print(response.json()['outputs'])
else:
    print("❌ Error:", response.status_code)
    print(response.text)
