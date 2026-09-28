def write_music_file(music_file, records):
    with open(music_file, 'w') as file:
        file.write(f"MULAB \n") #MULAB stands for Music library
        file.write(f"Songs: {len(records)} | ")
        file.write(f"Durations: {sum(record["Duration"] for record in records)} seconds \n")

        for record in records:
            line="|".join([
                str(record["ID"]),
                record["Song name"],
                record["Artist"],
                record["Album"],
                record["Genre"],
                str(record["Duration"]),
                str(record["Year released"]).lower()
            ])
            file.write(line+"\n")

sample_songs=[
    {
        "ID": 100001,
        "Song name": "What is love?",
        "Artist": "Twice",
        "Album": "What is love?",
        "Genre": "K-pop",
        "Duration": 224, # Duration converted to seconds in order to calc sum of duration of library (3mins44sec)
        "Year released": "2018"},
    {
        "ID": 100002,
        "Song name": "Love Story",
        "Artist": "Taylor Swift",
        "Album": "Fearless",
        "Genre": "Country pop",
        "Duration": 237, # Duration convert to seconds to easy to calc the total duration of songs in music library
        "Year released": "2008"
    }
]
write_music_file("music_sample.txt", sample_songs)
print("File successfully created!")



