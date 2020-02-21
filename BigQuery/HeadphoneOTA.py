#!/usr/bin/python

import sys
import os

class OTAInfo:
    model = ""
    otaTriggeredIOS = 0
    otaSuccessIOS = 0
    otaFailIOS = 0

    otaTriggeredAndroid = 0
    otaSuccessAndroid = 0
    otaFailAndroid = 0

    def __repr__(self):
        #return str(self.__dict__)
        return self.model + ' ,Trigged:'+str(self.otaTriggeredIOS + self.otaTriggeredAndroid)+' ,Success:' + str(self.otaSuccessAndroid + self.otaSuccessIOS) + ' , Fail:' + str(self.otaFailAndroid + self.otaFailIOS)

def parse(csvFile):
    file = open(csvFile, 'r')
    line = file.readline()

    modelDict = dict()
    while True:
        line = file.readline()
        if not line:
            break
        params = line.strip().split(',')
        if params[-2] == 'device_name':
            model = params[-1].upper()
            if model not in modelDict:
                modelDict[model] = OTAInfo()

            otaInfo = modelDict[model]
            otaInfo.model = model

            eventName = params[-3]
            isIOS = True if params[-4] == "IOS" else False
            if eventName == 'firmware_update_begun':
                if isIOS:
                    otaInfo.otaTriggeredIOS = otaInfo.otaTriggeredIOS + 1
                else:
                    otaInfo.otaTriggeredAndroid = otaInfo.otaTriggeredAndroid + 1
            elif eventName == 'firmware_update_failed':
                if isIOS:
                    otaInfo.otaFailIOS = otaInfo.otaFailIOS + 1
                else:
                    otaInfo.otaFailAndroid = otaInfo.otaFailAndroid + 1
            elif eventName == 'firmware_update_finished':
                if isIOS:
                    otaInfo.otaSuccessIOS = otaInfo.otaSuccessIOS + 1
                else:
                    otaInfo.otaSuccessAndroid = otaInfo.otaSuccessAndroid + 1

    file.close()

    print(modelDict.keys())
    for ota in modelDict.values():
        print(ota)


if __name__ == '__main__':
    parse('ds/ota_1031.csv')