#!/usr/bin/env python3

"""
text-to-speech program which will take an entered text and output speech
"""

from gtts import gTTS
import os
import rospy
from std_msgs.msg import String

# rospy.init_node("respond")


class respond():

    def __init__(self):
        self.language = 'en'
        self.speak_sub = rospy.Subscriber("/speak", String, self.speak_cb)
        self.result = ""
    
    def speak_cb(self, msg):
        self.result = msg.data
    
    def speak(self):
        print("Going to say: {}".format(self.result))
        speech = gTTS(text= self.result, lang=self.language, slow=False)
  
        # Saving the converted audio in a mp3 file named
        speech.save("speak.mp3")
        
        # Playing the converted file
        os.system("mpg123 -q speak.mp3")