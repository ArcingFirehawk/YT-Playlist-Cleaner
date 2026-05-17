## Commands
  + Activate virtual environment with `source .venv/Scripts/activate` in bash terminal.
  + Dectivate virtual environment with `deactivate` in bash terminal.

## To-Do
+ `token_handling.check_token()` Function
  + For some reason `credentials.refresh(Request())` doesn't seem to work.~~get an error if the token is expired.~~
  + ~~Testing the try-except with `get_videos.api_request()` instead brings up an error with an expired token. However, it now always excutes the except part.~~
  + ~~... Temporary solution is t  + Testing the try-except with `get_videos.api_request()` instead brings up an error with an expired token. However, it now always excutes the except part.o have a try-except in playlist_edit.py for the `add_videos.api_request()` and `del_videos.api_request()` to call token_handling.get_token().~~
+ ~~`common_funcs.build_service_obj()` Function~~
  + ~~common_funcs.build_service_obj, restrict need_auth to boolean~?~~
  + ~~Fi~nd way to go through if-else statement without the need_auth param.~~
    + ~~This is what's tripping up my API calls in token_handling.py.~~
+ Streamline imports (E.g., `from get_videos import api_request as get_request` and `from googleapiclient.discovery import build`).
+ Need to test add_video.py when token is expired.

## Notes
+ In my first request to the API, I asked for the IDs of the first 5 videos. However, they weren't what I was looking for. So, I tried the getting all fields for one video to isolate the actual video ID. It's under "[index][contentDetail][videoId]" or "[index][snippet][resourceId][videoId]".
+ In my API output testing, I found out that, among other things, unavailable videos have a privacy status called "privacyStatusUnspecified" as opposed to "public". I can use that to modify my query to only get the videos that are available.
+ I renamed my project, but found out that my virtual environment couldn't find my packages. After a little digging in the directory I found the "pyvenv.cfg" and edited that too. However, there were some issues the next day, so I jsut remade the directory.
+ Writing the YT API's output (of video IDs) to a text file didn't work, so I used .json.
+ The max # of results I can get per query is 50.
+ Adding videos to playlists can be done with a Video ID, but removing them from playlists requires a Playlist Item ID.
+ You shouldn't pass mutable data types as default arguements.
+ I can only add/delete one video from a playlist at a time.
+ According to the Credentials class in google.oauth2.credentials, some attributes (e.g., .expired and .valid) are depreciated. Use .token_state instead.

## Tutorials
+ YT
  + https://code.visualstudio.com/docs/languages/python
  + https://code.visualstudio.com/docs/python/python-tutorial
  + https://developers.google.com/youtube/v3/quickstart/python
  + https://developers.google.com/youtube/v3/docs/playlistItems
  + https://github.com/googleapis/google-api-python-client/tree/main


  + Uninstalling Python Libraries: https://www.w3schools.com/python/gloss_python_pip_packages_remove.asp
  + Python Virtual Environment: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

  + https://www.youtube.com/watch?v=eDe-z2Qy9x4
  + https://www.youtube.com/watch?v=i_5xPDX-erE
  + https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

  + https://stackoverflow.com/a/73376365