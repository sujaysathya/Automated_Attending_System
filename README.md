-># THE BUNK BOT<-
The bunk bot is built on python and its main purpose is to attend your online classes _for you_.<br />
This bot gets the meeting ID of your meeting from Google Docs (note that you need a friend to upload this for you) and opens Google Meet and logs in on your behalf.<br />
It can use both speech recognition and image processing techniques to interact with other people in the meeting.<br />
Once the meeting is done, it closes the Google Chrome page and this process continues every time you have an online class to attend <br />
Speech recognition is used to identify whether your enrollment number is being called out during attendance and the bot automatically types "present" in the chatbox<br />
Image processing is used to convert all the messages in the chatbox into an array of strings and uses some string manipulation techniques to find the most common phrase most of the students said and type it in the chat box. For example, if 5 kids said the answer was "11.5", the bot will type this answer in the chatbox and send it.<br />

Libraries used:<br />
1)Image:
Used for image processing.<br /> View the documentation [here.](https://pillow.readthedocs.io/en/stable/)
<br />
2)Winsound:
Can be used for playing a pre-recorded voice note of yourself saying "present". In this project, it has been used for signalling purposes.<br />
View the documentation [here.](https://docs.python.org/3.1/library/winsound.html)
3)Pyautogui:
Simulates the mouse and keyboard.<br />
View the documentation [here.](https://pyautogui.readthedocs.io/en/latest/)
<br />
4)Pytesseract:
Converts images to text.<br />
View the documentation [here.](https://pypi.org/project/pytesseract/)
<br />
5)Re:
Regular expressions for NLP<br />
View the documentation [here.](https://docs.python.org/3/library/re.html)
<br />
6)Cv2:
Used for image processing.<br />
View the documentation [here.](https://opencv-python-tutroals.readthedocs.io/en/latest/)
<br />
7)Datetime:
Used to time the speech recognition and the image processing algorithms and give them specific times to run.<br />
View the documentation [here.](https://docs.python.org/3/library/datetime.html)
<br />
8)speech_recognition:
Used for speech to text conversion.<br />
View the documentation [here.](https://pypi.org/project/SpeechRecognition/)
<br />
9)PyAudio:
Used to access the microphone.<br />
View the documentation [here.](https://people.csail.mit.edu/hubert/pyaudio/docs/)
<br />

Places to improve:<br />
Currently planning on making a chat bot which can hopefully have full fleged converstations.<br />
Please contribute and make this better lads.<br />

<h3>PLEASE NOTE:</h3>
For legal reasons,<br>
This bot was purely made for eductional purposes only and is meant as a fun way to learn and implement the libraries/packages mentioned above. <br>
This bot is not meant to be used in any malicious way and we are not responsible for anyone actually using this bot to wrongfully attend online classes on his/her/their behalf.



[![HitCount](http://hits.dwyl.com/sujaysathya/bunk_bot.svg)](http://hits.dwyl.com/sujaysathya/bunk_bot)

