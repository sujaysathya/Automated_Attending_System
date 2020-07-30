import re
from collections import Counter
from time import sleep

import pyautogui
import pytesseract
from PIL import Image

from Message import Message



def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i

    return num,counter

# returns str list with corresponding regex flags
def returnStrAndRegexList(imageName):

    strin = pytesseract.image_to_string(Image.open(imageName))
    str_list = strin.splitlines()
    for string in str_list:
        if(len(string) == 0):
            str_list.remove(string)
    regex_flag = [0] * len(str_list)

    for i in range(len(regex_flag)):
        if(re.search("\d?\d:\d{2}\s*[AP]M", str_list[i])):
            regex_flag[i] = 1
    while(regex_flag[0] == 0):
        regex_flag.pop(0)
        str_list.pop(0)
    return(str_list, regex_flag)


# should return what to reply
def returnComparatorList(imageName):

    str_list, regex_flag = returnStrAndRegexList(imageName)

    for i in range(len(str_list)):
        print(str(regex_flag[i]) + " " + str_list[i])

    print('')

    messagesBuffer = []
    comparatorList = []
    messagesBuffer.append(str_list[0])
    for i in range(1, len(str_list)):
        if(regex_flag[i] == 0):
            messagesBuffer.append(str_list[i])
        else:
            messageObj = Message(messagesBuffer)

            x = []
            x.append(messageObj.getname())
            x.append(messageObj.gettime())
            x.append(messageObj.getmessages())
            comparatorList.append(tuple(x))

            messagesBuffer = []
            messagesBuffer.append(str_list[i])

    messageObj = Message(messagesBuffer)

    x = []
    x.append(messageObj.getname())
    x.append(messageObj.gettime())
    x.append(messageObj.getmessages())
    comparatorList.append(tuple(x))

    return(comparatorList)

def returnComparison(oldImage, newImage, opt):
    print("printing old")
    x = returnComparatorList(oldImage)
    print("printing new")
    y = returnComparatorList(newImage)

    

    set_difference = set(y) - set(x)
    list_difference = list(set_difference)


    if(opt == 0):
        return(len(list_difference))
    elif(opt == 1):
        lentot = 0
        for element in list_difference:
            lentot += len(element[2])
        return(lentot)

def returnMostCommonWord(imageName):
    print("before function call of rmc")
    x = returnComparatorList(imageName)
    print("after function call of rmc")
    listOfWords = []
    for i in x:
        for j in i[2]:
            listOfWords.append(j)
    print("after for loop call")

    a1,b1=most_frequent(listOfWords)
    print("after return of a1,b1")
    return(a1,b1)

def pyautoguiMoveClickSleep(x_, y_, dur_, pause_):
    pyautogui.moveTo( x_, y_, duration=dur_ )
    pyautogui.click()
    sleep( pause_ )


def pyautoguiMoveTypeSleep(x_, y_, dur_, pause_, link_):
    pyautogui.moveTo( x_, y_, duration=dur_ )
    pyautogui.typewrite( link_, 0 )
    sleep( pause_ )