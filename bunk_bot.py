import Image
import speech_recognition as sr
import winsound
import pyautogui
import pytesseract
import re
import cv2
from time import sleep
from datetime import datetime

# theres a "tesseract.exe" file you need to download if you use this on windows
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

#The next five lines of code are used to find the time at which the code begings to execute
now1 = datetime.now()
dt_string1 = now1.strftime(" %H %M ")
hour1 =int(dt_string1[1:3])
minn1=int(dt_string1[4:])
a=dt.timedelta(hours=hour1, minutes=minn1)

#The clock function returns the amount of time that had passed since the code had begun execution in minutes
def clock():
    now2 = datetime.now()
    dt_string2 = now2.strftime(" %H %M ")
    hour2 =int(dt_string2[1:3])
    minn2=int(dt_string2[4:])
    b = dt.timedelta(hours=hour2, minutes=minn2)
    c=b-a
    d=str(c)
    e=int(d[2:4])
    return(e)

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


 # returns most frequent element in a list
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


#using the pyautogui library to automate my mouse to download a google docs file that has the link to my online class
#the coordinates given here are strictly w.r.t my computer screen size and where i have placed my icons
#to find your own coordinates, read the pyautogui documentation

x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6=690,1053,847,100,108,184,230,472,484,646,1917,0

#positions the mouse on the google chrome app on the taskbar
pyautogui.moveTo(x1,y1, duration=1)
pyautogui.click()
sleep(3)

#positions the mouse on the bookmark of the google document
pyautogui.moveTo(x2,y2, duration=1)
pyautogui.click()
sleep(3)

#positions the mouse on  "File" in the google docs
pyautogui.moveTo(x3,y3, duration=1)
pyautogui.click()
sleep(3)

#positions the mouse on  "download" after clicking on "File" in  google docs 
pyautogui.moveTo(x4,y4, duration=0)
pyautogui.click()
sleep(3)

#positions the mouse on  "Plain text .txt" after clicking on "download" in  google docs 
pyautogui.moveTo(x5,y5, duration=0)
pyautogui.click()
sleep(3)


#positions the mouse on the "X" on the top right corner of the brower to close it

pyautogui.moveTo(x6,y6, duration=0)
pyautogui.click()

#basically the same but to open google meet and enter a meeting
#please read the pyautogui documentation if you dont understand this code

x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10=701,1049,1026,99,1160,569,1129,601,1179,727,617,815,715,814,1322,619,1322,619,1913,0

#retriving the link from the google docs file
fp = open("C:\\Users\\sujay sathya\\Downloads\\zm.txt","r+")
link=fp.readline()
pyautogui.moveTo(x1,y1, duration=1)
pyautogui.click()
sleep(5)
pyautogui.moveTo(x2,y2, duration=1)
pyautogui.click()
sleep(5)
pyautogui.moveTo(x3,y3, duration=1)
pyautogui.click()
sleep(5)
pyautogui.moveTo(x4,y4, duration=1)
pyautogui.typewrite(link,0)
sleep(5)
pyautogui.moveTo(x5,y5, duration=1)
pyautogui.click()
sleep(5)
pyautogui.moveTo(x6,y6, duration=1)
pyautogui.click()
sleep(5)
pyautogui.moveTo(x7,y7, duration=1)
pyautogui.click()
sleep(10)
pyautogui.moveTo(x8,y8, duration=1)
pyautogui.click()
sleep(10)
pyautogui.moveTo(x9,y9, duration=1)
pyautogui.click()
sleep(10)

#now we have entered a google meeting and opened the chat box


sleep(10)


im1 = pyautogui.screenshot("ss1.png")
img1 = cv2.imread('ss1.png')
crop1 =img1[280:911,1520:1900]
cv2.imwrite("ss1.png",crop1)

# the image processing algorithm works only of for the first 40 minutes of the lecture
while(clock()!=40):
    sleep(20)
    winsound.PlaySound("sound.wav", winsound.SND_ASYNC | winsound.SND_ALIAS ) 
    im2 = pyautogui.screenshot("ss2.png")
    img2 = cv2.imread('ss2.png')
    crop2 =img2[280:911,1520:1900]
    cv2.imwrite("ss2.png",crop2)
    try:
        if(returnComparison("ss1.png", "ss2.png",1)>5):

            
            a1,b1=returnMostCommonWord("ss2.png")
            if(b1>3):
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
