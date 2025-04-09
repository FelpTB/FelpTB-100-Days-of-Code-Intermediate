import requests
import datetime

MY_LAT = -21.4294
MY_LONG = -45.9471

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
#
# data = response.json()
# print(data)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0

}

request_sunset = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
request_sunset.raise_for_status()
data = request_sunset.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise)
print(sunrise.split("T")[1].split(":")[0])
print(sunset)

time_now = datetime.datetime.now()

print(time_now.hour)