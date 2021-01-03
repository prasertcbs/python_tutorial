# Python 3.6 - Formatted string literals

def demo():
    track = "Perfect"
    artist = "Ed Sheeran"
    album = "divide"
    download = 1276738
    print(f"track name = {track}, artist = {artist}, download = {download:,}")  # string interpolation
    print("track name = {}, artist = {}".format(track, artist))


if __name__ == '__main__':
    demo()
