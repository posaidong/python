#!/usr/bin/python

import sys
import os

def custom_sort(line):
    return line[line.rindex(',') + 1 :]

def printLines(lines):
    lines.sort(key=custom_sort)
    for line in lines:
        print(line)

def filter(dict):
    keys = dict.keys()
    validDataCount = 0
    for key in keys:
        lines = dict[key]
        count = len(lines)
        appPlatform = lines[0].split(',')[41]
        if count < 50 and appPlatform == 'iOS':
            print(key, ' ', count, ' ', appPlatform)
            validDataCount += 1
            #printLines(lines)

    print('validDataCount=', validDataCount)


# macAddress	productId	colorId	productName	colorName	firmwareVersion	appVersion	jblConnect	durationJBLConnect	criticalTemperature	powerBank	playtime	playtimeInBattery	chargingTime	powerONCount	durationPowerONOFF	speakerphone	eqMode	playPause	jblConnectMaster	lightT1	lightT2	lightT3	lightT4	lightT5	lightT6	lightT7	lightT8	lightT9	lightT10	stereo	party	single	appToneToggle	appMFBMode	appHFPToggle	appEQMode	otaTriggered	otaSuccessful	otaUnsuccessful	otaDuration	appPlatform	appPlatVer	mobDevBrand	mobModel	appVolume	appDurationJBLConnect	appLightT1	appLightT2	appLightT3	appLightT4	appLightT5	appLightT6	appLightT7	appLightT8	appLightT9	appLightT10	currenttimestamp
def parse(csvFile):
    file = open(csvFile, 'r')
    line = file.readline()
    title = line

    dict = {}
    while True:
        line = file.readline()
        if not line:
            break
        macAddress = line[0:line.index(',')]
        if macAddress not in dict:
            dict[macAddress] = []
        dict[macAddress].append(line)

    file.close()
    filter(dict)
    #print(dict)

def main():
    if len(sys.argv) <= 1:
        print("Usage: python ", os.path.basename(__file__), " path_to_csv")
        exit(-1)

    csvFile = sys.argv[1]
    print('going to parse ', csvFile)
    parse(csvFile)

if __name__ == '__main__':
    main()
