def write_music_file(music_file, records):
    with open(music_file, 'w') as file:
        file.write(f"MULIB \n") #MULIB stands for Music library
        file.write(f"Songs: {len(records)} | ")
        file.write(f"Durations: {sum(record["Duration"] for record in records)} seconds \n")

        for record in records:
            file.write(
              f"{record['Song ID']} | "
              f"{record['Song name']} | "
              f"{record['Artist']} | "
              f"{record['Album']} | "
              f"{record['Genre']} | "
              f"{record['Duration']} | "
              f"{record['Year released']}\n")

sample_songs=[
    {
        "Song ID": 100001,
        "Song name": "What is love?",
        "Artist": "Twice",
        "Album": "What is love?",
        "Genre": "K-pop",
        "Duration": 224, # Duration converted to seconds in order to calc sum of duration of library (3mins44sec)
        "Year released": "2018"},
    {
        "Song ID": 100002,
        "Song name": "Love Story",
        "Artist": "Taylor Swift",
        "Album": "Fearless",
        "Genre": "Country pop",
        "Duration": 237, # Duration convert to seconds to easy to calc the total duration of songs in music library
        "Year released": "2008"
    },
{
        "Song ID": 100003,
        "Song name": "Photograph",
        "Artist": "Ed Sheeran",
        "Album": "X",
        "Genre": "Pop",
        "Duration": 259, # Duration convert to seconds to easy to calc the total duration of songs in music library
        "Year released": "2014"
    },
{
        "Song ID": 100004,
        "Song name": "Shape of You",
        "Artist": "Ed Sheeran",
        "Album": "Divide",
        "Genre": "Pop",
        "Duration": 279, # Duration convert to seconds to easy to calc the total duration of songs in music library
        "Year released": "2017"
    },
{
        "Song ID": 100005,
        "Song name": "Blinding Lights",
        "Artist": "The Weeknd",
        "Album": "After Hours",
        "Genre": "Pop",
        "Duration": 200, # Duration convert to seconds to easy to calc the total duration of songs in music library
        "Year released": "2020"
    }
]
write_music_file("sample_data_1.txt", sample_songs)
print("File successfully created!")



