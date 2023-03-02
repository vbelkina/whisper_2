#!/usr/bin/env python3

"""
speech recognition which will listen to the user until the keywords "what do you think?" are said
the text will then be processed by the gpt class
"""

import speech_recognition as sr

class srec():

    def __init__(self):
        self.r = sr.Recognizer()
        self.r.dynamic_energy_threshold = False
        self.r.energy_threshold = 400
        self.wake_word = "wis-glo"
        self.calibrate_mic()
        
    def calibrate_mic(self):
        """
        calibrate the mic with some ambient noise
        """
        with sr.Microphone() as source:  
            print("Please wait. Calibrating microphone...")  
            # listen for 5 seconds and create the ambient noise energy level  
            self.r.adjust_for_ambient_noise(source, duration=5)  

    def listen(self):
        """
        listen to the user until the keywords "what do you think" are said
        """
        total_result = ""
        result = ""

        while self.keyphrase not in result: 
            with sr.Microphone() as source:
                print("listening...")
                audio = self.r.listen(source)

            try: 
                result = self.r.recognize_google(audio)
                # result = result.lower()
                total_result += " " + result

                if any(end in result for end in self.end_session):
                    return False

                print("RESULT: ", result)
                print("TOTAL RESULT: ", total_result)
            except sr.UnknownValueError: 
                print("could not understand...")
            except sr.RequestError as e:  
                print("whisper error; {0}".format(e))

        return total_result
        