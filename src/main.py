#!/usr/bin/env python3

import respond, speech_rec
import rospy
from std_msgs.msg import Bool

rospy.init_node("main")


finished = False

def finished_cb(msg):
    finished = msg.data 

if __name__ == '__main__':

    finished_sub = rospy.Subscriber("/commnand/finished", Bool, finished_cb)
    sr = speech_rec.srec()
    response = respond.respond()

    user_input = ""

    while(1):
        user_input = sr.listen()

        if user_input and finished: 
            finished = False
        elif not finished: 
            continue
        else:
            response.speak("Okay, thank you for your time. Have a nice day!")
            break

    

    
