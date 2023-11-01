# Cintia Biro-Hajnal 25/10/23

class FileItem:
    def __init__(self, name, permissions, owner, size):
        self.name = name
        self.permissions = permissions
        self.owner = owner
        self.size = size

    def display(self):
        print(f"Name: {self.name}")
        print(f"Permissions: {self.permissions}")
        print(f"Owner: {self.owner}")
        print(f"Size: {self.size} bytes")

class CsvFile(FileItem):
    def __init__(self, name, permissions, owner, size, delimiter):
        super().__init__(name, permissions, owner, size)
        self.delimiter = delimiter

    def display(self):
        super().display()
        print(f"Delimiter: {self.delimiter}")

class JpgFile(FileItem):
    def __init__(self, name, permissions, owner, size, resolution):
        super().__init__(name, permissions, owner, size)
        self.resolution = resolution

    def display(self):
        super().display()
        print(f"Resolution: {self.resolution}")

class Mp3File(FileItem):
    def __init__(self, name, permissions, owner, size, duration):
        super().__init__(name, permissions, owner, size)
        self.duration = duration

    def display(self):
        super().display()
        print(f"Duration: {self.duration} seconds")

# Example usage:
file1 = CsvFile("data.csv", "rw-r--r--", "user1", 1024, ",")
file2 = JpgFile("image.jpg", "rw-rw-r--", "user2", 2048, "1920x1080")
file3 = Mp3File("song.mp3", "rw-r--r--", "user1", 4096, 240)

file1.display()
file2.display()
file3.display()
