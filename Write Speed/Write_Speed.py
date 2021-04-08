from datetime import *
import random
import time



text_list = ["Global AI Hub","Build","Function","Computer","Machine Learning","Student","Database","Software","Programmer","Python","Java","Tensorflow",
             "Interface","Compile","Loops"]
i = 1

before = datetime.now()
while i <= 10:
    counter = i
    a = random.choice(text_list)
    print("Please type: {}".format(a))
    text = str(input(": "))
    if text.lower() == a.lower():
        i += 1
        print("****"+ str(counter) +"****")
    elif text != a.lower():
        print("You failed.")
        i = 1

    if i == 11:
        after = datetime.now()
        speed = after - before
        seconds = speed.total_seconds()
        letter_per_second = round(len(text) / seconds, 1)
    
        print("You won!")
        print("Your score is: {} seconds.".format(seconds))
        print("{} letters per second.".format(letter_per_second))
        print("Restarting")
        print("\n"
              "\n"
              "\n"
              "\n")
        time.sleep(2)
        i = 1
