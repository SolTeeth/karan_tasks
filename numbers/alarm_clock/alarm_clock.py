import time
import os
from datetime import datetime


def timer(user_input):

    user_input = user_input.split(':')
    user_input = (element.lstrip('0') if len(element) > 1 else element for element in user_input)
    user_input = tuple(map(lambda x: int(x), user_input))
    time.sleep(user_input[0] * 3600 + user_input[1] * 60 + user_input[2])
    os.system('Z:/python/projects/Projects/numbers/alarm_clock/fairyland.mp3')


if int(input("""What do you want to do?'\n1: Set timer\n2: Set alarm at a certain time\n Type number: """)) == 1:

    user_input = input('Specify the time in format H:M:S of the time you want to wait.\n ex. 1:25:32\n')
    timer(user_input)
else:
    check = True
    while check:
        user_input = input('Specify the time at which you want the alarm to go off in format H:M:S .\n ex. 13:25:32\n')
        user_input = user_input.split(':')
        user_input = (element.lstrip('0') if len(element) > 1 else element for element in user_input)
        user_input = tuple(map(lambda x: int(x), user_input))

        now = (datetime.now().hour, datetime.now().minute, datetime.now().second)
        interval = (user_input[0] * 3600 + user_input[1] * 60 + user_input[2]) - (now[0] * 3600 + now[1] * 60 + now[2])

        if interval >= 0:
            check = False
            time.sleep(interval)
            os.system('Z:/python/projects/Projects/numbers/alarm_clock/fairyland.mp3')
        else:
            print('You entered the time which already passed. Please enter correct time.')
