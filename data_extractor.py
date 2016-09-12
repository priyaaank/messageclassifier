class DataExtractor:

    def __init__(self, filename="SahajChat.txt"):
        self.filename = filename

    def extract(self):
        f = open(self.filename, 'r')
        for line in f:
            print(line)


if __name__ == "__main__":
    DataExtractor().extract()
