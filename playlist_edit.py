"""
PURPOSE: To consolidate the .py files into one place.
"""

import os
from dotenv import load_dotenv
from Classes.Video import Video
import get_videos, add_videos, del_videos
# from Classes.Playlist import Playlist


# Gets specific .env variable.
def get_env(env_var):
    load_dotenv("Credentials/.env")
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
    # Credential Vars.
    api_key_public = get_env("API_KEY")
    api_key_private = "Credentials/client_secret_file.json"
    old_pl_id = get_env("OLD_PLAYLIST_ID")
    new_pl_id = get_env("NEW_PLAYLIST_ID")

    max_results = 3 # max is 50.
    
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

    get_vids_response = get_videos.api_request(api_key_public, old_pl_id, max_results)
    
    vid_list = extract(get_vids_response)
    length = len(vid_list)
    # print(f"\n\n{vid_list[0].title}\n\n")

    for i in range(length):
        # add_videos.api_request(api_key_private, new_pl_id, vid_list[i].vid_id)
        # del_videos.api_request(api_key_private, vid_list[i].pl_item_id)

        print(vid_list[i].title)



if __name__ == "__main__":
    main()