import tempfile
import os.path


class File:
    new_filename = 1

    def __init__(self, filename):
        self.filename = filename

        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                pass

        with open(filename, 'r') as f:
            self.file_strings = f.readlines()

        self.current = 0

    def read(self):
        with open(self.filename, 'r') as f:
            return f.read()

    def write(self, string):
        with open(self.filename, 'w') as f:
            f.write(string)
            return len(string)

    def __add__(self, other):
        new_path = os.path.join(tempfile.gettempdir(), str(self.new_filename))
        File.new_filename += 1
        with open(new_path, 'w') as nf:
            with open(self.filename, 'r') as f:
                file_strings = f.readlines()
                for i in file_strings:
                    nf.write(i)

            with open(other.filename, 'r') as f:
                file_strings = f.readlines()
                for i in file_strings:
                    nf.write(i)

        return File(new_path)

    def __str__(self):
        return os.path.abspath(self.filename)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= len(self.file_strings):
            self.current = 0
            raise StopIteration

        result = self.file_strings[self.current]
        self.current += 1
        return result
