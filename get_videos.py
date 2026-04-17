"""
PURPOSE: Get the videos of a Youtube playlist via the Youtube Data API and output them into a file.
"""

import os
import googleapiclient.discovery


# Function to get a specific .env variable.
def get_env(env_var):
    from dotenv import load_dotenv

    load_dotenv()
    return(os.getenv(env_var))


# Extracts the video IDs from the Youtube API's output.
def dict_extract(input):
    max = input["pageInfo"]["resultsPerPage"]
    print(f"Here's the # of videos: {max}.")

    #for ()



# Function to print input to file.
def print_to_file(input):
    import json
    
    with open("Output/videoFile.json", "w") as f:
        json.dump(input, f)



    #with open("videoFile.txt", "a") as f:
        #f.write(input) 


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = get_env("API_KEY")

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.playlistItems().list(
        part="contentDetails,id,snippet,status",
        maxResults=3,
        playlistId=get_env("PLAYLIST_ID")
    )
    response = request.execute()

    print(f"Here's the response from Youtube: {response}")

    print_to_file(response)

    #dict_extract(response)
    #print(f"here's the number of entries: {response[pageInfo[page]]}")

    

if __name__ == "__main__":
    main()