                                                              THE BUNK BOT 
The bunk bot is built on python and its main purpose is to attend your online class for you.<br />
This bot gets the meeting id of your meeting from google docs(you need a friend to upload this for you) and opens google meet and logs in on your behalf.<br />
It can use both speech recognition and image processing techniques to interact with other people in the meeting.<br />
Once the meeting is done, it closes the google chrome page and this process continues every time you have an online class to attend <br />
Speech recognition is used to identify whether your enrollment number is being called out during attendance and the bot automatically types "present" in the chatbox<br />
Image processing is used to convert all the messages in the chatbox into an array of strings and uses some string manipulation techniques to find the most common phrase most of the students said and type it in the chat box. For expample if 5 kids said the asnswer was "11.5", the bot will type this answer on the chatbox<br />

Libraries used:<br />
1)Image:
used for image processing<br />
https://pillow.readthedocs.io/en/stable/<br />
2)Winsound:
can be used for playing a pre-recorded voice note of yourself saying "present". In this project, it has been used for signalling purposes<br />
https://docs.python.org/3.1/library/winsound.html<br />
3)Pyautogui:
Simulates the mouse and keyboard<br />
https://pyautogui.readthedocs.io/en/latest/<br />
4)Pytesseract:
converts images to text<br />
https://pypi.org/project/pytesseract/<br />
5)Re:
regular expressions for NLP<br />
https://docs.python.org/3/library/re.html<br />
6)Cv2:
used for image processing<br />
https://opencv-python-tutroals.readthedocs.io/en/latest/<br />
7)Datetime:
used to time the speech recognition and the image processing algorithms and give them specific times to run <br />
https://docs.python.org/3/library/datetime.html<br />
8)Speech_recognition:
used for speech to text conversion<br />
https://pypi.org/project/SpeechRecognition/<br />
9)Py audio:
used to access the microphone<br />
https://people.csail.mit.edu/hubert/pyaudio/docs/<br />

Places to improve:<br />
Currently planning on making a chat bot which can hopefully have full fleged converstations.<br />
Please contribute and make this better lads.<br />

[![HitCount](http://hits.dwyl.com/sujaysathya/bunk_bot.svg)](http://hits.dwyl.com/sujaysathya/bunk_bot)

