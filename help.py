import pyautogui
from time import sleep
pyautogui.PAUSE = 1
sleep(5)

#this pyautogui.position() returns the x and y coordinates of the mouse
#one you start the execution of the file, you have 5 seconds to position the mouse on a point who's coordinates you need
#for example: if i place the mouse on top of the google chrome icon in my taskbar,I'll get the coordinates of the icon
x,y=pyautogui.position()
print(x,y)


#pyautogui.moveTo(x,y) is used to move the mouse from any position to the point x,y pyautogui.click() is used to simulate a 
#mouse click over here.
#w.r.t this example, the mouse will move on its own to the google chrome icon and open it
pyautogui.moveTo(x,y)
pyautogui.click()

#repeat this program to find the coordinates of all the places where you'll have to do a mouse click to open an application in the web
