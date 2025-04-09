import requests
from twilio.rest import Client

api_key = "272644717fdcd30cb5fc44345c9467d6"
endpoint = "https://api.openweathermap.org/data/2.5/forecast"
LAT = -21.428460
LON = -45.947010
number = +13342343047
acc_sid = "AC32518db309c306c0e759b077ed21b260"
auth_token = "215bffa98077738a6bc07d66edcd794d"

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": api_key
}

data = requests.get(endpoint, params=parameters).json()
# print(data["list"][0]["weather"][0]["id"])
will_rain = False
for hour_data in data["list"]:
    code = hour_data["weather"][0]["id"]
    if int(code) < 700:
        will_rain = True
if will_rain:
    client = Client(acc_sid, auth_token)
    message = client.messages.create(body="Vai chover hj meu chapa",
                                     from_="+13342343047",
                                     to="+5535999195960")
    print(message.status)




