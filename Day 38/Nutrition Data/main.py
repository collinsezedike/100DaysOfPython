import requests
from datetime import datetime
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/4f19d4f3096bb433d01a8f806c80f6db/workoutTracking(100DaysOfPython)/workouts"

exercise = input("Tell me what exercise you did: ").lower()
header_params = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
body_params = {"query": exercise}
response = requests.post(url=NUTRITIONIX_ENDPOINT, json=body_params, headers=header_params)
data = response.json()["exercises"]


today = datetime.now().strftime("%d/%m/%Y")
this_time = datetime.now().strftime("%H:%M:%S")

sheety_header = {"Authorization": os.environ.get("SHEETY_BEARER_TOKEN")}
for exercise_data in data:
    sheet_params = {
        "workout": {
            "date": today,
            "time": this_time,
            "exercise": exercise_data["name"].title(),
            "duration": exercise_data["duration_min"],
            "calories": exercise_data["nf_calories"]
        }
    }
    response = requests.post(url=SHEETY_ENDPOINT, json=sheet_params, headers=sheety_header)
    print(response.text)

