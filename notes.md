In my first request to the API, I asked for the IDs of the first 5 videos. However, they weren't what I was looking for. So, I tried the getting all fields for one video to isolate the actual video ID. It's under "[index][contentDetail][videoId]" or "[index][snippet][resourceId][videoId]".

In my API output testing, I found out that, among other things, unavailable videos have a privacy status called "privacyStatusUnspecified" as opposed to "public". I can use that to modify my query to only get the videos that are available.

I renamed my project, but found out that my virtual environment couldn't find my packages. After a little digging in the directory I found the "pyvenv.cfg" and edited that too. However, there were some issues the next day, so I jsut remade the directory.

Writing the YT API's output (of video IDs) to a text file didn't work, so I continued with .json.

The max # of results I can get per query is 50.

Adding videos to playlists can be done with a Video ID, but removing them from playlists requires a Playlist Item ID.