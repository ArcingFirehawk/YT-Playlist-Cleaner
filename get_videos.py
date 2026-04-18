"""
PURPOSE: Get the videos of a Youtube playlist via the Youtube Data API and output them into a file.
"""

import os
import googleapiclient.discovery
import json


# Function to get a specific .env variable.
def get_env(env_var):
    from dotenv import load_dotenv

    load_dotenv()
    return(os.getenv(env_var))


# Extracts the video IDs from the Youtube API's output.
def api_extract(input):
    x = 0
    vidList = []
    max = input["pageInfo"]["resultsPerPage"]
    #print(max)

    while x < max:
        num = x + 1

        vidStatus = input["items"][x]["status"]["privacyStatus"]

        if vidStatus == "public":
            vidId = input["items"][x]["contentDetails"]["videoId"]
            vidList.append(vidId)

    return vidList


# Function to print input to file.
def print_to_file(input):
    #import json
    
    with open("Output/videoFile.json", "w") as f:
        json.dump(input, f)


def extract_json(file_name):
    json.load


# Function to build the API request.
def api_request():
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = get_env("API_KEY")

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.playlistItems().list(
        part="contentDetails,status",
        maxResults=1,
        playlistId=get_env("PLAYLIST_ID")
    )

    return request.execute()


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"
    response = api_request()

    print(f"\n\nHere's the response from Youtube: \n{response}\n\n")
    print_to_file(response)

    processed = api_extract(response)

    print(f"\n\nHere's the list of video IDs: {processed}.\n\n")

    #print(f"here's the number of entries: {response[pageInfo[page]]}")
    #print(f"here's the number of entries: {response[items[contentDetails[videoId]]]}")

    

if __name__ == "__main__":
    main()