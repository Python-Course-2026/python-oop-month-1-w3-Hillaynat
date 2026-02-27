class Playlist:
    def __init__(self):
        self.tracks = []
    def get_duration (self):
        length = 0
        for track in self.tracks:
            length += track
        return length