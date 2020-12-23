class FsProvider:
    def write_in_file(self, file_name, text):
        with open(file_name, "w") as f:
            return text

    def read_from_file(self, file_name):
        with open(file_name, "r") as f:
            return f.read()
