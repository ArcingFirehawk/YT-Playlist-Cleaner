class Video:
    def __init__(self, title, playlist_item_id, vid_id):
        self.title = title
        self.playlist_item_id = playlist_item_id
        self.vid_id = vid_id

    def __str__(self):
        return f"\nThe video {self.title} has the playlist item ID and video ID of {self.playlist_item_id}:{self.vid_id}."