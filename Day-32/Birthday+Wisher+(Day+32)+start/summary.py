# import smtplib
#
# email = "tbfelipe067@gmail.com"
# password = "msda rhyl zccc sxze"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=email, password=password)
#     connection.sendmail(from_addr=email, to_addrs="tbfelipe266@gmail.com",
#                         msg="Subject:Hello\n\nThis is the body of my e-mail")

import datetime
now = datetime.datetime.now()
year = now.year
month = now.month
weekday = now.weekday()

birthday= datetime.datetime(year=2003, day=21, month=5)