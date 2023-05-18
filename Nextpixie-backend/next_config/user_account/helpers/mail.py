import requests
import os

key = "sk_c6c183d79ed546b5ec82d3d29e7369dd33fcbbbecf638313"

def signup_mail(email):
 
    requests.post(
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


def send_otp_mail(email, otp_code):

    requests.post(
        "https://api.useplunk.com/v1/track",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {key}"
        },
        json={
            "event": "otp_mail",
            "email": email,
            "data": {
                "otp": otp_code
            }
        },
    )