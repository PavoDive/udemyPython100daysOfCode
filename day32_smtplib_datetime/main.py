import smtplib
from password import gmail_password

my_email = "testpythongp@gmail.com"
my_password = gmail_password

# This is the canonical form:
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user = my_email, password = my_password)

# connection.sendmail(my_email, "testpythongp@outlook.com", "Subject:Hello\n\nThis is the body of the message.")
# connection.close()

# But this is the standard form, to avoid the final close method:
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user = my_email, password = my_password)

    connection.sendmail(my_email, "testpythongp@outlook.com", "Subject:Hello\n\nThis is the body of the message.")

