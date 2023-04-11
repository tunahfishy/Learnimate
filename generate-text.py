import requests
import json
import os

# TODO add api_key
API_KEY = os.environ["API_KEY"] 
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"


# TODO replace model 
def generate_chat_completion(messages, model="gpt-3.5-turbo", temperature=1, max_tokens=None):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    data = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }

    if max_tokens is not None:
        data["max_tokens"] = max_tokens

    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")
    

# TODO add messages
messages = [
    {"role": "system", "content": ""},
    {"role": "user", "content": f'' }
]

response_text = generate_chat_completion(messages)
print(response_text)