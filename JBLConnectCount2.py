#!/usr/bin/python

import sys
import os

N=1

def removeBiggectJBLConnect(input, biggestJBLConnect):
    file = open(input, 'r')
    output = open('/Users/sunnysun/Desktop/out.csv', 'w')
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
            biggestJBLConnect[macAddress] = -1
            continue
        else:
            output.write(line)


def parse(csvFile):
    file = open(csvFile, 'r')
    line = file.readline()

    macDict = dict()
    uploadTime = set()
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

        # time = macAddress + ',' + currenttimestamp
        # if time not in uploadTime:
        #     uploadTime.add(time)
        # else:  # ignore duplicated data
        #     continue

        if macAddress not in macDict:
            macDict[macAddress] = []
        macDict[macAddress].append(jblConnect)

    file.close()

    cnt = 0
    macAddressTotal = 0
    i = 0

    biggestJBLConnect = dict()

    for k, v in macDict.items():
        macAddressTotal += 1
        s = sorted(v, reverse=True)
        totalJBLConnect = 0
        # remove the first one and JBLConnect > 100
        if len(s) > 0:
            start = 1
            # if s[0] > 100:
            #     start = 1
            totalJBLConnect = sum(s[start:len(s)])

        if totalJBLConnect > 0:
            print(i, ',' , k, ',', totalJBLConnect, ',', s)
            i += 1
        else:
            continue

        if totalJBLConnect >= N:
            cnt += 1
            biggestJBLConnect[k] = s[0]
            continue

    print('jblconnect >= ', N, ',', cnt)
    print('macAddressTotal,', macAddressTotal, ',', '{:.1%}'.format(cnt / macAddressTotal))

    #removeBiggectJBLConnect(csvFile, biggestJBLConnect)

def main():
    # if len(sys.argv) <= 1:
    #     print("Usage: python ", os.path.basename(__file__), " path_to_csv")
    #     exit(-1)

    csvFile = '/Users/sunnysun/Desktop/data_fetched_18th_july_android.csv'
    print('going to parse ', csvFile)
    parse(csvFile)

if __name__ == '__main__':
    main()
