## To-Do
+ common_funcs.build_service_obj, restrict need_auth to boolean?
+ get_token() in token_handling.py doesn't get called when token.json is invalid.

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