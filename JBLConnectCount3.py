#!/usr/bin/python

import sys
import os

threshold = ['=1','2-5','6-10', '>10']
jblConnectCnt = [0,0,0,0]
speakerphoneCnt = [0,0,0,0]

def parse(csvFile):
    file = open(csvFile, 'r')
    line = file.readline()

    macDict = dict()
    while True:
        line = file.readline()
        if not line:
            break
        params = line.split(',')
        macAddress = params[1].replace('"', '')
        appVersion = params[6].replace('"', '')
        jblConnect = 0
        headphone = 0
        durationJBLConnect = 0
        speakerphone = 0
        try:
            jblConnect = int(params[7].replace('"', ''))
            headphone = int(params[16].replace('"', ''))  # speakerphone
            durationJBLConnect = int(params[8].replace('"', ''))
            speakerphone = int(params[16].replace('"', ''))
        except:
            continue
        currenttimestamp = params[len(params) - 4].replace('"', '')
        currenttimestamp = currenttimestamp.replace('T', ' ')
        currenttimestamp = currenttimestamp.replace('Z', '')
        mobModel = params[44].replace('"', '')

        if macAddress not in macDict:
            macDict[macAddress] = [0,0]
        macDict[macAddress][0] += jblConnect
        macDict[macAddress][1] += headphone

    file.close()

    for k, v in macDict.items():
        if v[0] > 10:
            jblConnectCnt[3] +=1
        if v[1] > 10:
            speakerphoneCnt[3] +=1

        if v[0] >= 6 and v[0] <= 10:
            jblConnectCnt[2] +=1
        if v[1] >= 6 and v[1] <=10:
            speakerphoneCnt[2] +=1

        if v[0] >= 2 and v[0] <= 5:
            jblConnectCnt[1] +=1
        if v[1] >= 2 and v[1] <=5:
            speakerphoneCnt[1] +=1

        if v[0] == 1:
            jblConnectCnt[0] +=1
        if v[1] == 1:
            speakerphoneCnt[0] +=1

    macAddressTotal = len(macDict.keys())

    print('threshold ', threshold)
    print('jblConnectCnt ', jblConnectCnt, ['{:.1%}'.format(x / macAddressTotal) for x in jblConnectCnt])
    print('speakerphoneCnt ', speakerphoneCnt, ['{:.1%}'.format(x / macAddressTotal) for x in speakerphoneCnt])

def main():
    # if len(sys.argv) <= 1:
    #     print("Usage: python ", os.path.basename(__file__), " path_to_csv")
    #     exit(-1)

    csvFile = '/Users/sunnysun/Desktop/removed_duplicated.csv'
    print('going to parse ', csvFile)
    parse(csvFile)

if __name__ == '__main__':
    main()
