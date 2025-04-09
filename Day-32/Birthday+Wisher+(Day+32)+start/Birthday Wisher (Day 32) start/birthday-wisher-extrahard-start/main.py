##################### Extra Hard Starting Project ######################
import datetime
import pandas
import smtplib
import random

email = "tbfelipe067@gmail.com"
password = "msda rhyl zccc sxze"
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

now = datetime.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row.month, data_row.day):data_row
                 for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    letter_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    birth_person = birthday_dict[today]
    with open(letter_path) as letter_file:
        content = letter_file.read()
        new_content = content.replace("[NAME]", birth_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs=birth_person.email,
                            msg=f"Subject: Happy Birthday!!!\n\n{new_content}")







# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




