#!/usr/bin/python

import sys
import os

n = 1

def parse(csvFile):
    file = open(csvFile, 'r')
    line = file.readline()
    title = line
    print(title)

    macAddressSet = set()
    jblConnect = set()
    durationJBLConnect = set()
    speakerphone = set()

    jblConnectDict = {}
    speakphoneDict = {}
    while True:
        line = file.readline()
        if not line:
            break
        params = line.split(',')
        mac = params[1]
        macAddressSet.add(mac)  # macAddress
        connect = 0
        headphone = 0
        duration = 0
        try:
            connect = int(params[7].replace('"', '')) #jblConnect
            duration = int(params[8].replace('"', '')) #durationJBLConnect
            headphone = int(params[16].replace('"', '')) #speakerphone
        except:
            #print('invalid jblConnect, ' , line)
            continue

        if connect > 0 :
            jblConnect.add(mac + ',1')

        if duration > 0:
            durationJBLConnect.add(mac + ',1')

        if headphone > 0:
            speakerphone.add(mac + ',1')

        if mac not in jblConnectDict:
            jblConnectDict[mac] = 0
        jblConnectDict[mac] += connect

        if mac not in speakphoneDict:
            speakphoneDict[mac] = 0
        speakphoneDict[mac] += headphone

    file.close()

    print('macAddress=', len(macAddressSet))
    print('jblConnect=', len(jblConnect))
    print('durationJBLConnect=', len(durationJBLConnect))
    print('speakerphone=', len(speakerphone))


    jblConnectCnt = 0
    for k,v in jblConnectDict.items():
        if v > n:
            jblConnectCnt += 1

    speakphoneCnt = 0;
    for k,v in speakphoneDict.items():
        if v >= n:
            speakphoneCnt += 1

    print('jblConnectCnt=', jblConnectCnt)
    print('speakerphoneCnt=', speakphoneCnt)

def main():
    csvFile = '/Users/sunnysun/Desktop/data_fetched_18th_july_android.csv'
    print('going to parse ', csvFile)
    parse(csvFile)

if __name__ == '__main__':
    main()
