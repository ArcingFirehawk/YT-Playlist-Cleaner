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


# Extracts the API's output into the Video class format.
def extract(api_response):
    good_vid_list = []  # List containing public videos.
    bad_vid_list = []   # List containing unavailable videos.
    length = api_response["pageInfo"]["resultsPerPage"]


    for i in range(length):
        vid_status = api_response["items"][i]["status"]["privacyStatus"]

        if vid_status == "public":
            vid_title = api_response["items"][i]["snippet"]["title"]
            vid_id = api_response["items"][i]["contentDetails"]["videoId"]
            vid_creator = api_response["items"][i]["snippet"]["videoOwnerChannelTitle"]
            pl_item_id = api_response["items"][i]["id"]

            good_vid_list.append(Video(vid_title, vid_id, vid_creator, pl_item_id))
        else:
            vid_title = f"Unavailable{i + 1:02d}"
            vid_id = api_response["items"][i]["contentDetails"]["videoId"]
            vid_creator = "N/A"
            pl_item_id = api_response["items"][i]["id"]

            bad_vid_list.append(Video(vid_title, vid_id, vid_creator, pl_item_id))

    
    return good_vid_list, bad_vid_list


def main():
    api_key_public = get_env("API_KEY")
    api_key_private = "Credentials/client_secret_file.json"
    old_pl_id = get_env("OLD_PLAYLIST_ID")
    new_pl_id = get_env("NEW_PLAYLIST_ID")
    max_results = 3 # Max is 50.
    

    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

    get_vids_response = get_videos.api_request(api_key_public, old_pl_id, max_results)
    
    good_vid_list, bad_vid_list = extract(get_vids_response)
    good_length = len(good_vid_list)
    bad_length = len(bad_vid_list)
    # print(f"\n\n{vid_list[0].title}\n\n")

    print("\n\n-----Bad Videos-----")

    # if statement to clean up old playlist so that next API request has fewer "bad" videos.
    if bad_length >= 0:
        for i in range(bad_length):
            # del_videos.api_request(api_key_private, bad_vid_list[i].pl_item_id)
            print(bad_vid_list[i].title)

    print("\n\n-----Good Videos-----")

    for i in range(good_length):
        # add_videos.api_request(api_key_private, new_pl_id, vid_list[i].vid_id)
        # del_videos.api_request(api_key_private, vid_list[i].pl_item_id)
        print(good_vid_list[i].title)



if __name__ == "__main__":
    main()