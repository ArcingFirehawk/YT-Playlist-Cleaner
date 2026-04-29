"""
PURPOSE: Removes videos from a playlist.
"""

import google_auth_oauthlib.flow
import googleapiclient.discovery
import os
from common_funcs import get_env


scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


# Builds API request.
def api_request(api_key, pl_item_id):
    api_service_name = "youtube"
    api_version = "v3"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(api_key, scopes)
    credentials = flow.run_local_server(port=0)
    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

    request = youtube.playlistItems().delete(
        id=pl_item_id
    )
    
    request.execute()



def main():
    api_key_private = "Credentials/client_secret_file.json"
    pl_item_id = get_env("TEST_PLAYLIST_ITEM_ID")

    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

    api_request(api_key_private, pl_item_id)


if __name__ == "__main__":
    main()