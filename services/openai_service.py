import requests

ENDPOINT = "YOUR_ENDPOINT"
API_KEY = "YOUR_API_KEY"

def send_request_to_gpt(prompt):
    # Configuration
    headers = {
        "Content-Type": "application/json",
        "api-key": API_KEY,
    }
    # Payload for the request
    payload = {
        "messages": [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "You are an AI assistant that helps people find information."
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            },
            {
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": "Hello! How can I assist you today?"
                    }
                ]
            }
        ],
        "temperature": 0.7,
        "top_p": 0.95,
        "max_tokens": 800
    }
    # Send request
    try:
        response = requests.post(ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.RequestException as e:
        print(e)
        raise SystemExit(f"Failed to make the request. Error: {e}")
    return response
