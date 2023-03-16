#this is the game I might write to be used in teh discord server. Nadia sabe.

#DEVNOTE: TEMPRATURES ARE IN (aproximate) DEGREES >>RANKINE<< (not Fahrenheit)
def intro():
    #print intro text
    print("A hiss, a click, and the door opens. Fingers of mist curl around your feet as you gaze into the frigid darkness.")
    print("welcome to:")
    print(" _______  __   __  _______                                                     \n|       ||  | |  ||       |                                                    \n|_     _||  |_|  ||    ___|                                                    \n  |   |  |       ||   |___                                                     \n  |   |  |       ||    ___|                                                    \n  |   |  |   _   ||   |___                                                     \n  |___|  |__| |__||_______|                                                    \n               _______  ______    _______  _______  _______  _______  ______   \n              |       ||    _ |  |       ||       ||       ||       ||    _ |  \n              |    ___||   | ||  |    ___||    ___||____   ||    ___||   | ||  \n              |   |___ |   |_||_ |   |___ |   |___  ____|  ||   |___ |   |_||_ \n              |    ___||    __  ||    ___||    ___|| ______||    ___||    __  |\n              |   |    |   |  | ||   |___ |   |___ | |_____ |   |___ |   |  | |\n              |___|    |___|  |_||_______||_______||_______||_______||___|  |_|")
    return 

#conversion fucntoins because
def RtoF(oldtemp):
    return oldtemp + 460
def FtoR(oldtemp):
    return oldtemp - 460
#prettyfiying

#inventory variable
inventory = []
#Fear variable. Fear effects what options you have.
Fear = 0
#internal temprature variable. You can only get so cold
IntTemp = 558.0
#external temprature variable. Dicides weather you get cold or not.
temp = 497.0
#cold resistance varable. The lower it is, the faster you get cold. I suggest that you make the number nice.
coldRes = 0.0

def changeTemp():
    change = 0
    global IntTemp
    global temp
    global coldRes
    #calculates change in temprature
    #decrease temprature if bodytemp below outside temp
    if IntTemp > temp:
        change += 0.1
    #increase intrnal temprature if bodytemp above outside temp
    if IntTemp < temp:
        change -= 0.1
    #cold resistance variable minimises the amount of heat you loose
    if coldRes != 0:
        change = change/coldRes
    #rounding so that numpers dont look like 0.0000000000000000000000001
    round(change, 3)
    IntTemp -= change


#DEBUG--DEBUG--DEBUG
