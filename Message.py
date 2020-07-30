import re

def getnametime(x):
    matchobj = re.search("(.+)(\d?\d:\d{2}\s*[AP]M)", x)
    return(matchobj.group(1), matchobj.group(2))

class Message:

    def __init__(self, strings):
        self.strings = []
        self.strings.extend(strings)
        self.name, self.time = getnametime(strings[0])
        self.strings.pop(0)
        self.strings = tuple(self.strings)

    def show(self):
        print("Name: " + self.name)
        print("Time: " + self.time)
        print("Messages: ")
        for i in self.strings:
            print(i)
        print('')

    def getname(self):
        return(self.name)

    def gettime(self):
        return(self.time)

    def getmessages(self):
        return(self.strings)