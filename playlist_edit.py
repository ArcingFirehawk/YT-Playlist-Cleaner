"""
PURPOSE: To consolidate the .py files into one place.
"""

import os
from Classes.Video import Video
import get_videos, add_videos, del_videos
from common_funcs import get_env
# from Classes.Playlist import Playlist



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

    response = get_videos.api_request(api_key_public, old_pl_id, max_results)
    
    good_vid_list, bad_vid_list = extract(response)
    good_length = len(good_vid_list)
    bad_length = len(bad_vid_list)

    # if statement to clean up old playlist so next API request has fewer "bad" videos.
    if bad_length >= 20:
        for i in range(bad_length):
            del_videos.api_request(api_key_private, bad_vid_list[i].pl_item_id)

    for i in range(good_length):
        add_videos.api_request(api_key_private, new_pl_id, good_vid_list[i].vid_id)
        del_videos.api_request(api_key_private, good_vid_list[i].pl_item_id)


if __name__ == "__main__":
    main()