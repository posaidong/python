import subprocess
import time
import os

print('startLogcat...')

subprocess.call(['./dumpLogcat.sh'])

print('sleeping...')
time.sleep(10)
print('over sleep')

# killall - kill processes by name
# SIGINT	2	Terminate	Terminal interrupt signal
os.system('adb shell killall -2 logcat')

print('existing....')