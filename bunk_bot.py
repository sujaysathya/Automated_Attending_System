from PIL import Image
import speech_recognition as sr
import winsound
import pyautogui
import pytesseract
import re
import cv2

from time import sleep, time
#from datetime import datetime

# theres a "tesseract.exe" file you need to download if you use this on windows
# pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# This is a function that receives strings in the format of "Name HH:MM AM/PM".
# For example, "Roman Atwood 11:52 PM".
# From the above string, the function would return "Roman Atwood" and "11:52 PM"
def getnametime(x):
    matchobj = re.search("(.+)(\d?\d:\d{2}\s*[AP]M)", x)
    return(matchobj.group(1), matchobj.group(2))

# This is a Message class.
# It consists of three attributes.
# strings are all the messages that the particular person has sent.
# name is the name of the person sending the messages
# time is the time at which the messages were sent by the person
class Message:

    def __init__(self, strings):
        self.strings = []
        self.strings.extend(strings)
        self.name, self.time = getnametime(strings[0])
        self.strings.pop(0)
        self.strings = tuple(self.strings)

    # simple function to show the name, time and messages of the object
    def show(self):
        print("Name: " + self.name)
        print("Time: " + self.time)
        print("Messages: ")
        for i in self.strings:
            print(i)
        print('')

    # series of functions to receive name, time, and messages

    def getname(self):
        return(self.name)

    def gettime(self):
        return(self.time)

    def getmessages(self):
        return(self.strings)

# returns most frequent element in a list, along with its frequency.
def most_frequent(List):
    counter = 0
    num = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
    return num,counter

# This function receives a filename of an image as input and returns two lists.
# The first list is called str_list.
# It splits the entire image into a list of lines and spits it out.
# The second list is called regex_flag.
# This list is the same length as str_list.
# It contains flags corresponding to every element of 1.
# If str_list[i] satifies the given regex filter (eg "11:52 AM"), regex_flag[i] is 1.
# otherwise it is 0.
def returnStrAndRegexList(imageName):

    # reading a long string from the image
    strin = pytesseract.image_to_string(Image.open(imageName))

    # splitting that long string into many lines
    str_list = strin.splitlines()

    # removing blank lines from str_list
    for string in str_list:
        if(len(string) == 0):
            str_list.remove(string)

    # initializing regex_flag with 0s
    regex_flag = [0] * len(str_list)

    # going through entire str_list to set regex flags for lines that
    # satisfy the given condition
    for i in range(len(regex_flag)):
        if(re.search("\d?\d:\d{2}\s*[AP]M", str_list[i])):
            regex_flag[i] = 1

    # if regex_flag does not start with 1, ie, the str_list does not start with a timestamp,
    # elements from the beginning of both lists are popped
    # until a 1 is reached.
    while(regex_flag[0] == 0):
        regex_flag.pop(0)
        str_list.pop(0)

    # both lists are returned
    return(str_list, regex_flag)


# returns a nested list of messages in tuples, so they can easily compared in returnComparison
def returnComparatorList(imageName):

    # calls returnStrAndRegexList() to receive str_list and regex_flag for the given image.
    str_list, regex_flag = returnStrAndRegexList(imageName)

    # just a loop to print out regex_flag and str_list to check
    # for i in range(len(str_list)):
    #     print(str(regex_flag[i]) + " " + str_list[i])
    # print('')


    messagesBuffer = []
    comparatorList = []
    messagesBuffer.append(str_list[0])
    for i in range(1, len(str_list)):
        if(regex_flag[i] == 0):
            messagesBuffer.append(str_list[i])
        else:
            comparatorList.append(parseMessageBuffer(messagesBuffer))
            messagesBuffer = []
            messagesBuffer.append(str_list[i])
    comparatorList.append(parseMessageBuffer(messagesBuffer))
    return(comparatorList)

# Takes a message from the buffer and returns a tuple for comparatorList.
def parseMessageBuffer(msgBuffer):
    msgObj = Message(msgBuffer)
    x = []
    x.append(msgObj.getname())
    x.append(msgObj.gettime())
    x.append(msgObj.getmessages())
    return tuple(x)

# This function accepts three parameters -> oldImage, newImage and opt.
# oldImage and newImage are filenames to the older image, and the new image.
#
# The function should return the number of new messages that have appeared in the new image,
# when compared to the old image.
#
# When opt is set to 0, it returns the number of new Message Objects that have been created.
#
# When opt is set to 1, it adds up the total number of new individual messages within
# all the new message objects.
def returnComparison(oldImage, newImage, opt):
    x = returnComparatorList(oldImage)
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

# returns the most common message in the image along with its frequency
def returnMostCommonWord(imageName):
    x = returnComparatorList(imageName)
    listOfWords = []
    for i in x:
        for j in i[2]:
            listOfWords.append(j)
    a1,b1=most_frequent(listOfWords)
    return(a1,b1)

#using the pyautogui library to automate my mouse to download a google docs file that has the link to my online class
#the coordinates given here are strictly w.r.t my computer screen size and where i have placed my icons
#to find your own coordinates, read the pyautogui documentation

