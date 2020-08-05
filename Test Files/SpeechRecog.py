# -*- coding: utf-8 -*-

import speech_recognition as sr
r = sr.Recognizer()
while(1):

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
            MyText =r.recognize_google(audio2,language='en-IN') 
            MyText = MyText.lower() 
            print("Did you say "+MyText) 


    except sr.RequestError as e: 
            print("Could not request results; {0}".format(e)) 

    except sr.UnknownValueError: 
            print(" ")