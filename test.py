from reader import read_music_file,search_song_name, search_artist, search_album, search_genre,search_yearReleased
from writer import write_music_file

records=[
    {
    "Song ID":10003,
    "Song name": "Photograph",
    "Artist": "Ed Sheeran",
    "Album": "X",
    "Genre": "Pop",
    "Duration": 259,
    "Year released": 2014
},
    {
    "Song ID":10004,
    "Song name": "A Thousand Years",
    "Artist": "Christina Perri",
    "Album": "None", # no album belong to
    "Genre": "Pop",
    "Duration": 259,
    "Year released": 2011
    }
]
write_music_file("output.mulib", records)
read_records=read_music_file("output.mulib")

# Search record using info (song's name, artist, genre, album, year released)
songName_result=search_song_name(read_records, "A Thousand Years")
print("Songs with matching name: ")
if songName_result:
    for record in songName_result:
        print(f"Songs: {record['Song ID']} | "
            f"{record['Song name']} | "
            f"{record['Artist']} | "
            f"{record['Album']} | "
            f"{record['Genre']} | "
            f"{record['Duration']} | "
            f"{record['Year released']}"
        )
else:
    print("No song found")

artist_result=search_artist(read_records, "Ed Sheeran")
print("Songs with matching artist: ")
if artist_result:
    for record in artist_result:
        print(f"Songs: {record['Song ID']} | "
        f"{record['Song name']} | "
        f"{record['Artist']} | "
        f"{record['Album']} | "
        f"{record['Genre']} | "
        f"{record['Duration']} | "
        f"{record['Year released']}"
    )
else:
    print("No song found")

album_result=search_album(read_records, "X")
print("Songs with matching album: ")
if album_result:
    for record in album_result:
        print(f"Songs: {record['Song ID']} | "
              f"{record['Song name']} | "
              f"{record['Artist']} | "
              f"{record['Album']} | "
              f"{record['Genre']} | "
              f"{record['Duration']} | "
              f"{record['Year released']}"
              )
else:
    print("No song found")

genre_result=search_genre(read_records, "Pop")
print("Songs with matching genre: ")
if genre_result:
    for record in genre_result:
        print(f"Songs: {record['Song ID']} | "
              f"{record['Song name']} | "
              f"{record['Artist']} | "
              f"{record['Album']} | "
              f"{record['Genre']} | "
              f"{record['Duration']} | "
              f"{record['Year released']}"
              )
else:
    print("No song found")

yearReleased_result=search_yearReleased(read_records, 2011)
print("Songs with matching year released: ")
if yearReleased_result:
    for record in yearReleased_result:
        print(f"Songs: {record['Song ID']} | "
              f"{record['Song name']} | "
              f"{record['Artist']} | "
              f"{record['Album']} | "
              f"{record['Genre']} | "
              f"{record['Duration']} | "
              f"{record['Year released']}"
              )
else:
    print("No song found")

