#!/usr/bin/python

import sys
import os

def sort_bytime(line):
    params = line.split(',')
    return params[len(params) - 4]

def parse(csvFile):
    file = open(csvFile, 'r')
    line = file.readline()

    macAddressDict = dict()
    while True:
        line = file.readline()
        if not line:
            break
        params = line.split(',')
        macAddress = params[1].replace('"', '')
        appVersion = params[6].replace('"', '')
        durationJBLConnect = params[8].replace('"', '')
        jblConnect = 0
        try:
            jblConnect = int(params[7].replace('"', ''))
        except:
            continue
        currenttimestamp = params[len(params) - 4].replace('"', '')
        currenttimestamp = currenttimestamp.replace('T', ' ')
        currenttimestamp = currenttimestamp.replace('Z', '')
        mobModel = params[44].replace('"', '')

        if macAddress not in macAddressDict:
            macAddressDict[macAddress] = []
        else:
            macAddressDict[macAddress].append(line)


    file.close()

    for k,v in macAddressDict.items():
        if len(v) > 50:
            print(k, len(v))
            v.sort(key=sort_bytime)
            for i in v:
                print(i)


def main():
    # if len(sys.argv) <= 1:
    #     print("Usage: python ", os.path.basename(__file__), " path_to_csv")
    #     exit(-1)

    csvFile = '/Users/sunnysun/Desktop/Android_4.5.228.csv'
    print('going to parse ', csvFile)
    parse(csvFile)

if __name__ == '__main__':
    main()