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
def parseAndroid(csvFile, totalUsers):
    file = open(csvFile, 'r')
    line = file.readline()

    # marketing name = Users
    phoneDict = dict()
    # totalUsers = 0
    while True:
        line = file.readline()
        if not line:
            break
        params = line.split(',')
        model = params[0]
        users = int(params[1].strip())
        # totalUsers = totalUsers + users
        if model in modelDict:
            marketingName = modelDict[model]
            if marketingName in phoneDict:
                phoneDict[marketingName] = phoneDict[marketingName] + users
            else:
                phoneDict[marketingName] = users

    file.close()
    print('android total devices count=', totalUsers, ' total phone serials=', len(phoneDict.keys()))

    file = open('out_' + csvFile, 'w')
    file.write('Device model,Users,Percentage\n')

    topPhones = sorted(phoneDict.items(), key=lambda kv: kv[1], reverse=True)
    i = 0
    for tuple in topPhones:
        print(i, ',', tuple[0], ',', tuple[1], ',', '{:.2%}'.format(tuple[1] / totalUsers))
        file.write(tuple[0] + ',' + str(tuple[1]) + ',' + '{:.2%}'.format(tuple[1] / totalUsers) + '\n')
        if i > 100:
            break
        i = i + 1

    file.close()


def parseIOS(csvFile):
    file = open(csvFile, 'r')
    line = file.readline()

    # marketing name = Users
    phoneDict = dict()
    totalUsers = 0
    while True:
        line = file.readline()
        if not line:
            break
        params = line.split(',')
        marketingName = params[0]
        users = int(params[1].strip())
        totalUsers = totalUsers + users
        phoneDict[marketingName] = users

    file.close()
    print('iOS total devices count=', totalUsers, ' total phone serials=', len(phoneDict.keys()))

    file = open('out_' + csvFile, 'w')
    file.write('Device model,Users,Percentage\n')

    topPhones = sorted(phoneDict.items(), key=lambda kv: kv[1], reverse=True)
    for tuple in topPhones:
        print(tuple[0], ',', tuple[1], ',', '{:.2%}'.format(tuple[1] / totalUsers))
        file.write(tuple[0] + ',' + str(tuple[1]) + ',' + '{:.2%}'.format(tuple[1] / totalUsers) + '\n')

    file.close()


def main():
    # if len(sys.argv) <= 1:
    #     print("Usage: python ", os.path.basename(__file__), " path_to_csv")
    #     exit(-1)

    androidInput = 'jblconnect_android.csv'
    iOSInput = 'jblconnect_iOS.csv'
    parseIOS(iOSInput)

    url = 'http://storage.googleapis.com/play_public/supported_devices.csv'
    fileName = os.path.basename(url)

    if not os.path.exists(fileName):
        urllib.request.urlretrieve(url, fileName)

    if os.path.exists(fileName):
        initDB(fileName)
        parseAndroid(androidInput, 2634020)


if __name__ == '__main__':
    main()
