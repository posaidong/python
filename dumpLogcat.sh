#!/bin/bash

# Android应用运行起来后, 通过该脚本过滤出所有应用的日志

packageName='com.harman.ble.jbllink'
pid=`adb shell ps | grep $packageName | awk '{print $2}'`
echo 'pid=' $pid
adb logcat -c
adb logcat | grep $pid > log.txt &


