#!/usr/bin/python

import sys
import os
import subprocess
import json

files = []
def searchFile(path):
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for folder in d:
            searchFile(os.path.join(r, folder))
        for file in f:
            if '.parquet' in file:
                files.append(os.path.join(r, file))

def parseFile(file):
    # parquet-tools cat --json aa.snappy.parquet
    bashCommand = 'parquet-tools cat --json ' + file
    print(bashCommand)
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)

    'output type is byte'
    output, error = process.communicate()
    if error != None:
        print('parse file failed: ', error)
        return

    tmp = open('/Users/sunnysun/tmp/2.txt', 'w')
    tmp.write(output.decode('utf-8'))
    tmp.close()
    # data = json.loads(output)
    # print(data)


def main():
    if len(sys.argv) <= 1:
        print("Usage: python ", os.path.basename(__file__), " path_to_directory")
        exit(-1)

    path = sys.argv[1]
    print('searching ', path)
    searchFile(path)

    parseFile(files[1])

    # for file in files:
    #     parseFile(file)
    #     break;


if __name__ == '__main__':
    main()