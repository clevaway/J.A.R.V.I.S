import requests
import json
import base64


class Vision:

    def __init__(self, base_url='http://localhost:11434'):
        self.base_url = base_url

    def generate_description(self, model, image_path, prompt="You are a helpful AI assistant and you only respond with short answers, you refer to me as Sir. and you responses always start with 'I see...' Now, tell me, What do you see in this picture?", stream=False):
        endpoint = f'{self.base_url}/api/generate'

        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(
                image_file.read()).decode('utf-8')

        payload = {
            "model": model,
            "prompt": prompt,
            "stream": stream,
            "images": [encoded_string]
        }

        headers = {'Content-Type': 'application/json'}

        response = requests.post(
            endpoint, data=json.dumps(payload), headers=headers)

        if response.status_code == 200:
            response_json = json.loads(response.text)
            if 'response' in response_json:
                return response_json['response']
            else:
                return {"error": "Response field not found in the API response."}
        else:
            return {"error": f"Error {response.status_code}: {response.text}"}
