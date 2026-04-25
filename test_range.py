"""
PURPOSE: Testing range function with objects.
"""

import json
import Classes.Video as Video


videos = []


with open("Output/videoList.json") as f:
    file = json.load(f)
    f.close()

length = len(file)


for i in range(length):
    vidStatus = file["items"][i]["status"]["privacyStatus"]

    if vidStatus == "public":
        vid_title = file["items"][i]["snippet"]["title"]
        vid_id = file["items"][i]["contentDetails"]["videoId"]
        pl_item_id = file["items"][i]["id"]


        videos.append(Video(vid_title, vid_id, pl_item_id))

        
        i += 1

print(videos)