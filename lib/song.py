class Song:
    # create class attibute to keep track of the number of new songs
    count = 0
    # create empty list to keep track of genre, artist
    genres = []
    artists = []
    # a dictionary in which the keys are the names of each genre. 
    # Each genre name key should point to a value that is the number of songs that have that genre.
    genre_count = {}
    artist_count = {}


    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(self.genre)
        self.add_to_artist(self.artist)


    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment


    @classmethod
    def add_to_genres(cls, genre):
        
        # Control for duplicates, check if the count of genre in genres list = 0
        # that means the genre is not yet in genres list 
        if cls.genres.count(genre) == 0:
            # append genre to genres list
            cls.genres.append(genre)
            # create key/vaue in genre_count dict
            cls.genre_count[genre] = 1
        else: # genre is already in genres list
            cls.genre_count[genre] += 1


    @classmethod
    def add_to_artist(cls, artist):
        if cls.artists.count(artist) == 0:
            cls.artists.append(artist)
            cls.artist_count[artist] = 1
        else:
            cls.artist_count[artist] += 1


    @classmethod
    def add_to_genre_count(cls):
        return cls.genre_count
    

    @classmethod
    def add_to_artist_count(cls):
        return cls.artist_count
        


# Song("99 Problems", "Jay Z", "Rap")
# Song("Halo", "Beyonce", "Pop")
# Song("Smells Like Teen Spirit", "Nirvana", "Rock")
# Song("song1", "Jay Z", "Rap")

# print(Song.count)
# print(Song.genres)
# print(Song.artists)
# print(Song.genre_count)
# print(Song.artist_count)