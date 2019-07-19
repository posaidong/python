#!/usr/bin/python

import sys
import os

# macAddress,productName,currenttimestamp,appVersion,firmwareVersion
def parse(csvFile):
    file = open(csvFile, 'r')
    output = open('/Users/sunnysun/Desktop/out.csv', 'w')
    line = file.readline()
    title = line

    output.write(line)

    existing = set()
    while True:
        line = file.readline()
        if not line:
            break
        params = line.split(',')
        val = params[0] + ',' + params[2]
        if val not in existing:
            output.write(line)

        existing.add(val)

    file.close()
    output.close()

def main():
    # if len(sys.argv) <= 1:
    #     print("Usage: python ", os.path.basename(__file__), " path_to_csv")
    #     exit(-1)

    csvFile = '/Users/sunnysun/Desktop/1.csv'
    print('going to parse ', csvFile)
    parse(csvFile)

if __name__ == '__main__':
    main()
