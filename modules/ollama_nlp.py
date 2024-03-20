import requests
import json


class OllamaNLP:

    def __init__(self, base_url='http://localhost:11434'):
        self.base_url = base_url

    def generate_text(self, model, prompt, stream=False, options=None):
        endpoint = f'{self.base_url}/api/generate'

        # prompt = "<s>[INST] <<SYS>>You are Jarvis, a helpful AI assistant from the iron man movie and you only respond with short answers, you refer to me as Sir. <</SYS>>"+prompt+"</s>",

        payload = {
            "model": model,
            "prompt": prompt,
            "options": options,
            "stream": stream,
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
