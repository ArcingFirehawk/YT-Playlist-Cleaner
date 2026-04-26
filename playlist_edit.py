"""
PURPOSE: To consolidate the .py files into one place.
"""

import os
from dotenv import load_dotenv
from Classes.Video import Video
import get_videos, add_videos, del_videos
from Classes.Playlist import Playlist



# Gets specific .env variable.
def get_env(env_var):
    load_dotenv()
    return(os.getenv(env_var))


# Extracts the API's output into the Video class.
def extract(api_response):
    vid_list = []
    length = api_response["pageInfo"]["resultsPerPage"]


    for i in range(length):
        vid_status = api_response["items"][i]["status"]["privacyStatus"]

        if vid_status == "public":
            vid_title = api_response["items"][i]["snippet"]["title"]
            vid_id = api_response["items"][i]["contentDetails"]["videoId"]
            vid_creator = api_response["items"][i]["snippet"]["videoOwnerChannelTitle"]
            pl_item_id = api_response["items"][i]["id"]

            vid_list.append(Video(vid_title, vid_id, vid_creator, pl_item_id))
    
    return vid_list


def main():
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

    extract(get_vids_response)


if __name__ == "__main__":
    main()