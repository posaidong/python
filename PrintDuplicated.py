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
        # print(params[len(params) - 4])
        val = params[1] + ',' + params[len(params) - 4]


        if line not in existing:
            existing.add(line)
        else:
            print(line)

    file.close()
    output.close()

def main():
    # if len(sys.argv) <= 1:
    #     print("Usage: python ", os.path.basename(__file__), " path_to_csv")
    #     exit(-1)

    csvFile = '/Users/sunnysun/Desktop/data_fetched_18th_july_android.csv'
    print('going to parse ', csvFile)
    parse(csvFile)

if __name__ == '__main__':
    main()
