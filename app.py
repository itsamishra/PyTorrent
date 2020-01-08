import bencode
from collections import OrderedDict


# Opens torrent file, parses
def decode_torrent(file_name: str) -> OrderedDict:
    with open(file_name, "rb") as file:
        return bencode.decode(file.read())


FILE_NAME = "debian-10.2.0-amd64-netinst.iso.torrent"
torrent_data = decode_torrent(FILE_NAME)

pass
