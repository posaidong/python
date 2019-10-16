#!/usr/bin/python

import sys
import os

def parse(csvFile):
    file = open(csvFile, 'r')
    output = open('/Users/sunnysun/Desktop/removed_duplicated.csv', 'w')
    line = file.readline()
    title = line
    output.write(line)

    existingRecords = set()
    removeCnt = 0
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

        deviceParam = params[7:29]
        val = ''.join(str(e) for e in deviceParam)
        val += macAddress
        val += currenttimestamp

        if val in existingRecords:
            removeCnt += 1
            print('remove  ', val)
            continue

        existingRecords.add(val)
        output.write(line)

    file.close()
    output.close()

    print('removeCnt=', removeCnt)


def main():
    # if len(sys.argv) <= 1:
    #     print("Usage: python ", os.path.basename(__file__), " path_to_csv")
    #     exit(-1)

    csvFile = '/Users/sunnysun/Desktop/removed_max_jblconnect.csv'
    print('going to parse ', csvFile)
    parse(csvFile)

if __name__ == '__main__':
    main()