"""
PURPOSE: Get the videos of a Youtube playlist via the Youtube Data API and output them into a file.
"""

import os
from common_funcs import get_env, print_to_file, build_service_obj
from Classes.Video import Video



# Extracts the API's output into the Video class format.
def extract(api_response):
    good_vid_list = []  # List containing public videos.
    bad_vid_list = []   # List containing unavailable videos.
    length = api_response["pageInfo"]["resultsPerPage"]


    for i in range(length):
        vid_status = api_response["items"][i]["status"]["privacyStatus"]

        if vid_status == "public":
            vid_title = api_response["items"][i]["snippet"]["title"]
            vid_creator = api_response["items"][i]["snippet"]["videoOwnerChannelTitle"]
            vid_id = api_response["items"][i]["contentDetails"]["videoId"]
            pl_item_id = api_response["items"][i]["id"]

            good_vid_list.append(Video(vid_title, vid_id, vid_creator, pl_item_id))
        else:
            vid_title = f"Unavailable{i + 1:02d}"
            vid_creator = "N/A"
            vid_id = api_response["items"][i]["contentDetails"]["videoId"]
            pl_item_id = api_response["items"][i]["id"]

            bad_vid_list.append(Video(vid_title, vid_id, vid_creator, pl_item_id))
    
    return good_vid_list, bad_vid_list





# Builds API request.
def api_request(api_key, pl_id, num_results=1):
    youtube = build_service_obj(False, api_key)

    request = youtube.playlistItems().list(
        part="snippet,contentDetails,status",
        maxResults=num_results,
        playlistId=pl_id
    )

    try:
        response = request.execute()
        msg()
        
        return response
    except Exception as e:
        print(f"\n\nThere was an error with the get request. ERROR: {e}.")


# Prints a message to console notifying user of successful operation.
def msg():
    print(f"\n\nSucessfully retrieved the videos from YouTube.")




def main():
    api_key = get_env("PUBLIC_API_KEY")
    pl_id = get_env("OLD_PLAYLIST_ID")
    max_results = 3

    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"
    
    response = api_request(api_key, pl_id, max_results)

    print_to_file(response, "rawResponse.json")

    good_vid_list, bad_vid_list = extract(response)
    good_length = len(good_vid_list)
    bad_length = len(bad_vid_list)

    if good_length > 0:
        print("\n\n-----Good Videos List-----")
        for i in range(good_length):
            print(good_vid_list[i].title)
    
    if bad_length > 0:
        print("\n-----Bad Videos List-----")
        for i in range(bad_length):
            print(bad_vid_list[i].title)
    print("\n\n")

    print_to_file(good_vid_list, "processedResponseGood.json")
    print_to_file(bad_vid_list, "processedResponseBad.json")


if __name__ == "__main__":
    main()