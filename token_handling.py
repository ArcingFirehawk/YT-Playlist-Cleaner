"""
PURPOSE: Handles the refresh token.

ORIGINAL AUTHOR: Linda Lawton - DaImTo
ORIGINAL SOURCE: https://stackoverflow.com/a/73376365
EDITED BY: Anthony Choi
"""

import os
from google.oauth2.credentials import Credentials
from  google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError

from common_funcs import get_env
import get_videos



SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
TOKEN_FILE = "Credentials/token.json"


# Checks if refresh token already exists and valid.
def check_token():
    credentials = None


    # if statement that checks if the token already exists and works.
    if os.path.exists(TOKEN_FILE):        
        try:
            credentials = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
            pl_id = get_env("NEW_PLAYLIST_ID")

            get_videos.api_request(credentials, pl_id)
            # credentials.refresh(Request())    # This doesn't work.

        # except google.auth.exceptions.RefreshError as e:
        except HttpError as e:
            print(f"\n\nRefresh token expired, requesting authorization again. ERROR: {e}.")
            credentials = None

        # if statement to get a new token if it doesn't exist or is invalid.
    if not credentials or credentials.token_state == "INVALID":
        credentials = get_token()

    return credentials


# Gets new refresh token.
def get_token():
    api_key_private = "Credentials/client_secret_file.json"

    flow = InstalledAppFlow.from_client_secrets_file(api_key_private, SCOPES)
    credentials = flow.run_local_server(port=0)

    with open(TOKEN_FILE, "w") as f:
        f.write(credentials.to_json())
    
    return credentials


def main():
    check_token()


if __name__ == '__main__':
    main()