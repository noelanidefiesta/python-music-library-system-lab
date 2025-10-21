class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artists_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self._register_song()

    @classmethod
    def _reset_class_state(cls):
        cls.count = 0
        cls.genres = []
        cls.artists = []
        cls.genre_count = {}
        cls.artists_count = {}

    def _register_song(self):
        type(self).count += 1
        if self.genre not in type(self).genres:
            type(self).genres.append(self.genre)
        if self.artist not in type(self).artists:
            type(self).artists.append(self.artist)
        type(self).genre_count[self.genre] = type(self).genre_count.get(self.genre, 0) + 1
        type(self).artists_count[self.artist] = type(self).artists_count.get(self.artist, 0) + 1
