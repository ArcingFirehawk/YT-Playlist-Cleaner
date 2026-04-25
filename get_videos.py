"""
PURPOSE: Get the videos of a Youtube playlist via the Youtube Data API and output them into a file.
"""

import os
import googleapiclient.discovery
from dotenv import load_dotenv
import json



# Gets specific .env variable.
def get_env(env_var):
    load_dotenv()
    return(os.getenv(env_var))


# Extracts video IDs from Youtube API's output.
def api_extract(input):
    i = 0   # Counter
    vidList = []    # List to contain vidTuples.
    vidTuple = () # Tuple to contain playlist item IDs and video IDs.
    max = input["pageInfo"]["resultsPerPage"]   # The # of results from the API request.

    while i < max:
        vidStatus = input["items"][i]["status"]["privacyStatus"]

        if vidStatus == "public":
            playlistItemId = input["items"][i]["id"]
            vidId = input["items"][i]["contentDetails"]["videoId"]

            vidTuple = (playlistItemId, vidId)
            vidList.append(vidTuple)
        
        i += 1

    return vidList


# Prints to .json file.
def print_to_file(input, file_name):
    file_directory = "Output/" + file_name
    
    with open(file_directory, "w") as f:
        json.dump(input, f)


# Builds API request.
def api_request(num_results):
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = get_env("API_KEY")

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.playlistItems().list(
        part="snippet,contentDetails,status",
        maxResults=num_results,
        playlistId=get_env("OLD_PLAYLIST_ID")
    )

    return request.execute()



def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"
    response = api_request(1)

    print(f"\n\nHere's the response from Youtube: \n{response}\n\n")
    print_to_file(response, "videoFile.json")

    processed = api_extract(response)
    print(f"\n\nHere's the list of video IDs: {processed}.\n\n")

    print_to_file(processed, "videoList.json")


if __name__ == "__main__":
    main()