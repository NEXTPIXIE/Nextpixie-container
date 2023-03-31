import requests
import os

key = os.getenv("email_key")

def signup_mail(email):
 
    plunk = requests.post(
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

    print(plunk)