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
print("Number of songs:", len(read_records))

# Search record using info (song's name, artist, genre, album, year released)
search_songName=search_song_name(read_records, "A Thousand Years")
search_artist=search_artist(read_records, "Ed Sheeran")
search_album=search_album(read_records, "X")
search_genre=search_genre(read_records, "Pop")
search_yearReleased=search_yearReleased(read_records, 2011)

# Print results
print("Songs matching name: A Thousand Years")
if search_songName:
    record=search_songName
    print(
        f"Songs: {record['Song ID']} | "
        f"{record['Song name']} | "
        f"{record['Artist']} | "
        f"{record['Album']} | "
        f"{record['Genre']} | "
        f"{record['Duration']} | "
        f"{record['Year released']}")
else:
    print("No songs matching name")

print("Songs by artist: Ed Sheeran", search_artist)
if search_artist:
    record=search_artist
    print(
        f"Songs: {record['Song ID']} | "
        f"{record['Song name']} | "
        f"{record['Artist']} | "
        f"{record['Album']} | "
        f"{record['Genre']} | "
        f"{record['Duration']} | "
        f"{record['Year released']}")
else:
    print("No songs matching artist")

print("Songs in album: X", search_album)
if search_album:
    record=search_album
    print(
        f"Songs: {record['Song ID']} | "
        f"{record['Song name']} | "
        f"{record['Artist']} | "
        f"{record['Album']} | "
        f"{record['Genre']} | "
        f"{record['Duration']} | "
        f"{record['Year released']}")
else:
    print("No songs matching album")

print("Songs in genre: Pop", search_genre)
if search_genre:
    record=search_genre
    print(
        f"Songs: {record['Song ID']} | "
        f"{record['Song name']} | "
        f"{record['Artist']} | "
        f"{record['Album']} | "
        f"{record['Genre']} | "
        f"{record['Duration']} | "
        f"{record['Year released']}")
else:
    print("No songs matching genre")

print("Songs released in 2014:", search_yearReleased)
if search_yearReleased:
    record=search_yearReleased
    print(
        f"Songs: {record['Song ID']} | "
        f"{record['Song name']} | "
        f"{record['Artist']} | "
        f"{record['Album']} | "
        f"{record['Genre']} | "
        f"{record['Duration']} | "
        f"{record['Year released']}")
else:
    print("No songs matching released year")


