"""
PURPOSE: To consolidate the .py files into one place.
"""

import os
from dotenv import load_dotenv
import get_videos, add_videos, del_videos
import Classes.Playlist as Playlist, Classes.Video as Video


# Gets specific .env variable.
def get_env(env_var):
    load_dotenv()
    return(os.getenv(env_var))


# Extracts the API's output into the Video class.
def extract(input):
    pass

    i = 0   # Counter
    vidList = []    # List to contain video obj.
    vidTuple = () # Tuple to contain playlist item IDs and video IDs.
    max = input["pageInfo"]["resultsPerPage"]   # The # of results from the API request.

    for i in range(max):
        vidStatus = input["items"][i]["status"]["privacyStatus"]

        if vidStatus == "public":
            vidList.append(Video())

    while i < max:
        vidStatus = input["items"][i]["status"]["privacyStatus"]

        if vidStatus == "public":
            vid
            playlistItemId = input["items"][i]["id"]
            vidId = input["items"][i]["contentDetails"]["videoId"]

            vidTuple = (playlistItemId, vidId)
            vidList.append(vidTuple)
        
        i += 1

    return vidList


# YT Vars.
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"
num_results = 1 # max is 50.

# Credential Vars.
api_key = get_env("API_KEY")
client_secrets_file = "client_secret_file.json"
#playlist_item_id = get_env("TEST_PLAYLIST_ITEM_ID")
old_pl_id = get_env("OLD_PLAYLIST_ID")
new_pl_id = get_env("NEW_PLAYLIST_ID")


os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

get_vids_response = get_videos.api_request(API_SERVICE_NAME, API_VERSION, api_key, old_pl_id, num_results)