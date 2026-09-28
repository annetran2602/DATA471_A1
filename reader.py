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
# Read the music file
songs=read_music_file("music_sample.txt")

print("Music Library")
print("-----------------\n")

display_music(songs)

print("Number of songs:", len(songs))
if songs:
    duration=sum(record["Duration"] for record in songs)
    print("Duration:", duration,"seconds")