#The next five lines of code are used to find the time at which the code begings to execute
a=time()


#The clock function returns the amount of time that had passed since the code had begun execution in minutes
def clock():
    return (time()-a)//60

def pyautoguiMoveClickSleep(x_,y_,dur_,pause_,):
    pyautogui.moveTo(x_,y_, duration=dur_)
    pyautogui.click()
    sleep(pause_)

def pyautoguiMoveTypeSleep(x_,y_,dur_,pause_,link_):
    pyautogui.moveTo(x_,y_, duration=dur_)
    pyautogui.typewrite(link_,0)
    sleep(pause_)

x_list = [690,847,108,230,484,1917]
y_list = [1053,100,184,472,646,0]
dur_list = [1,1,1,0,0,0]
pause_list = [3]*6

for i in range(len(x_list)):
    pyautoguiMoveClickSleep(x_list[i],y_list[i],dur_list[i],pause_list[i])


#retriving the link from the google docs file
fp = open("C:\\Users\\sujay sathya\\Downloads\\zm.txt","r+")
link=fp.readline()

x_list = [701,1026,1160,1129,1179,617,715,1322,1322,1913]
y_list = [1049,99,569,601,727,815,814,619,619,0]
dur_list = [1]*10
pause_list = [5]*6 +[10]*2 + [20,0]

for i in range(len(x_list)):
    if i == 9:
        continue
    if i != 5:
        pyautoguiMoveClickSleep(x_list[i],y_list[i],dur_list[i],pause_list[i])
        continue
    pyautoguiMoveTypeSleep(x_list[i],y_list[i],dur_list[i],pause_list[i],link)





im1 = pyautogui.screenshot("ss1.png")

img1 = cv2.imread('ss1.png')

crop1 =img1[280:911,1520:1900]

cv2.imwrite("ss1.png",crop1)

# the image processing algorithm works only of for the first 40 minutes of the lecture
while(clock()!=40):
    sleep(20)
    im2 = pyautogui.screenshot("ss2.png")
    img2 = cv2.imread('ss2.png')
    crop2 =img2[280:911,1520:1900]
    cv2.imwrite("ss2.png",crop2)
    try:
        if(returnComparison("ss1.png", "ss2.png",1)>5):
            a1,b1=returnMostCommonWord("ss2.png")
            if(b1>3):
                #specific locations w.r.t the chat box in google meet
                x11,y11,x12,y12,x13,y13=1625,156,1694,976,1872,985
                pyautogui.moveTo(x11,y11, duration=1)
                pyautogui.click()
                sleep(2)
                pyautogui.moveTo(x12,y12, duration=1)
                pyautogui.click()
                pyautogui.typewrite(a1,1)
                pyautogui.moveTo(x13,y13, duration=1)
                pyautogui.click()
                sleep(2)
        else:
            print("nothing new here")
    except:
        print("error")
    cv2.imwrite("ss1.png",crop2)
    sleep(20)
r = sr.Recognizer()

while(clock()!=60):
    # Exception handling to handle
    # exceptions at the runtime
    try:
        # use the microphone as source for input.
        with sr.Microphone() as source2:
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)
            #listens for the user's input
            audio2 = r.listen(source2,phrase_time_limit=5)
            # Using ggogle to recognize audio
            MyText = r.recognize_google(audio2,language='en-IN')
            MyText = MyText.lower()
            print("Did you say "+MyText)
            #google didnt get my name right since im indian, had to improvise xD
            if(MyText.find("sujay")!=-1 or MyText.find("today")!=-1 or MyText.find("tujhe")!=-1 or MyText.find("sujoy")!=-1 or MyText.find("sachai")!=-1 or MyText.find("suji")!=-1):
                x11,y11,x12,y12,x13,y13=1625,156,1694,976,1872,985

                pyautogui.moveTo(x11,y11, duration=1)

                pyautogui.click()

                sleep(2)

                pyautogui.moveTo(x12,y12, duration=1)

                pyautogui.click()

                pyautogui.typewrite("present sir",1)

                pyautogui.moveTo(x13,y13, duration=1)

                pyautogui.click()

                sleep(2)

            #174 is my roll number

            if(MyText.find("one seventy four")!=-1 or MyText.find("74")!=-1 or  MyText.find("174")!=-1 or  MyText.find("7474")!=-1):

                x11,y11,x12,y12,x13,y13=1625,156,1694,976,1872,985

                pyautogui.moveTo(x11,y11, duration=1)

                pyautogui.click()

                sleep(2)

                pyautogui.moveTo(x12,y12, duration=1)

                pyautogui.click()

                pyautogui.typewrite("present sir",1)

                pyautogui.moveTo(x13,y13, duration=1)

                pyautogui.click()

                sleep(2)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print(" ")

print("exited loop succesfully")
sleep(10)

#moves to "X" on the top right corner to close chrome
pyautogui.moveTo(x10,y10, duration=1)

pyautogui.click()

fp.close()
#removes file so that i can download it again in the same location
os.remove("C:\\Users\\sujay sathya\\Downloads\\zm.txt")

print("File Removed!")
