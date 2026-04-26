class Video:
    def __init__(self, name, pl_id, videos=None):
        self.name = name
        self.pl_id = pl_id
        
        if videos is None:
            self.videos = []
        else:
            self.videos = videos


    def __str__(self):
        return f"\nThe playlist {self.name} has the playlist ID of {self.pl_id}."