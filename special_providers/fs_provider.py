class FsProvider:
    """Пишет в файл, читает из файла"""
    def write_in_file(self, file_name, text, mode):

        with open(file_name, mode) as f:
            print(file_name)
            f.write(text)

    def read_from_file(self, file_name, mode):
        with open(file_name, mode) as f:
            x = f.read()

            return x
