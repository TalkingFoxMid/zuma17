class TestFsProvider:
    def __init__(self):
        self.file = "[]"

    def write_in_file(self, file_name, text):
        self.file = text

    def read_from_file(self, file_name):
        return self.file
