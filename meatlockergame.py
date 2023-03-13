#this is the game I might write to be used in teh discord server. Nadia sabe.

#DEVNOTE: TEMPRATURES ARE IN (aproximate) DEGREES >>RANKINE<< (not Fahrenheit)
def intro():
    #print intro text
    print("A hiss, a click, and the door opens. Fingers of mist curl around your feet as you gaze into the frigid darkness.")
    print("welcome to:")
    print(" _______  __   __  _______                                                     \n|       ||  | |  ||       |                                                    \n|_     _||  |_|  ||    ___|                                                    \n  |   |  |       ||   |___                                                     \n  |   |  |       ||    ___|                                                    \n  |   |  |   _   ||   |___                                                     \n  |___|  |__| |__||_______|                                                    \n               _______  ______    _______  _______  _______  _______  ______   \n              |       ||    _ |  |       ||       ||       ||       ||    _ |  \n              |    ___||   | ||  |    ___||    ___||____   ||    ___||   | ||  \n              |   |___ |   |_||_ |   |___ |   |___  ____|  ||   |___ |   |_||_ \n              |    ___||    __  ||    ___||    ___|| ______||    ___||    __  |\n              |   |    |   |  | ||   |___ |   |___ | |_____ |   |___ |   |  | |\n              |___|    |___|  |_||_______||_______||_______||_______||___|  |_|")
    return 

def RtoF(oldtemp):
    return oldtemp + 460
def FtoR(oldtemp):
    return oldtemp - 460


#inventory variable
inventory = []
#Fear variable. Fear effects what options you have.
Fear = 0
#internal temprature variable. You can only get so cold
IntTemp = 558
#external temprature variable. Dicides weather you get cold or not.
temp = 497
#cold resistance varable. The lower it is, the faster you get cold
coldRes = 0

def changeTemp():
    change = 0
    global IntTemp
    global temp
    global coldRes
    #calculates change in temprature

    #if the external tempreature is bigger than Internal temprature then...
    if temp >= IntTemp:
        #increase internal temprature by: external temprature/10 OR 5, whichever is greater
        if temp/10 > 5:
           change += temp/10
        else:
           change += 5
    #if the external temprature is less than Internal temprature then...
    if temp < IntTemp:
        #decrease internal temprature by: external temprature/20 OR 5, whichever is smaller
        if temp/10 < 1:
            change -= temp/10
        else:
            change -= 1

    #heat resistance calculation
    if change < 0 and coldRes > 0:
        change = change/coldRes
    
    #im rounding
    change = round(change, 1)
    #actually change the temprature
    IntTemp += change


#DEBUG--DEBUG--DEBUG
i = 0

while i < 5:
    changeTemp()
    print(IntTemp)
    i += 1
