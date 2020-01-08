from torrent import Torrent
from sys import argv

# Verifies correct usage
if len(argv) != 2:
    print("Error, incorrect usage!")
    print("Usage: python app.py <path/to/torrent/file>")
    exit()

FILE_NAME = str(argv[1])

torrent = Torrent(FILE_NAME)

pass
