# Workout-Tracker

Workout-Tracker is a Python Module to track workout or habits using natural english language

# Sample Usage

```bash
from Nutritionix import Nutriotionix
from datetime import datetime
import os

# Initialize Constant
API_KEY = os.environ.get("API_KEY")
APP_ID = os.environ.get("APP_ID")
SECRET = os.environ.get("SECRET")
Today = datetime.now()


data = Nutriotionix(app_id=APP_ID, api_key=API_KEY)
requested_data = data.request_data(input("Tell me what exercise you did?"))
data_json = requested_data["exercises"]

for item in data_json:
    # print(item)
    workouts = {
        "workout": {
            "date": Today.strftime("%d/%m/%Y"),
            "time": Today.time().strftime("%H:%M:%S"),
            "exercise": item["user_input"],
            "duration": item["duration_min"],
            "calories": item["nf_calories"],
            "id": "0",
        }
    }
    post_resp = data.post_data_sheet(workouts, secret=SECRET)
    print(post_resp)

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
