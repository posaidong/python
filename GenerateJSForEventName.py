#!/usr/bin/python

import sys
import os
import json


def generateJSForEventName(jsonFile):
    with open(jsonFile) as file:
        data = json.load(file)
        for e in data['event_names']:
            print('exports.' + e['event_name'] + ' = functions.analytics.event("' + e[
                'event_name'] + '").onLog((event, context) => { handleEvent(event, context); });')


def main():
    print("generate js for event name")
    jsonFile = '/Users/sunnysun/Work/firebase_functions/JBLConnectTest2/functions/smart_audio.json'
    generateJSForEventName(jsonFile)


if __name__ == '__main__':
    main()
