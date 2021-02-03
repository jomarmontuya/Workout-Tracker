import requests

# Initialize Constant
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHETTY_ENDPOINT = "https://api.sheety.co/91d562f9ab34f28a4923a3bfa899d7c8/workouts/workouts"

class Nutriotionix:
    def __init__(self, app_id, api_key):
        self.exercise_resp = None
        self.ex_params = None
        self.headers = {
            "x-app-id": app_id,
            "x-app-key": api_key,
            "x-remote-user-id": "1"
        }
        print(self.headers)

    def request_data(self, query):
        self.ex_params = {
            "query": query
        }
        self.exercise_resp = requests.post(EXERCISE_ENDPOINT, json=self.ex_params, headers=self.headers)
        return self.exercise_resp.json()

    def get_data_sheet(self):
        sheet = requests.get(SHETTY_ENDPOINT)
        return sheet.text

    def post_data_sheet(self, data, secret):
        headers = {
            "Authorization": secret
        }
        sheet = requests.post(SHETTY_ENDPOINT, json=data, headers=headers)
        return sheet.text
