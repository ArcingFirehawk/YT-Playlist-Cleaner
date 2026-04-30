"""
PURPOSE: Handles the refresh token.

ORIGINAL AUTHOR: Linda Lawton - DaImTo
ORIGINAL SOURCE: https://stackoverflow.com/a/73376365
EDITED BY: Anthony Choi
"""

import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import google_auth_oauthlib.flow
import google.auth.exceptions
import json



scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
token_file = "Credentials/token.json"


# Checks if a refresh token already exists.
def check_token():
    credentials = None


    # if statement that checks if the token already exists and works.
    if os.path.exists(token_file):
        try:
            credentials = Credentials.from_authorized_user_file(token_file, scopes)
            credentials.refresh(Request())
        except google.auth.exceptions.RefreshError as error:
            credentials = None
            print(f"\n\nRefresh token expired, requesting authorization again. \nError: {error}.")

    # if statement to get a new token if it doesn't exist or is invalid.
    if not credentials or credentials.token_state == "INVALID":
        credentials = get_token()

    # return credentials


# Gets a new refresh token.
def get_token():
    api_key_private = "Credentials/client_secret_file.json"

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(api_key_private, scopes)
    credentials = flow.run_local_server(port=0)

    with open(token_file, "w") as f:
        f.write(credentials.to_json())
    
    return credentials


# Loads the existing token.
def load_token():
    check_token()

    with open(token_file, "r") as f:
        credentials = json.load(f)
        f.close()

    return credentials


def main():
    credentials = None
    api_key_private = "Credentials/client_secret_file.json"


    # if statement that checks if the token already exists and works.
    if os.path.exists(token_file):
        try:
            credentials = Credentials.from_authorized_user_file(token_file, scopes)
            credentials.refresh(Request())
        except google.auth.exceptions.RefreshError as error:
            credentials = None
            print(f"\n\nRefresh token expired, requesting authorization again. \nError: {error}.")

    # if statement to get a new token if it doesn't exist or is invalid.
    if not credentials or credentials.token_state == "INVALID":
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(api_key_private, scopes)
        credentials = flow.run_local_server(port=0)

    with open(token_file, "w") as f:
        f.write(credentials.to_json())

    return credentials
    


if __name__ == '__main__':
    main()