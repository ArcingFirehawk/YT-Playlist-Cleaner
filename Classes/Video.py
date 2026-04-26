class Video:
    def __init__(self, title, vid_id, pl_item_id):
        self.title = title
        self.vid_id = vid_id
        self.pl_item_id = pl_item_id


    def __str__(self):
        return f"\nThe video {self.title} has the video ID and playlist item ID of {self.vid_id}:{self.pl_item_id}."