import requests
import datetime
import os

# NUTRITIONIX
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]


GENDER = "male"
WEIGHT_KG = "75.0"
HEIGHT_CM = "188"
AGE = "21"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)



#SHEETY
BEARER_TOKEN = os.environ["BEARER_TOKEN"]

sheety_add_endpoint = "https://api.sheety.co/6f23aa564c9170d6a5f96443617f22e0/exercicio/workouts"

params = {
  "workout": {
    "name": "Felipe Teixeira Baldim",
    "email": "felipe.baldim@sou.unifal-mg.edu.br"
  }
}


today_date = datetime.datetime.now().strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    bearer = {"Authorization": f"Bearer {BEARER_TOKEN}"}

    sheet_response = requests.post(sheety_add_endpoint, json=sheet_inputs, headers=bearer)

    print(sheet_response.text)



