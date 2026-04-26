"""
PURPOSE: Removes videos from a playlist.
"""

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


from dotenv import load_dotenv



scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

# Gets specific .env variable.
def get_env(env_var):
    load_dotenv()
    return(os.getenv(env_var))


# Builds API request.
def api_request(api_key, pl_item_id):
    api_service_name = "youtube"
    api_version = "v3"
    # client_secrets_file = "client_secret_file.json"
    # playlist_item_id = get_env("TEST_PLAYLIST_ITEM_ID")

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        api_key, scopes)
    credentials = flow.run_local_server(port=0)
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.playlistItems().delete(
        id=pl_item_id
    )

    request.execute()
    
    #return request.execute()




def main():
    playlist_id = get_env("NEW_PLAYLIST_ID")
    vid_id = get_env("TEST_VIDEO")

    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

    response = api_request()

    print(response)

if __name__ == "__main__":
    main()