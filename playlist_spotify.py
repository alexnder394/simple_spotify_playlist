playlists = {
        'title': 'Patagonia bus',
        'author': 'Reda',
        'songs': [
        {'title': 'song1', 'artist': 'arts', 'duration': 2.5},
        {'title': 'song2', 'artist': ['arts2', 'arts2.1'], 'duration': 3.5},
        {'title': 'song3', 'artist': 'arts3', 'duration': 3.75}
    ]
}
playlist_length = 0
for song in playlists['songs']:
    playlist_length += (song["duration"])
print(playlist_length)
