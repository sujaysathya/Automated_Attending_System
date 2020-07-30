from HelperFunctions import getnametime


class Message:
    """
    This is a Message class.
    It consists of three attributes.
    strings are all the messages that the particular person has sent.
    name is the name of the person sending the messages time is the time at which the messages were sent by the person
    """

    def __init__(self, strings):
        self.strings = []
        self.strings.extend( strings )
        self.name, self.time = getnametime( strings[0] )
        self.strings.pop( 0 )
        self.strings = tuple( self.strings )

    # simple function to show the name, time and messages of the object
    def show(self):
        print( "Name: " + self.name )
        print( "Time: " + self.time )
        print( "Messages: " )
        for i in self.strings:
            print( i )
        print( '' )

    def getname(self):
        return self.name

    def gettime(self):
        return self.time

    def getmessages(self):
        return self.strings
