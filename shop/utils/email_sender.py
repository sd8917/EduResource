import requests
from digitatShop.settings import EMAIL_SERVICE_ENDPOINT,EMAIL_SENDER_EMAIL,EMAIL_SENDER_NAME,EMAIL_API_KEY
import json

def sendEmail(name,email,subject,htmlContent):

    payload = {
        "sender": {
            "name": EMAIL_SENDER_NAME,
            "email": EMAIL_SENDER_EMAIL
        },
        "to": [
            {
                "email": email,
                "name": name
            }
        ],
        "replyTo": {
            "email": EMAIL_SENDER_EMAIL,
            "name": EMAIL_SENDER_NAME
        },
        "htmlContent": htmlContent,
        "subject": subject
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "api-key": EMAIL_API_KEY
    }

    response = requests.request("POST", EMAIL_SERVICE_ENDPOINT, json=payload, headers=headers)

    return response
