#!/usr/bin/python

import sys
import os

def getMaxItem(item):
    s = sorted(item[1], reverse=True)
    if len(s) > 0:
        return s[0]
    return 0

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
        playtime = 0
        try:
            jblConnect = int(params[7].replace('"', ''))
            playtime = int(params[11].replace('"', ''))
        except:
            continue
        currenttimestamp = params[len(params) - 4].replace('"', '')
        currenttimestamp = currenttimestamp.replace('T', ' ')
        currenttimestamp = currenttimestamp.replace('Z', '')
        mobModel = params[44].replace('"', '')

        if macAddress not in macDict:
            macDict[macAddress] = []
        macDict[macAddress].append(playtime)

    file.close()

    list = sorted(macDict.items(), key=getMaxItem, reverse=True)

    i = 0
    for item in list:
        if len(item[1]) > 0 and item[1][0] > 0:
            print(item[0], sorted(item[1], reverse=True))
            i += 1
            if i > 10:
                break


def main():
    # if len(sys.argv) <= 1:
    #     print("Usage: python ", os.path.basename(__file__), " path_to_csv")
    #     exit(-1)

    csvFile = '/Users/sunnysun/Desktop/removed_duplicated.csv'
    print('going to parse ', csvFile)
    parse(csvFile)

if __name__ == '__main__':
    main()