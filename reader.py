def read_music_file(music_file):
    records=[]
    with open(music_file, "r") as file:# open file to read
        header=file.readline().strip().split("|")
        if header[0] != "MULIB":
            print("Error, invalid file format")
        # Read the summary line
        file.readline()
        for line in file:
            line=line.strip()

            if not line:
                continue

            fields=line.split("|")

            if len(fields)!=7:
                print("Error, invalid file format")
                continue

            record={
                "Song ID":int(fields[0]),
                "Song name":fields[1],
                "Artist":fields[2],
                "Album":fields[3],
                "Genre":fields[4],
                "Duration":int(fields[5]),
                "Year released":int(fields[6])
            }
            records.append(record)
    return records

# Display column header
def display_header():
    print(f"{'Song ID':<10} | "
          f"{'Song name':<30} | "
          f"{'Artist':<20} | "
          f"{'Album':<20} | "
          f"{'Genre':<15} | "
          f"{'Duration':<10} | "
          f"{'Year released':<10}")
    print(
        "----------------------------------------------------------------------------------------------------------------------------------------------\n")

# Display record
def display_music(records):
    for record in records:
        print(f"{record['Song ID']:<10} | "
        f"{record['Song name']:<30} | "
        f"{record['Artist']:<20} | "
        f"{record['Album']:<20} | "
        f"{record['Genre']:<15} | "
        f"{record['Duration']:<10} | "
        f"{record['Year released']:<10}"
)

# Searchability
def search_song_name(records, songName):
    matches = []
    for record in records:
        if record["Song name"].strip().lower() == songName.strip().lower():
            matches.append(record)
    return matches


def search_artist(records, artist):
    matches = []
    for record in records:
        if record["Artist"].strip().lower() == artist.strip().lower():
            matches.append(record)
    return matches


def search_album(records, album):
    matches = []
    for record in records:
        if record["Album"].strip().lower() == album.strip().lower():
            matches.append(record)
    return matches


def search_genre(records, genre):
    matches = []
    for record in records:
        if record["Genre"].strip().lower() == genre.strip().lower():
            matches.append(record)
    return matches


def search_yearReleased(records, yearReleased):
    matches = []
    for record in records:
        if record["Year released"] == yearReleased:
            matches.append(record)
    return matches

# Read the music file
songs=read_music_file("music_sample.txt")

# Display Music Library
print("Music Library")
print("-----------------\n")
print("Number of songs:", len(songs))
if songs:
    duration=sum(record["Duration"] for record in songs)
    print("Duration:", duration,"seconds")
display_header()
display_music(songs)


