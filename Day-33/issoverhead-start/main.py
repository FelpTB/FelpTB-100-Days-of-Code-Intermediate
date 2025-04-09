import requests
from datetime import datetime
import smtplib
import time

email = "tbfelipe067@gmail.com"
password = "msda rhyl zccc sxze"

MY_LAT = -21.4294
MY_LONG = -45.9471

def estaproximo():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_latitude <= MY_LONG+5:
        return True



def estadenoite():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now <= sunrise or time_now >= sunset:
        return True

while True:
    time.sleep(60)
    if estaproximo() and estadenoite():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(email,password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg="Subject:Look Up\n\nThe ISS is above you in the sky."
        )




