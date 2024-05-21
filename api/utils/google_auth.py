import requests
import os
from dotenv import load_dotenv

from google.oauth2 import id_token
from google.auth.transport import requests as google_requests

load_dotenv()
GOOGLE_CLIENT_ID = str(os.getenv("GOOGLE_CLIENT_ID"))
GOOGLE_CLIENT_SECRET = str(os.getenv("GOOGLE_CLIENT_SECRET"))
GOOGLE_REDIRECT_URI = str(os.getenv("GOOGLE_REDIRECT_URI"))
GOOGLE_TOKEN_URI = str(os.getenv("GOOGLE_TOKEN_URI"))


def code_token_exchange(code):
    token_uri = GOOGLE_TOKEN_URI
    redirect_uri = GOOGLE_REDIRECT_URI
    client_id = GOOGLE_CLIENT_ID
    client_secret = GOOGLE_CLIENT_SECRET

    data = {
        "code": code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code",
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    # print(data)
    response = requests.post(token_uri, data=data, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        return response_data
    else:
        error_message = f"Error during code_token_exchange: {response.status_code} - {response.text}"  # print(error_message)
        return {"error": error_message}


def verify_id_token(token):
    try:
        idinfo = id_token.verify_oauth2_token(
            token, google_requests.Request(), GOOGLE_CLIENT_ID, clock_skew_in_seconds=10
        )

        if "accounts.google.com" not in idinfo["iss"]:
            raise ValueError("The token is either invalid or has expired")

        # print("idinfo: ", idinfo)
        idinfo_res = {
            "email": idinfo["email"],
            "id": idinfo["sub"],
            "name": idinfo["name"],
        }
        return idinfo_res
        # userid = idinfo["sub"]
    except ValueError as e:
        error_message = f"Error during token verification: {str(e)}"
        print(error_message)
        return {"error": error_message}
