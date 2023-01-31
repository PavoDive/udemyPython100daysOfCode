from random import choice
import smtplib
import datetime
import pandas
from password import gmail_password
# There is a file password.py in the same folder and it only contains
# the following line:
# gmail_password = "the-16-digit-password-given-by-google"
# this was done to avoid commiting the password to github


# ---------- function to send emails ----------
my_email = "testpythongp@gmail.com"

def send_email(email, subject, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email, password = gmail_password)
        connection.sendmail(my_email, email, f"Subject:{subject}\n\n{message}")


birthday_table = pandas.read_csv("birthdays.csv")
birthday_list = birthday_table.to_dict(orient = "records")

messages = ["letter_templates/letter_" + str(i) +".txt" for i in range(1, 4)]
subjects = ["Today is the day!", "Today we celebrate you", "Happy BD!"]
now = datetime.datetime.now()

for person in birthday_list:
    if person["day"] == now.day and person["month"] == now.month:
        name = person["name"]
        email = person["email"]
        letter_file = choice(messages)
        with open(letter_file) as file1:
            letter_text = file1.read()
            letter_text = letter_text.replace("[NAME]", name)

        letter_subject = choice(subjects)
        send_email(email, letter_subject, letter_text)
        print("Email sent successfully")

