"""
PURPOSE: To consolidate get_videos.py, add_videos.py, and del_videos.py into one place.
"""

import os
import get_videos, add_videos, del_videos
from common_funcs import get_env
from token_handling import check_token



def main():
    api_key_public = get_env("API_KEY")
    api_key_private = check_token()
    old_pl_id = get_env("OLD_PLAYLIST_ID")
    new_pl_id = get_env("NEW_PLAYLIST_ID")
    max_results = 1 # Max is 50.


    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

    response = get_videos.api_request(api_key_public, old_pl_id, max_results)
    
    good_vid_list, bad_vid_list = get_videos.extract(response)
    good_length = len(good_vid_list)
    bad_length = len(bad_vid_list)

    # if statement to clean up old playlist so next API request has fewer "bad" videos.
    if bad_length >= 20:
        for i in range(bad_length):
            del_videos.api_request(api_key_private, bad_vid_list[i].pl_item_id)

    for i in range(good_length):
        add_videos.api_request(api_key_private, new_pl_id, good_vid_list[i].vid_id, good_vid_list[i].title)
        del_videos.api_request(api_key_private, good_vid_list[i].pl_item_id, good_vid_list[i].title)


if __name__ == "__main__":
    main()