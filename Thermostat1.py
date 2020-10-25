import random
import time
import sys
from datetime import datetime

now = datetime.now()

#This will fetch the current time so you can run a programmed thermostat
current_time = int(now.strftime("%H"))
print("Current Time: ", current_time)
#This is the ability to fetch the day also 
current_day = datetime.today().strftime('%A')
print("Current Day: ",current_day)

#The current temperature starts out random right now for the sake of testing the program
current_temp = round(random.uniform(60,80),2)


#The temperature setting is also random for the sake of testing
# temp_set = random.randint(66,74)   





#Here is a timed version using current time


if current_day == "Sunday":
    if current_time > 7 and current_time < 20:
        temp_set = 72
    if current_time > 20 or current_time < 7:
        temp_set = 68

if current_day == "Monday":
    if current_time > 7 and current_time < 9:
        temp_set = 72
    if current_time > 20 or current_time < 7:
        temp_set = 68
if current_day == "Tuesday":
    if current_time > 7 and current_time < 9:
        temp_set = 72
    if current_time > 20 or current_time < 7:
        temp_set = 68
if current_day == "Wednesday":
    if current_time > 7 and current_time < 9:
        temp_set = 72
    if current_time > 20 or current_time < 7:
        temp_set = 68
if current_day == "Thursday":
    if current_time > 7 and current_time < 9:
        temp_set = 72
    if current_time > 20 or current_time < 7:
        temp_set = 68
if current_day == "Friday":
    if current_time > 7 and current_time < 9:
        temp_set = 72
    if current_time > 20 or current_time < 7:
        temp_set = 68

if current_day == "Saturday":
    if current_time > 7 and current_time < 9:
        temp_set = 72
    if current_time > 20 or current_time < 7:
        temp_set = 68


#Printing for sake of testing so you know what the temperature setting is for sor
print("User Temperature Setting: " + str(temp_set))
print("Current Actual Temperature: " + str(current_temp))

#This is so i can stop it from going forever
runcount = 0

#This is sort of the main loop that compares the temperature the user set temperature each time
def CheckTemp():
    global runcount
    runcount += 1
    global temp_set
    global current_temp

    

    if current_temp > temp_set:
        print("Cooling")
        Cool()
        
    if current_temp < temp_set:
        print("Heating")
        Heat()

#This is what happens when the temperature is higher than the setting AKA it's warmer than you want it to be        
def Cool():
    global current_temp
    current_temp = round(random.uniform(current_temp,current_temp - 2),2)
    time.sleep(1)
    print(current_temp)
    run()

#this is what happens when you want it to be warmer
def Heat():
    global current_temp
    current_temp = round(random.uniform(current_temp,current_temp + 2),2)
    time.sleep(1)
    print(current_temp)
    run()

#This determines if it's running, right now it's just set to stop at 25 so it doesn't go forever, this could be an on off switch or maybe times of day even
def run():
    if runcount < 25:
        CheckTemp()
    if runcount == 25:
        sys.exit

    
        


run()