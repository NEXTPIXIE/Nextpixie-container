import requests
import os

key = os.getenv("email_key")

def signup_mail(email):
 
    mail = requests.post(
        "https://api.useplunk.com/v1/track",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {key}" 
        },
        json={
            "event": "user-signup",
            "email": email
        }
        
    )

    return mail


def send_otp_mail(first_name, email, otp):

    mail = requests.post(
        "https://api.useplunk.com/v1/track",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {key}"
        },
        json={
            "event": "otp_mail",
            "email": email,
            "data": {
                "otp": otp,
                "first_name": first_name
            }
        },
    )

    return mail