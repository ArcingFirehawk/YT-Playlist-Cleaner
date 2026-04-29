"""
PURPOSE: Testing range function with objects.
"""

import os
from Classes.Video import Video
import get_videos


videos = []


# Extracts video IDs from Youtube API's output using classes.
def api_class_extract(input):
    vid_list = []
    length = input["pageInfo"]["resultsPerPage"]


    for i in range(length):
        vid_status = input["items"][i]["status"]["privacyStatus"]

        if vid_status == "public":
            vid_title = input["items"][i]["snippet"]["title"]
            vid_id = input["items"][i]["contentDetails"]["videoId"]
            vid_creator = input["items"][i]["snippet"]["videoOwnerChannelTitle"]
            pl_item_id = input["items"][i]["id"]

            vid_list.append(Video(vid_title, vid_id, vid_creator, pl_item_id))
            

    return vid_list


def main():
    API_SERVICE_NAME = "youtube"
    API_VERSION = "v3"
    api_key = get_videos.get_env("API_KEY")
    pl_id = get_videos.get_env("OLD_PLAYLIST_ID")
    num_results = 3

    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"
    
    response = get_videos.api_request(API_SERVICE_NAME, API_VERSION, api_key, pl_id, num_results)
    print(f"\n\n{response}\n\n")

    processed = api_class_extract(response)

    print(processed)
    print(processed[0])
    print(processed[1])
    print(processed[1].vid_id)



if __name__ == "__main__":
    main()