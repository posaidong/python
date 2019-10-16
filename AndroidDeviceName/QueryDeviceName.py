#!/usr/bin/python

import sys
import os
import urllib.request

# model = marketing name
modelDict = dict()


def initDB(fileName):
    file = open(fileName, 'r', encoding="utf-16")
    line = file.readline()

    while True:
        line = file.readline()
        if not line:
            break
        # Retail Branding,Marketing Name,Device,Model
        params = line.split(',')
        modelDict[params[3].strip()] = params[0] + ' ' + params[1]

    file.close()


# Device model,Users
def parse(csvFile):
    file = open(csvFile, 'r')
    line = file.readline()

    # marketing name = Users
    phoneDict = dict()
    while True:
        line = file.readline()
        if not line:
            break
        params = line.split(',')
        model = params[0]
        phoneCnt = int(params[1].strip())
        if model in modelDict:
            marketingName = modelDict[model]
            if marketingName in phoneDict:
                phoneDict[marketingName] = phoneDict[marketingName] + phoneCnt
            else:
                phoneDict[marketingName] = phoneCnt

    file.close()

    topPhone = sorted(phoneDict.items(), key=lambda kv: kv[1], reverse=True)
    for tuple in topPhone:
        print(tuple[0], ',', tuple[1])


def main():
    # if len(sys.argv) <= 1:
    #     print("Usage: python ", os.path.basename(__file__), " path_to_csv")
    #     exit(-1)

    inputFile = 'device_model.csv'
    print('going to parse ', inputFile)

    url = 'http://storage.googleapis.com/play_public/supported_devices.csv'
    fileName = os.path.basename(url)

    if not os.path.exists(fileName):
        urllib.request.urlretrieve(url, fileName)

    if os.path.exists(fileName):
        initDB(fileName)
        parse(inputFile)

if __name__ == '__main__':
    main()
