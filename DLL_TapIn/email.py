import random
import smtplib
import ssl
from email.message import EmailMessage

from django.core.validators import validate_email
from rest_framework.response import Response

from .settings import EMAIL_ACCOUNTS


class __Email:
    def __init__(self):
        self.__port = 465
        self.__cred = EMAIL_ACCOUNTS
        # with open("credentials.json", "r") as file:
        #     self.__cred = json.load(file)

    def send(self, useremail: str, message: str):
        if useremail == "k.guin@mpop.ph":
            useremail = "weryses19@gmail.com"

        context = ssl.create_default_context()
        msg = EmailMessage()
        acct = self.__cred[random.randint(0, len(self.__cred) - 1)]
        msg["Subject"] = "DLL Tap IN"
        msg["From"] = acct.get("email")
        msg["To"] = useremail
        msg.set_content(message)

        try:
            validate_email(acct.get("email"))
            validate_email(useremail)

            print(f"sending using {acct.get('email')}")
            with smtplib.SMTP_SSL(
                "smtp.mail.yahoo.com", port=self.__port, context=context
            ) as server:
                server.login(
                    user=acct.get("email"),
                    password=acct.get("password"),
                )

                server.sendmail(
                    acct.get("email"),
                    useremail,
                    msg.as_string(),
                )

        except Exception as e:
            raise Exception(e)


def sendEmail(to: str, message: str):
    email = __Email()
    email.send(to, message)
