"""
PURPOSE: Adds videos to a playlist using their video ID.
"""

import os
from common_funcs import get_env, build_service_obj
from token_handling import check_token


# Builds API request.
def api_request(api_key, pl_id, vid_id, vid_title="--"):
    youtube = build_service_obj(True, api_key)

    request = youtube.playlistItems().insert(
        part="snippet",
        body={
          "snippet": {
            "playlistId": pl_id,
            "position": 0,
            "resourceId": {
              "kind": "youtube#video",
              "videoId": vid_id
            }
          }
        }
    )
    
    try:
        request.execute()
        msg(vid_title)
    except Exception as e:
        print(f"\n\nThere was an error with the add request. ERROR: {e}.")


# Prints a message to console notifying user of successful operation.
def msg(vid_title):
    print(f"Sucessfully added \"{vid_title}\" to the new playlist.")


def main():
    api_key_private = check_token()
    playlist_id = get_env("NEW_PLAYLIST_ID")
    vid_id = get_env("TEST_VIDEO")

    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

    api_request(api_key_private, playlist_id, vid_id)


if __name__ == "__main__":
    main()