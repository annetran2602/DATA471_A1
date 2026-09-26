def write_music_file(music_file, records):
    with open(music_file, 'w') as file:
        file.write(f"MULAB, \n") #MULAB stands for Music library
        file.write(f"Songs: {len(records)}\n")

        for record in records:
            line="|".join([
                str(record["ID"]),
                record["Song name"],
                record["Artist"],
                record["Album"],
                record["Genre"],
                record["Duration"],
                str(record["Year released"]).lower()
            ])
            file.write(line+"\n")

sample_songs=[
    {
        "ID": "000001",
        "Song name": "What is love?",
        "Artist": "Twice",
        "Album": "What is love?",
        "Genre": "K-pop",
        "Duration": "3 mins 44 seconds",
        "Year released": "2018"},
    {
        "ID": "000002",
        "Song name": "Love Story",
        "Artist": "Taylor Swift",
        "Album": "Fearless",
        "Genre": "Country pop",
        "Duration": "3 mins 57 seconds",
        "Year released": "2008"
    }
]
write_music_file("music_sample.txt", sample_songs)
print("File successfully created!")



