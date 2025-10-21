import pytest
from song import Song

def setup_function():
    Song.count = 0
    Song.genres = []
    Song.artists = []
    Song.genre_count = {}
    Song.artists_count = {}
    if hasattr(Song, '_temp_genre'):
        delattr(Song, '_temp_genre')
    if hasattr(Song, '_temp_artist'):
        delattr(Song, '_temp_artist')

def test_song_creation_increments_count():
    s1 = Song('Lose Yourself', 'Eminem', 'Rap')
    assert Song.count == 1
    s2 = Song('Hey Jude', 'The Beatles', 'Rock')
    assert Song.count == 2

def test_genres_and_artists_unique_lists():
    Song('S1', 'Artist A', 'Genre X')
    Song('S2', 'Artist B', 'Genre X')
    Song('S3', 'Artist A', 'Genre Y')
    assert set(Song.genres) == {'Genre X', 'Genre Y'}
    assert set(Song.artists) == {'Artist A', 'Artist B'}

def test_genre_count_and_artist_count():
    Song('A', 'Artist1', 'Pop')
    Song('B', 'Artist2', 'Pop')
    Song('C', 'Artist1', 'Rock')
    assert Song.genre_count == {'Pop': 2, 'Rock': 1}
    assert Song.artists_count == {'Artist1': 2, 'Artist2': 1}

def test_multiple_same_genre_artist():
    Song('One', 'ArtistZ', 'Indie')
    Song('Two', 'ArtistZ', 'Indie')
    Song('Three', 'ArtistY', 'Indie')
    assert Song.genre_count['Indie'] == 3
    assert Song.artists_count['ArtistZ'] == 2

def test_class_attributes_persist_across_instances():
    Song('X', 'Alpha', 'Electro')
    Song('Y', 'Beta', 'Electro')
    assert Song.count >= 2
    assert 'Electro' in Song.genres
