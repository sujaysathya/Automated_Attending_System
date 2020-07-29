THE BUNK BOT
The bunk bot is built on python and its main purpose is to attend your online class for you.
This bot gets the meeting id of your meeting from google docs(you need a friend to upload this for you) and opens google meet and logs in on your behalf.
It can use both speech recognition and image processing techniques to interact with other people in the meeting.
Once the meeting is done, it closes the google chrome page and this process continues every time you have an online class to attend 
Speech recognition is used to identify whether your enrollment number is being called out during attendance and the bot automatically types "present" in the chatbox
Image processing is used to convert all the messages in the chatbox into an array of strings and uses some rudimentary NLP techniques to prepare a suitable reply based on the same.

Libraries used:
1)Image:
used for image processing
2)Winsound:
can be used for playing a pre-recorded voice note of yourself saying "present". In this project, it has been used for signalling purposes
3)Pyautogui:
Simulates the mouse and keyboard
4)Pytesseract:
converts images to text
5)re
regular expressions for NLP
6)cv2
used for image processing
7)Datetime
used to time the speech recognition and the image processing algorithms and give them specific times to run 
8)speech_recognition:
used for speech to text conversion
9)py audio:
used to access the microphone
