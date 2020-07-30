import re
from collections import Counter
from time import sleep
import pyautogui
import pytesseract
from PIL import Image

from Message import Message


def most_frequent(List):
    """
    returns most frequent element in a list, along with its frequency
    :param List:
    :return:
    """
    occurence_count = Counter( List )
    num, counter = occurence_count.most_common( 1 )[0]
    return num, counter


def parseMessageBuffer(msgBuffer):
    """
    Takes a message from the buffer and returns a tuple for comparatorList.
    :param msgBuffer:
    :return:
    """
    msgObj = Message( msgBuffer )
    x = []
    x.append( msgObj.getname() )
    x.append( msgObj.gettime() )
    x.append( msgObj.getmessages() )
    return tuple( x )


def returnComparatorList(imageName):
    """
    returns a nested list of messages in tuples, so they can easily compared in returnComparison
    :param imageName:
    :return:
    """
    str_list, regex_flag = returnstrandregexlist(
        imageName )  # calls returnStrAndRegexList() to receive str_list and regex_flag for the given image.

    # just a loop to print out regex_flag and str_list to check for Debugging purposes
    # for i in range(len(str_list)):
    #     print(str(regex_flag[i]) + " " + str_list[i])
    # print('')

    messagesBuffer = []
    comparatorList = []
    messagesBuffer.append( str_list[0] )
    for i in range( 1, len( str_list ) ):
        if (regex_flag[i] == 0):
            messagesBuffer.append( str_list[i] )
        else:
            comparatorList.append( parseMessageBuffer( messagesBuffer ) )
            messagesBuffer = []
            messagesBuffer.append( str_list[i] )
    comparatorList.append( parseMessageBuffer( messagesBuffer ) )
    return (comparatorList)


def pyautoguiMoveClickSleep(x_, y_, dur_, pause_):
    pyautogui.moveTo( x_, y_, duration=dur_ )
    pyautogui.click()
    sleep( pause_ )


def pyautoguiMoveTypeSleep(x_, y_, dur_, pause_, link_):
    pyautogui.moveTo( x_, y_, duration=dur_ )
    pyautogui.typewrite( link_, 0 )
    sleep( pause_ )


def returnstrandregexlist(imageName):
    """
    This function receives a filename of an image as input and returns two lists.
    The first list is called str_list.
    It splits the entire image into a list of lines and spits it out.
    The second list is called regex_flag.
    This list is the same length as str_list.
    It contains flags corresponding to every element of 1.
    If str_list[i] satisfies the given regex filter (eg "11:52 AM"), regex_flag[i] is 1.
    otherwise it is 0.
    :param imageName:
    :return:
    """
    # reading a long string from the image
    strin = pytesseract.image_to_string( Image.open( imageName ) )

    # splitting that long string into many lines
    str_list = strin.splitlines()

    # removing blank lines from str_list
    for string in str_list:
        if len( string ) == 0:
            str_list.remove( string )

    # initializing regex_flag with 0s
    regex_flag = [0] * len( str_list )

    # going through entire str_list to set regex flags for lines that
    # satisfy the given condition
    for i in range( len( regex_flag ) ):
        if re.search( "\d?\d:\d{2}\s*[AP]M", str_list[i] ):
            regex_flag[i] = 1

    # if regex_flag does not start with 1, ie, the str_list does not start with a timestamp,
    # elements from the beginning of both lists are popped
    # until a 1 is reached.
    while regex_flag[0] == 0:
        regex_flag.pop( 0 )
        str_list.pop( 0 )

    # both lists are returned
    return str_list, regex_flag
