import bencode


class Torrent:
    # Reads torrent file & parses data
    def __init__(self, torrent_file_name: str):
        self.file_name = torrent_file_name
        with open(torrent_file_name, "rb") as file:
            self.torrent_data = bencode.decode(file.read())
        self.torrent_length = self.torrent_data["info"]["length"]
        self.piece_length = self.torrent_data["info"]["piece length"]
        self.pieces = self.torrent_data["info"]["pieces"]
        self.announce = self.torrent_data["announce"]

    # Returns string representation of torrent
    def __str__(self) -> str:
        return str(self.torrent_data)
