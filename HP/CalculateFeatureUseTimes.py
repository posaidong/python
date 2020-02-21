#!/usr/bin/python

import sys
import os
import time
from datetime import datetime


class DAInfo:
    pass


def parse(csvFile, daInfoDict):
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
        appPlatform = params[-4].replace('"', '')
        productName = params[3].replace('"', '')
        appEQChange = int(params[11].replace('"', ''))
        appDeviceDisovered = int(params[8].replace('"', ''))
        appSmartAssistant = int(params[27].replace('"', ''))
        appAutoOff = int(params[23].replace('"', ''))
        appANC = int(params[9].replace('"', ''))
        appAmbientAware = int(params[25].replace('"', ''))

        if (macAddress not in daInfoDict):
            daInfoDict[macAddress] = DAInfo()
            daInfoDict[macAddress].reportTimes = 0
            daInfoDict[macAddress].appEQChange = 0
            daInfoDict[macAddress].appDeviceDisovered = 0
            daInfoDict[macAddress].appSmartAssistant = 0
            daInfoDict[macAddress].appAutoOff = 0
            daInfoDict[macAddress].appANC = 0
            daInfoDict[macAddress].appAmbientAware = 0
            daInfoDict[macAddress].appPlatform = appPlatform
            daInfoDict[macAddress].productName = productName

        daInfoDict[macAddress].appEQChange += appEQChange
        daInfoDict[macAddress].appDeviceDisovered += appDeviceDisovered
        if (appSmartAssistant > 0):
            daInfoDict[macAddress].appSmartAssistant += 1
        if (appAutoOff > 0):
            daInfoDict[macAddress].appAutoOff += 1
        if (appANC > 0):
            daInfoDict[macAddress].appANC += 1
        if (appAmbientAware > 0):
            daInfoDict[macAddress].appAmbientAware += 1
        daInfoDict[macAddress].reportTimes += 1

    file.close()


def generateReport(csvFile, daInfoDict):
    file = open(csvFile, 'w')
    file.write(
        'macAddress,appPlatform,productName,reportTimes,appEQChange,appDeviceDisovered,appSmartAssistant,appAutoOff,appANC,appAmbientAware\n')

    for k, v in daInfoDict.items():
        file.write(k + ',' + v.appPlatform
                   + ',' + v.productName + ',' + str(v.reportTimes) + ',' + str(v.appEQChange) + ',' + str(
            v.appDeviceDisovered) + ',' + str(v.appSmartAssistant) + ',' + str(v.appAutoOff) + ',' + str(
            v.appANC) + ',' + str(v.appAmbientAware) + '\n')
    file.close()


def getTimestamp(str):
    return time.mktime(time.strptime(str, '%Y-%m-%d %H:%M:%S'))


def timestamp2Str(timestamp):
    return datetime.fromtimestamp(timestamp)


def main():
    # if len(sys.argv) <= 1:
    #     print("Usage: python ", os.path.basename(__file__), " path_to_csv")
    #     exit(-1)

    # csvFile = './ds/realtime_tblheadphone_data_201912271614.csv'
    csvFile = './ds/alldata_2019_1224_1231.csv'
    outFile = './ds/report.csv'
    print('going to parse ', csvFile)

    daInfoDict = dict()
    parse(csvFile, daInfoDict)
    generateReport(outFile, daInfoDict)


if __name__ == '__main__':
    main()
