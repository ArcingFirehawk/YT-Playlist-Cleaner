"""
PURPOSE: Removes videos from a playlist.
"""

import os
from common_funcs import get_env, build_service_obj



# Builds API request.
def api_request(api_key, pl_item_id):
    youtube = build_service_obj(False, api_key)

    request = youtube.playlistItems().delete(
        id=pl_item_id
    )
    
    request.execute()


def main():
    api_key_private = "Credentials/client_secret_file.json"
    pl_item_id = get_env("TEST_PLAYLIST_ITEM_ID")
    
    
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"
    
    api_request(api_key_private, pl_item_id)


if __name__ == "__main__":
    main()