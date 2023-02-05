import password
import smtplib


class Gmail:
    def __init__(self):
        """

        """
        self.__smtp_server = "smtp.gmail.com"
        self.__my_email = "testpythongp@gmail.com"


    def send_email(self, send_to, message_body):
        with smtplib.SMTP(self.__smtp_server) as connection:
            connection.starttls()
            connection.login(user = self.__my_email, password = password.gmail_password)
            connection.sendmail(self.__my_email, send_to, f"Subject:Flight Deal alert!\n\n{message_body}")


