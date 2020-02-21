#!/usr/bin/python

import sys
import os
import time
from datetime import datetime


class AppInfo:
    pass


def parse(csvFile, appUploadTimeDict, appInfoDict):
    file = open(csvFile, 'r')
    line = file.readline()
    title = line

    while True:
        line = file.readline()
        if not line:
            break

        params = line.split(',')
        macAddress = params[0].replace('"', '')
        appUploadTime = params[7].replace('"', '')
        appPlatform = params[-4]
        productName = params[3]

        if (macAddress not in appUploadTimeDict):
            appUploadTimeDict[macAddress] = []
            appInfoDict[macAddress] = AppInfo()

        appUploadTimeDict[macAddress].append(appUploadTime)
        appInfoDict[macAddress].appPlatform = appPlatform
        appInfoDict[macAddress].productName = productName

    file.close()


def printTopReportedUser(topNumber, d):
    i = 0
    for k in sorted(d, key=lambda k: len(d[k]), reverse=True):
        print(k, len(d[k]))
        if i > topNumber:
            break
        i += 1


def getTimestamp(str):
    return time.mktime(time.strptime(str, '%Y-%m-%d %H:%M:%S'))


def timestamp2Str(timestamp):
    return datetime.fromtimestamp(timestamp)


def printDuplicatedRecords(intervalSeconds, appUploadTimeDict, appInfoDict):
    for k, v in appUploadTimeDict.items():
        v.sort()
        previousTime = -1
        for t in v:
            if (len(v) <= 1):
                continue
            try:
                if previousTime == -1:
                    previousTime = getTimestamp(t)
                else:
                    now = getTimestamp(t)
                    if (now - previousTime <= intervalSeconds):
                        print(k, ',', appInfoDict[k].appPlatform, ',', appInfoDict[k].productName, ', interval=',
                              now - previousTime, timestamp2Str(previousTime), timestamp2Str(now))
                        break
                    previousTime = now

            except ValueError:
                pass


def main():
    # if len(sys.argv) <= 1:
    #     print("Usage: python ", os.path.basename(__file__), " path_to_csv")
    #     exit(-1)

    # csvFile = './ds/realtime_tblheadphone_data_201912271614.csv'
    csvFile = './ds/EQgt50_realtime_tblheadphone_data_202001021516.csv'
    print('going to parse ', csvFile)

    appUploadTimeDict = dict()
    appInfoDict = dict()
    parse(csvFile, appUploadTimeDict, appInfoDict)
    printTopReportedUser(10, appUploadTimeDict)
    printDuplicatedRecords(5, appUploadTimeDict, appInfoDict)


if __name__ == '__main__':
    main()
