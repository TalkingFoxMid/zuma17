class TestFsProvider:
    """FsProvider для тестов, чтобы не обрщааться к файловой
    системе"""
    def __init__(self):
        self.files = {"leaderboard": "",
                      "lb.hash": ""}

    def write_in_file(self, file_name, text, mode):
        self.files[file_name] = text

    def read_from_file(self, file_name, mode):
        return self.files[file_name]
