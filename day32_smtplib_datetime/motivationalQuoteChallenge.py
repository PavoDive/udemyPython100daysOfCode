import smtplib
import datetime
from random import choice
from password import gmail_password
# There is a file password.py in the same folder and it only contains
# the following line:
# gmail_password = "the-16-digit-password-given-by-google"
# this was done to avoid commiting the password to github

# ------------ read the quotes -----------
with open("quotes.txt") as file1:
    quotes = file1.readlines()


# ------------ email sender function -----
def send_email():
    today_quote = choice(quotes)

    my_email = "testpythongp@gmail.com"
    my_password = gmail_password

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email, password = my_password)
        connection.sendmail(my_email, "testpythongp@outlook.com", f"Subject:Cheer up, it's Monday!\n\n{today_quote}")
        print("Email sent successfully!")


# ---------- check if today is monday ----------
now = datetime.datetime.now()
if now.isoweekday() == 1:
    send_email()
