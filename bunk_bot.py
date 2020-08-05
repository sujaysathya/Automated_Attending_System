import os
from time import sleep, time
import winsound
import cv2
import sys
import pyautogui
import speech_recognition as sr
import pytesseract
from HelperFunctions import returnComparatorList, most_frequent, pyautoguiMoveClickSleep, pyautoguiMoveTypeSleep
from HelperFunctions import returnMostCommonWord, returnComparison, returnStrAndRegexList
# theres a "tesseract.exe" file you need to download if you use this on windows
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Retrieving the link from the google docs file

# PLEASE Edit these Global variables as necessary
filelocation = "C:\\Users\\sujay sathya\\Downloads\\zm.txt"
x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6=690,1053,847,100,108,184,230,472,484,646,1917,0#download .txt file from google docs
x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,x13,y13,x14,y14,x15,y15,x16,y16=701,1049,1026,99,1160,569,1129,601,1179,727,617,815,715,814,1322,619,1322,619,1913,0#open google meet
x17, y17, x18, y18, x19, y19 = 1625, 156, 1694, 976, 1872, 985#cordinates to type on the chat box



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
    pyautogui.moveTo( x17, y17, duration=1 )
    pyautogui.click()
    sleep( 2 )
    pyautogui.moveTo( x18, y18, duration=1 )
    pyautogui.click()
    pyautogui.typewrite( "present sir", 1 )
    pyautogui.moveTo( x19, y19, duration=1 )
    pyautogui.click()
    sleep( 2 )


if __name__ == "__main__":

    
    pyautogui.moveTo(x1,y1, duration=1)
    pyautogui.click()
    sleep(10)
    pyautogui.moveTo(x2,y2, duration=1)
    pyautogui.click()
    sleep(10)
    pyautogui.moveTo(x3,y3, duration=1)
    pyautogui.click()
    sleep(10)
    pyautogui.moveTo(x4,y4, duration=0)
    pyautogui.click()
    sleep(10)
    pyautogui.moveTo(x5,y5, duration=0)
    pyautogui.click()
    sleep(10)
    pyautogui.moveTo(x6,y6, duration=0)
    pyautogui.click()
    
    
    
    fp = open(filelocation,"r+")
    link=fp.readline()
    pyautogui.moveTo(x7,y7, duration=1)
    pyautogui.click()
    sleep(10)
    pyautogui.moveTo(x8,y8, duration=1)
    pyautogui.click()
    sleep(10)
    pyautogui.moveTo(x9,y9, duration=1),
    pyautogui.click()
    sleep(10)
    pyautogui.moveTo(x10,y10, duration=1)
    pyautogui.typewrite(link,0)
    sleep(10)
    pyautogui.moveTo(x11,y11, duration=1)
    pyautogui.click()
    sleep(10)
    pyautogui.moveTo(x12,y12, duration=1)
    pyautogui.click()
    sleep(10)
    pyautogui.moveTo(x13,y13, duration=1)
    pyautogui.click()
    sleep(10)
    pyautogui.moveTo(x14,y14, duration=1)
    pyautogui.click()
    sleep(10)
    pyautogui.moveTo(x15,y15, duration=1)
    pyautogui.click()
    sleep(10) 
    sleep(10)
    winsound.PlaySound("sound.wav", winsound.SND_ASYNC | winsound.SND_ALIAS ) 
    im1 = pyautogui.screenshot("ss1.png")
    img1 = cv2.imread('ss1.png')
    crop1 =img1[280:911,1520:1900]
    cv2.imwrite("ss1.png",crop1)

    while(clock()!=40):
        sleep(20)
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC | winsound.SND_ALIAS ) 
        im2 = pyautogui.screenshot("ss2.png")
        img2 = cv2.imread('ss2.png')
        crop2 =img2[280:911,1520:1900]
        cv2.imwrite("ss2.png",crop2)
        try:
            if(returnComparison("ss1.png", "ss2.png",1)>=5):

                
                a1,b1=returnMostCommonWord("ss2.png")
                print(a1)
                print(b1)
                if(b1>=3):
                    pyautogui.moveTo(x17,y17, duration=1)
                    pyautogui.click()
                    sleep(2)
                    pyautogui.moveTo(x18,y18, duration=1)
                    pyautogui.click()
                    pyautogui.typewrite(a1,1)
                    pyautogui.moveTo(x19,y19, duration=1)
                    pyautogui.click()
                    sleep(2)
            else:
                print("nothing new here")
        except:
            print(sys.exc_info())
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
                if(MyText.find("sujay")!=-1 or MyText.find("today")!=-1 or MyText.find("tujhe")!=-1 or MyText.find("sujoy")!=-1 or MyText.find("sachai")!=-1 or MyText.find("suji")!=-1):
                  #change the strings from sujay to your name and like wise for any pronounciation of your name 
                    answerAttendance()
                
                if(MyText.find("one seventy four")!=-1 or MyText.find("74")!=-1 or  MyText.find("174")!=-1 or  MyText.find("7474")!=-1):
                    #change the strings from one seventy four to your roll number
                    x11,y11,x12,y12,x13,y13=1625,156,1694,976,1872,985
                    answerAttendance()   
           
              
        except sr.RequestError as e: 
            print("Could not request results; {0}".format(e)) 
          
        except sr.UnknownValueError: 
            print(" ")  
    print("exited loop succesfully")   
    sleep(10)
    pyautogui.moveTo(x16,y16, duration=1)
    pyautogui.click()
    fp.close()
    os.remove(filelocation)
    print("File Removed!")

