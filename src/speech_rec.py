#!/usr/bin/env python3

"""
speech recognition which will listen to the user until the keywords "what do you think?" are said
the text will then be processed by the gpt class
"""

import speech_recognition as sr
import rospy
from std_msgs.msg import String

# rospy.init_node("speech_rec")

class srec():

    def __init__(self):
        self.r = sr.Recognizer()
        self.r.dynamic_energy_threshold = False
        self.r.energy_threshold = 400
        # self.keyphrase = "what do you think"
        self.end_session = ["shutdown", "shut down", "shot down"]
        self.command_pub = rospy.Publisher("/command", String, queue_size=1)

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


        while not result: 
            with sr.Microphone() as source:
                print("listening...")
                audio = self.r.listen(source)

            try:
                
                result = self.r.recognize_whisper(audio)
                result = result.lower()
                # total_result += " " + result

                if any(end in result for end in self.end_session):
                    return False
                
                print("RESULT: ", result)

                if result: 
                    print("sending the result")
                    self.command_pub.publish(result)

                return result

                print("TOTAL RESULT: ", total_result)
            except sr.UnknownValueError: 
                print("could not understand...")
            except sr.RequestError as e:  
                print("whisper error; {0}".format(e))

        # return total_result
        