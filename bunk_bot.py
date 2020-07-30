import os
from time import sleep, time

import cv2
import pyautogui
import speech_recognition as sr

from HelperFunctions import returnComparatorList, most_frequent, pyautoguiMoveClickSleep, pyautoguiMoveTypeSleep

# theres a "tesseract.exe" file you need to download if you use this on windows
# pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Retrieving the link from the google docs file

# PLEASE Edit these Global variables as necessary
filelocation = "C:\\Users\\sujay sathya\\Downloads\\zm.txt"
x11, y11, x12, y12, x13, y13 = 1625, 156, 1694, 976, 1872, 985


def returnMostCommonWord(imageName):
    """
    The most common message in the image along with its frequency
    :param imageName:
    :return:
    """
    x = returnComparatorList( imageName )
    listOfWords = []
    for i in x:
        for j in i[2]:

            listOfWords.append( j )
    a1, b1 = most_frequent( listOfWords )
    return a1, b1


def returnComparison(oldImage, newImage, opt):
    """
    oldImage and newImage are filenames to the older image, and the new image.

    The function should return the number of new messages that have appeared in the new image,
    when compared to the old image.

    When opt is set to 0, it returns the number of new Message Objects that have been created.
    When opt is set to 1, it adds up the total number of new individual messages within all the new message objects.

    :param oldImage:
    :param newImage:
    :param opt:
    :return:
    """
    x = returnComparatorList( oldImage )
    y = returnComparatorList( newImage )
    set_difference = set( y ) - set( x )
    list_difference = list( set_difference )
    if opt == 0:
        return len( list_difference )
    elif opt == 1:
        lentot = 0
        for element in list_difference:
            lentot += len( element[2] )
        return lentot


# Using the pyautogui library to automate my mouse to download a google docs file that has the link to my online class
# the coordinates given here are strictly w.r.t my computer screen size and where i have placed my icons
# to find your own coordinates, read the pyautogui documentation: https://pyautogui.readthedocs.io/en/latest/

a = time()


def clock():
    """
    The clock function returns the amount of time that had passed since the code had begun execution in minutes
    :return:
    """
    return (time() - a) // 60


def answerAttendance():
    pyautogui.moveTo( x11, y11, duration=1 )
    pyautogui.click()
    sleep( 2 )
    pyautogui.moveTo( x12, y12, duration=1 )
    pyautogui.click()
    pyautogui.typewrite( "present sir", 1 )
    pyautogui.moveTo( x13, y13, duration=1 )
    pyautogui.click()
    sleep( 2 )


if __name__ == "__main__":
    x_list = [690, 847, 108, 230, 484, 1917]
    y_list = [1053, 100, 184, 472, 646, 0]
    dur_list = [1, 1, 1, 0, 0, 0]
    pause_list = [3] * 6

    for i in range( len( x_list ) ):
        pyautoguiMoveClickSleep( x_list[i], y_list[i], dur_list[i], pause_list[i] )

    fp = open( filelocation, "r+" )
    link = fp.readline()

    x_list = [701, 1026, 1160, 1129, 1179, 617, 715, 1322, 1322, 1913]
    y_list = [1049, 99, 569, 601, 727, 815, 814, 619, 619, 0]
    dur_list = [1] * 10
    pause_list = [5] * 6 + [10] * 2 + [20, 0]
    x10=x_list[9]
    y10=y_list[9]

    for i in range( len( x_list ) ):
        if i == 9:
            continue
        if i != 5:
            pyautoguiMoveClickSleep( x_list[i], y_list[i], dur_list[i], pause_list[i] )
            continue
        pyautoguiMoveTypeSleep( x_list[i], y_list[i], dur_list[i], pause_list[i], link )

    im1 = pyautogui.screenshot( "ss1.png" )

    img1 = cv2.imread( 'ss1.png' )

    crop1 = img1[280:911, 1520:1900]

    cv2.imwrite( "ss1.png", crop1 )

    # the image processing algorithm works only of for the first 40 minutes of the lecture
    while clock() != 40:
        sleep( 200 )
        im2 = pyautogui.screenshot( "ss2.png" )
        img2 = cv2.imread( 'ss2.png' )
        crop2 = img2[280:911, 1520:1900]
        cv2.imwrite( "ss2.png", crop2 )
        try:
            if returnComparison( "ss1.png", "ss2.png", 0 ) > 5:
                a1, b1 = returnMostCommonWord( "ss2.png" )
                if b1 > 3:
                    # specific locations w.r.t the chat box in google meet
                    pyautogui.moveTo( x11, y11, duration=1 )
                    pyautogui.click()
                    sleep( 2 )
                    pyautogui.moveTo( x12, y12, duration=1 )
                    pyautogui.click()
                    pyautogui.typewrite( a1, 1 )
                    pyautogui.moveTo( x13, y13, duration=1 )
                    pyautogui.click()
                    sleep( 2 )
            else:
                print( "nothing new here" )
        except:
            print( "error" )
        cv2.imwrite( "ss1.png", crop2 )
        sleep( 20 )
    r = sr.Recognizer()

    while clock() != 60:
        # Exception handling at the runtime
        try:
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                # wait for a second to let the recognizer adjust the energy threshold based on the surrounding noise level
                r.adjust_for_ambient_noise( source2, duration=0.2 )
                # listens for the user's input
                audio2 = r.listen( source2, phrase_time_limit=5 )
                # Using google to recognize audio
                MyText = r.recognize_google( audio2, language='en-IN' )
                MyText = MyText.lower()
                print( "Did you say " + MyText )
                # google didnt get my name right since im indian, had to improvise xD
                # TODO: MAKE THESE POSSIBLE TEXTS TO CHECK AS A GLOBAL LIST
                if (MyText.find( "sujay" ) != -1 or MyText.find( "today" ) != -1 or MyText.find(
                        "tujhe" ) != -1 or MyText.find( "sujoy" ) != -1 or MyText.find( "sachai" ) != -1 or MyText.find(
                    "suji" ) != -1):
                    answerAttendance()
                # 174 is my roll number
                # Todo: Make all these possible text as global variables
                if (MyText.find( "one seventy four" ) != -1 or MyText.find( "74" ) != -1 or MyText.find(
                        "174" ) != -1 or MyText.find( "7474" ) != -1):
                    answerAttendance()

        except sr.RequestError as e:
            print( "Could not request results; {0}".format( e ) )
        except sr.UnknownValueError:
            print( " " )

    print( "exited loop succesfully" )
    sleep( 10 )

    # moves to "X" on the top right corner to close chrome
    pyautogui.moveTo( x10, y10, duration=1 )

    pyautogui.click()

    fp.close()
    # removes file so that i can download it again in the same location
    os.remove( filelocation )

    print( "File Removed!" )
