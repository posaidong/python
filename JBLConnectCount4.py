#!/usr/bin/python

import sys
import os

threshold = ['=1','2-5','6-10', '>10']
jblConnectCnt = [0,0,0,0]   #count for jbl connect based on threshold
speakerphoneCnt = [0,0,0,0] #count for speakphone based on threshold

durationJBLConnectTotal = [0,0,0,0] # total duration for jblconnect based on threshold

speakerphoneTimes = [0,0,0,0] # total times for speakerphone based on threshold
jblConnectTimes =[0,0,0,0] # total jblConnect times based on threshold
playtimeTotal = [0,0,0,0] # total playtime based on threshold



def parse(csvFile):
    file = open(csvFile, 'r')
    line = file.readline()

    macDict = dict()
    playtimeAllDevices = 0
    while True:
        line = file.readline()
        if not line:
            break
        params = line.split(',')
        macAddress = params[1].replace('"', '')
        appVersion = params[6].replace('"', '')
        jblConnect = 0
        durationJBLConnect = 0
        speakerphone = 0
        playtime = 0
        try:
            jblConnect = int(params[7].replace('"', ''))
            speakerphone = int(params[16].replace('"', ''))  # speakerphone times, not duration
            durationJBLConnect = int(params[8].replace('"', ''))
            playtime = int(params[11].replace('"', ''))
        except:
            continue
        currenttimestamp = params[len(params) - 4].replace('"', '')
        currenttimestamp = currenttimestamp.replace('T', ' ')
        currenttimestamp = currenttimestamp.replace('Z', '')
        mobModel = params[44].replace('"', '')

        if macAddress not in macDict:
            macDict[macAddress] = [0,0,0]
        macDict[macAddress][0] += jblConnect     #times
        macDict[macAddress][1] += speakerphone   #times
        macDict[macAddress][2] += playtime       #duration

        playtimeAllDevices += playtime

    file.close()

    jblConnectMacs = dict()
    speakerphoneMacs = dict()
    for i in range(len(durationJBLConnectTotal)):
        jblConnectMacs[i] = set()
        speakerphoneMacs[i] = set()

    for k, v in macDict.items():
        if v[0] > 10: # times of jblconnect
            jblConnectCnt[3] +=1
            jblConnectMacs[3].add(k)
            jblConnectTimes[3] += v[0]
            playtimeTotal[3] += v[2]
        if v[1] > 10:
            speakerphoneCnt[3] +=1
            speakerphoneMacs[3].add(k)

        if v[0] >= 6 and v[0] <= 10:
            jblConnectCnt[2] +=1
            jblConnectMacs[2].add(k)
            jblConnectTimes[2] += v[0]
            playtimeTotal[2] += v[2]
        if v[1] >= 6 and v[1] <=10:
            speakerphoneCnt[2] +=1
            speakerphoneMacs[2].add(k)

        if v[0] >= 2 and v[0] <= 5:
            jblConnectCnt[1] +=1
            jblConnectMacs[1].add(k)
            jblConnectTimes[1] += v[0]
            playtimeTotal[1] += v[2]
        if v[1] >= 2 and v[1] <=5:
            speakerphoneCnt[1] +=1
            speakerphoneMacs[1].add(k)

        if v[0] == 1:
            jblConnectCnt[0] +=1
            jblConnectMacs[0].add(k)
            jblConnectTimes[0] += v[0]
            playtimeTotal[0] += v[2]
        if v[1] == 1:
            speakerphoneCnt[0] +=1
            speakerphoneMacs[0].add(k)

    macAddressTotal = len(macDict.keys())

    print('threshold ', threshold)
    print('jblConnectCnt ', jblConnectCnt, ['{:.1%}'.format(x / macAddressTotal) for x in jblConnectCnt])
    print('speakerphoneCnt ', speakerphoneCnt, ['{:.1%}'.format(x / macAddressTotal) for x in speakerphoneCnt])
    print('avg playtime for all of devices', int(playtimeAllDevices / macAddressTotal), ',playtimeAllDevices=', playtimeAllDevices, ',macAddressTotal=',macAddressTotal)

    parseByMac(csvFile, jblConnectMacs, speakerphoneMacs)


def parseByMac(csvFile, jblConnectMacs, speakerphoneMacs):
    file = open(csvFile, 'r')
    line = file.readline()

    while True:
        line = file.readline()
        if not line:
            break
        params = line.split(',')
        macAddress = params[1].replace('"', '')
        appVersion = params[6].replace('"', '')
        jblConnect = 0
        durationJBLConnect = 0
        speakerphone = 0
        try:
            jblConnect = int(params[7].replace('"', ''))
            speakerphone = int(params[16].replace('"', ''))  # speakerphone
            durationJBLConnect = int(params[8].replace('"', ''))
        except:
            continue
        currenttimestamp = params[len(params) - 4].replace('"', '')
        currenttimestamp = currenttimestamp.replace('T', ' ')
        currenttimestamp = currenttimestamp.replace('Z', '')
        mobModel = params[44].replace('"', '')

        if durationJBLConnect == 0 and speakerphone == 0:
            continue

        for i, v in jblConnectMacs.items():
            if macAddress in v:
                durationJBLConnectTotal[i] += durationJBLConnect

        for i, v in speakerphoneMacs.items():
            if macAddress in v:
                speakerphoneTimes[i] += speakerphone
                break


    file.close()

    durationJBLConnectAvgByDevice = [0,0,0,0]
    timesSpeakerphoneAvgByDevice = [0,0,0,0]
    durationJBLConnectAvgByTime = [0,0,0,0]
    playtimeAvgByDevice = [0,0,0,0]

    for i, v in jblConnectMacs.items():
        durationJBLConnectAvgByDevice[i] = int(durationJBLConnectTotal[i] / len(v))
        durationJBLConnectAvgByTime[i] = int(durationJBLConnectTotal[i] / jblConnectTimes[i])
        playtimeAvgByDevice[i] = int(playtimeTotal[i] / len(v))

    for i, v in speakerphoneMacs.items():
        if(len(v) == 0):
            continue
        timesSpeakerphoneAvgByDevice[i] = int(speakerphoneTimes[i] / len(v))

    print('avg durationJBLConnect by device ', durationJBLConnectAvgByDevice);
    print('avg durationJBLConnect by times  ', durationJBLConnectAvgByTime);
    print('avg timesSpeakerphone by device ', timesSpeakerphoneAvgByDevice);
    print('avg playtime by device', playtimeAvgByDevice)


def main():
    # if len(sys.argv) <= 1:
    #     print("Usage: python ", os.path.basename(__file__), " path_to_csv")
    #     exit(-1)

    csvFile = '/Users/sunnysun/Desktop/removed_duplicated.csv'
    print('going to parse ', csvFile)
    parse(csvFile)

if __name__ == '__main__':
    main()
