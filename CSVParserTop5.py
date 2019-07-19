#!/usr/bin/python

import sys
import os

top5 = 5
def custom_sort(line):
    # print(line.split(',')[2])
    return line.split(',')[2]

def printLines(lines):
    lines.sort(key=custom_sort)
    for line in lines:
        print(line)

def filter(dict):
    keys = dict.keys()
    validDataCount = 0
    count1 = 0 # 0 ~ 10
    count2 = 0 # 10 ~ 50
    count3 = 0 # 50 ~ 100
    count4 = 0 # > 100

    macDict = {}
    for key in keys:
        lines = dict[key]
        count = len(lines)
        macDict[count] = lines[0].split(',')[0]
            # print('count=', count, ' ', lines[0].split(',')[0])
        # if count > 500:
        #     printLines(lines)
        # if lines[0].split(',')[0] == '00:42:79:C4:77:67':
        #     printLines(lines)

        if count < 10:
            count1 += 1
            continue
        if count < 50:
            count2 += 1
            continue
        if count < 100:
            count3 += 1
            continue
        if count > 100:
            count4 += 1
            continue

    # s = SortedDict(macDict)
    sortedKey = sorted(macDict.keys(), reverse=True)
    i = 0
    for k in sortedKey:
        print('count=', k, macDict[k])
        if i >= top5:
            break
        i += 1

    print('0 ~ 10   ', count1)
    print('10 ~ 50  ', count2)
    print('50 ~ 100 ', count3)
    print('> 100    ', count4)
    print('all      ', count1 + count2 + count3 + count4)


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
        macAddress = line[line.split(',')[1]]
        if macAddress not in dict:
            dict[macAddress] = []
        dict[macAddress].append(line)

    file.close()
    filter(dict)
    #print(dict)

def main():
    # if len(sys.argv) <= 1:
    #     print("Usage: python ", os.path.basename(__file__), " path_to_csv")
    #     exit(-1)

    csvFile = '/Users/sunnysun/Desktop/1.csv'
    print('going to parse ', csvFile)
    parse(csvFile)

if __name__ == '__main__':
    main()
