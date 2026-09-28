def read_music_file(music_file):
    records=[]
    with open(music_file, "r") as file:
        header=file.readline().strip().split("|")
        if header[0]!="MULAB":
            print("Error, invalid file format")
        summary=file.readline().strip()
        for line in file:
            line=line.strip()
            if not line:
                continue
            fields=line.split("|")
            if len(fields)!=7:
                print("Error, invalid file format")
            record={
                "ID":int(fields[0]),
                "Song name":fields[1],
                "Artist":fields[2],
                "Album":fields[3],
                "Genre":fields[4],
                "Duration":int(fields[5]),
                "Year released":int(fields[6])
            }
            records.append(record)
    return records

def display_music(records):
    for record in records:
        print(f"{record["ID"]} | "
        f"{record["Song name"]} | "
        f"{record["Artist"]} | "
        f"{record["Album"]} | "
        f"{record["Genre"]} | "
        f"{record["Duration"]} | "
        f"{record["Year released"]} | "
)

# Searchability
def search_song_name(records, songName): # Search by song's name
    for record in records:
        if record["Song name"] == songName:
            return record

def search_artist(records, artist): # Search by artist's name
    for record in records:
        if record["Artist"] == artist:
            return record

def search_album(records, album): # Search by album's name
    for record in records:
        if record["Album"] == album:
            return record

def search_genre(records, genre): # Search by genre
    for record in records:
        if record["Genre"] == genre:
            return record

def search_yearReleased(records, yearReleased): # Search by year released
    for record in records:
        if record["Year released"] == yearReleased:
            return record

# Read the music file
songs=read_music_file("music_sample.txt")

print("Music Library")
print("-----------------\n")

display_music(songs)

print("Number of songs:", len(songs))
if songs:
    duration=sum(record["Duration"] for record in songs)
    print("Duration:", duration,"seconds")

