#!/usr/bin/python

import sys
import os

class UserInfo:

    def __init__(self):
        self.model = ''
        self.userIdsIOS = set()
        self.userIdsAndroid = set()

    def __repr__(self):
        return str(self.__dict__)

def parse(csvFile):
    file = open(csvFile, 'r')
    line = file.readline()

    userIds = set()
    modelDict = dict()
    while True:
        line = file.readline()
        if not line:
            break
        params = line.strip().split(',')
        userIds.add(params[1])

        model = params[-1].upper()
        if model not in modelDict:
            modelDict[model] = UserInfo()

        userInfo = modelDict[model]
        userInfo.model = model

        isIOS = True if params[-4] == "IOS" else False
        if isIOS:
            userInfo.userIdsIOS.add(params[1])
        else:
            userInfo.userIdsAndroid.add(params[1])

    file.close()

    print("tatal app users: ", len(userIds))

    print(modelDict.keys())
    cnt = 0
    for it in modelDict.values():
        cnt += len(it.userIdsIOS)
        cnt += len(it.userIdsAndroid)
        print(it.model, " , iOS Users =", len(it.userIdsIOS), " , Android Users =", len(it.userIdsAndroid), ", total =", str(len(it.userIdsIOS) + len(it.userIdsAndroid)))

    print("total hp devices: ", cnt)

if __name__ == '__main__':
    parse('ds/DeviceConnect1031.csv')