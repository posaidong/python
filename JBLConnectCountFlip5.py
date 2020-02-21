#!/usr/bin/python

import sys
import os

def parse(csvFile):
    file = open(csvFile, 'r')
    line = file.readline()

    macDict = dict()
    playtimeAllDevices = 0
    durationJBLConnectAllDevices = 0
    usedJBLConnectMacs = set()
    while True:
        line = file.readline()
        if not line:
            break
        params = line.split(',')
        macAddress = params[0].replace('"', '')
        appVersion = params[6].replace('"', '')
        jblConnect = 0
        durationJBLConnect = 0
        speakerphone = 0
        playtime = 0
        try:
            jblConnect = int(params[7].replace('"', ''))
            speakerphone = int(params[16].replace('"', ''))  # speakerphone times, not duration,   Flip 5 no this feature
            durationJBLConnect = int(params[8].replace('"', ''))
            playtime = int(params[11].replace('"', ''))
        except:
            continue
        currenttimestamp = params[len(params) - 1].replace('"', '')
        currenttimestamp = currenttimestamp.replace('T', ' ')
        currenttimestamp = currenttimestamp.replace('Z', '')
        # mobModel = params[44].replace('"', '')

        if macAddress not in macDict:
            macDict[macAddress] = [0,0,0]
        macDict[macAddress][0] += jblConnect     #times
        macDict[macAddress][1] += speakerphone   #times
        macDict[macAddress][2] += playtime       #duration

        playtimeAllDevices += playtime
        durationJBLConnectAllDevices += durationJBLConnect

        if (durationJBLConnect > 0):
            usedJBLConnectMacs.add(macAddress)

    file.close()

    macAddressTotal = len(macDict.keys())

    print('macAddressTotal ', macAddressTotal)
    print('avg playtime for all of devices', int(playtimeAllDevices / macAddressTotal), ',playtimeAllDevices=', playtimeAllDevices, ',macAddressTotal=',macAddressTotal)
    print('avg durationJBLConnect for all of devices', int(durationJBLConnectAllDevices / macAddressTotal), ',durationJBLConnectAllDevices=',
          durationJBLConnectAllDevices, ',macAddressTotal=', macAddressTotal)
    print('usage percentage of JBLConnect is', '{:.1%}'.format(len(usedJBLConnectMacs)/macAddressTotal))


def main():
    # if len(sys.argv) <= 1:
    #     print("Usage: python ", os.path.basename(__file__), " path_to_csv")
    #     exit(-1)

    csvFile = '/Users/sunnysun/Desktop/realtime_tblapp_data_201908011455.csv'
    print('going to parse ', csvFile)
    parse(csvFile)

if __name__ == '__main__':
    main()
