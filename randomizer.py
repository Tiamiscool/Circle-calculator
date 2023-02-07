import random
import time
def funct():
    list = ["front kick ", "punch ", "dodge ", "jab ", "round kick ", "hook kick ",
     "right cresent kick " "slide up punch ", "slide up jab ", "stepping front kick ",
      "spinning back kick ", "spinning round kick ", "form ", "puncher ", "3D ",
       "football thrower(extra credit if blue and below) ", "left cresent kick "
         "right elbow ", "left elbow ", "front elbow ", "spinning elbow "
         , "knee ", "jump knee ", "jump front kick ", "jump round kick "
         , "flying sidekick " "pop kick ", "knife hand block ", "inside block ",
         "outside block ", "low block ", "high block ", "superman punch " ]
    for i in range(50):
        print(random.choice(list))
        time.sleep(5)
funct()