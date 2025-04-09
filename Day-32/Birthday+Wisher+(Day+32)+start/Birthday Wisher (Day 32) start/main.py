import smtplib

email = "tbfelipe067@gmail.com"
password = "msda rhyl zccc sxze"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs="tbfelipe266@gmail.com",
                        msg="Subject:Hello\n\nThis is the body of my e-mail")
