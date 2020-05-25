from datetime import datetime


class Logger:

    def __init__(self, filename='log.md'):
        self.filename = filename
        self.contents = ["Date: {0}\n".format(datetime.now())]
        self.contents.append("----------------------------------------\n")

    def log(self, message):
        self.contents.append(message)
        self.contents.append('\n')

    def save(self):
        f = open(self.filename, "w")
        f.write(''.join(self.contents))
        f.close()

