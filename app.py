import bencode
from collections import OrderedDict
from torrent import Torrent

FILE_NAME = "debian-10.2.0-amd64-netinst.iso.torrent"
torrent = Torrent(FILE_NAME)
print(torrent)

pass
