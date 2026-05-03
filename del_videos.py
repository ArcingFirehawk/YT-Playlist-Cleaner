"""
PURPOSE: Removes videos from a playlist.
"""

import os
from common_funcs import get_env, build_service_obj
from token_handling import check_token



# Builds API request.
def api_request(api_key, pl_item_id, vid_title="--"):
    youtube = build_service_obj(False, api_key)

    request = youtube.playlistItems().delete(
        id=pl_item_id
    )

    try:
        request.execute()
        msg(vid_title)
    except Exception as e:
        print(f"\n\nThere was an error with the delete request. ERROR: {e}.")
    


# Prints a message to console notifying user of successful operation.
def msg(vid_title):
    print(f"Sucessfully deleted \"{vid_title}\" from the new playlist.")




def main():
    api_key_private = check_token()
    pl_item_id = get_env("TEST_PLAYLIST_ITEM_ID")
    
    
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"
    
    api_request(api_key_private, pl_item_id)


if __name__ == "__main__":
    main()