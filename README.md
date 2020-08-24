<h2 align = 'center'>THE BUNK BOT</h2>

[![HitCount](http://hits.dwyl.com/sujaysathya/bunk_bot.svg?style=flat)](http://hits.dwyl.com/sujaysathya/bunk_bot)
![Python 3.8.5](https://img.shields.io/badge/Python-3.8.5-blue?style=flat&logo=python)
[![GitHub stars](https://img.shields.io/github/stars/sujaysathya/bunk_bot?color=green)](https://github.com/sujaysathya/bunk_bot/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/sujaysathya/bunk_bot?color=green)](https://github.com/sujaysathya/bunk_bot/network)
[![GitHub issues](https://img.shields.io/github/issues/sujaysathya/bunk_bot)](https://github.com/sujaysathya/bunk_bot/issues)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?)](https://github.com/sujaysathya/bunk_bot/issues)


Watch our YouTube tutorial on how to use this [here!](https://www.youtube.com/watch?v=fKa-_8R9auM)
<p>The <b><i>Bunk Bot</i></b> is built on Python and its main purpose is to attend your online meetings/classes <i>for you</i>.
 
This bot gets the meeting ID of your meeting from Google Docs (note: your friend can upload this for you if you can't) and opens Google Meet and logs in on your behalf.

It can use both Speech Recognition and Image Processing techniques to interact with other people in the meeting.

Once the meeting is done, it closes the Google Chrome page and this process continues every time you have an online class to attend.

<i><b>Speech Recognition</b></i> is used to identify whether your enrollment number is being called out during attendance and the bot automatically types "present" in the chatbox.

<i><b>Image Processing</b></i> is used to convert all the messages in the chatbox into an array of strings and uses some string manipulation techniques to find the most common phrase most of the students said and type it in the chat box. For example, if 5 people said the answer was "11.5", the bot will type "11.5" in the chatbox and send it.

</p>

Libraries used:
1) <b>Image:</b>
Used for image processing.
View the documentation [here.](https://pillow.readthedocs.io/en/stable/)

2) <b>WinSound:</b>
Can be used for playing a pre-recorded voice note of yourself saying "present". In this project, it has been used for signalling purposes.
View the documentation [here.](https://docs.python.org/3.1/library/winsound.html)

3) <b>PyAutoGUI:</b>
Simulates the mouse and keyboard.
View the documentation [here.](https://pyautogui.readthedocs.io/en/latest/)

4) <b>PyTesseract:</b>
Converts images to text.
View the documentation [here.](https://pypi.org/project/pytesseract/)

5) <b>RE:</b>
Regular expressions for NLP.
View the documentation [here.](https://docs.python.org/3/library/re.html)

6) <b>Cv2:</b>
Used for image processing.
View the documentation [here.](https://opencv-python-tutroals.readthedocs.io/en/latest/)

7) <b>DateTime:</b>
Used to time the speech recognition and the image processing algorithms and give them specific times to run
View the documentation [here.](https://docs.python.org/3/library/datetime.html)

8) <b>speech_recognition:</b>
Used for speech to text conversion. 
View the documentation [here.](https://pypi.org/project/SpeechRecognition/)

9) <b>PyAudio:</b>
Used to access the microphone.
View the documentation [here.](https://people.csail.mit.edu/hubert/pyaudio/docs/)
#### Compatibility:

Changing the coordinates in PyAutoGUI is more than enough to implement this code on Google Meet, Zoom Meetings, Microsoft Teams or any other software you use to attend class.<br>


#### CHANGES YOU HAVE TO MAKE:

<p>A small amount of the code you see in this repository is hardcoded w.r.t to my computer.
Changes that you have to make to implement this on your computer are:<p\>

1) Change all the coordinates that PyAutoGUI uses. Refer to `coordinate_finder.py` to find the coordinates which are suitable for you (if you didn't understand any of this, please read the PyAutoGUI documentation).<br>
2) Change all the file paths.<br>
3) Change the size of the crop in `crop=img1[280:911,1520:1900]` to `crop=img1[y1:y2,x1:x2]` where `x1`, `x2`, `y1` and `y2` are coordinates of the chatbox in the online classroom software (i.e Google Meet/ Zoom etc.)<br>

These changes can be made in the global variables that is mentioned in the bunk_bot.py file. Can be found in the 15th line.

#### Fixes and Patches:
1) An unknown exception thrown during image processing has been handled.<br>  
2) Circular import error has been fixed<br>
3) Test files to check the working of the PyTesseract and Speech Recognition Libraries have been added to the folder Test Files. Use these to verify that you've downloaded them and that they're working.<br>

#### Places to improve:
Currently planning on making a ChatBot which can hopefully have full fleged conversations.\
You can provide your suggestions on this [here.](https://github.com/sujaysathya/bunk_bot/issues/5)\
Please contribute and make this better lads.

<h3>PLEASE NOTE:</h3>
<p>For legal reasons,<br>
This bot was purely made for <b><i>educational</i></b> purposes only and is meant as a fun way to learn and implement the libraries/packages mentioned above. <br>
This bot is not meant to be used in any malicious way and we are not responsible for anyone actually using this bot to wrongfully attend online classes on his/her/their behalf.</p>




