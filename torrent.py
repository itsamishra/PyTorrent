import bencode


class Torrent:
    # Parses data
    def __init__(self, torrent_file_name: str):
        self.file_name = torrent_file_name
        with open(torrent_file_name, "rb") as file:
            self.torrent_data = bencode.decode(file.read())

    def __str__(self) -> str:
        return str(self.torrent_data)
