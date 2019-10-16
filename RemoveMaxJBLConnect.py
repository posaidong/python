#!/usr/bin/python

import sys
import os

def removeBiggectJBLConnect(input, biggestJBLConnect):
    file = open(input, 'r')
    output = open('/Users/sunnysun/Desktop/removed_max_jblconnect.csv', 'w')
    line = file.readline()
    title = line
    output.write(line)

    print('biggestJBLConnect len=', len(biggestJBLConnect))

    i = 0
    while True:
        line = file.readline()
        if not line:
            break
        params = line.split(',')
        macAddress = params[1].replace('"', '')
        jblConnect = 0
        try:
            jblConnect = int(params[7].replace('"', ''))
        except:
            pass

        if macAddress in biggestJBLConnect and biggestJBLConnect[macAddress] == jblConnect:
            print(i, ', remove ', macAddress, ',', jblConnect)
            i += 1
            biggestJBLConnect.pop(macAddress)
            continue
        else:
            output.write(line)


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
        try:
            jblConnect = int(params[7].replace('"', ''))
        except:
            continue
        currenttimestamp = params[len(params) - 4].replace('"', '')
        currenttimestamp = currenttimestamp.replace('T', ' ')
        currenttimestamp = currenttimestamp.replace('Z', '')
        mobModel = params[44].replace('"', '')

        if macAddress not in macDict:
            macDict[macAddress] = []
        macDict[macAddress].append(jblConnect)

    file.close()

    i = 0
    biggestJBLConnect = dict()

    for k, v in macDict.items():
        s = sorted(v, reverse=True)
        totalJBLConnect = 0
        # remove the first one
        if len(s) > 0:
            totalJBLConnect = sum(s)

        if totalJBLConnect > 0:
            print(i, ',' , k, ',', totalJBLConnect, ',', s)
            i += 1
            biggestJBLConnect[k] = s[0]
        else:
            continue

    removeBiggectJBLConnect(csvFile, biggestJBLConnect)

def main():
    # if len(sys.argv) <= 1:
    #     print("Usage: python ", os.path.basename(__file__), " path_to_csv")
    #     exit(-1)

    csvFile = '/Users/sunnysun/Desktop/flip-4-android-app-version-4.3.214-4.5.223-fw-ver-3.9.0.csv'
    print('going to parse ', csvFile)
    parse(csvFile)

if __name__ == '__main__':
    main()