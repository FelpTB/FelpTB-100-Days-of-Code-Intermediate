import datetime
import smtplib
import random

email = "tbfelipe067@gmail.com"
password = "msda rhyl zccc sxze"

now = datetime.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs="tbfelipe266@gmail.com",
                            msg="Subject:HAPPY MONDAY!!!\n\n"+quote)