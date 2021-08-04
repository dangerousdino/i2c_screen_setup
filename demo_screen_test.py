from rpi_lcd import LCD
from time import sleep
import os
import datetime

# Loads lcd module
lcd = LCD()

# runs linux command to get hostname and returns value when function called
def get_hostname():
    gethost = os.popen('hostname')
    host = gethost.read().strip()
    return host

# runs linux command to get host IP (wlan0 for Wi-Fi and eth0 for ethernet) and returns value when function called
def get_ip():
    f = os.popen('ifconfig wlan0 | grep "inet" | cut -d: -f2 | cut -d " " -f10')
    ip=f.read().strip()
    return ip

def get_time():
    now = datetime.datetime.now()
    time = now.strftime("%H:%M:%S")
    return time

def get_temp():
    cputemp = os.popen('/opt/vc/bin/vcgencmd measure_temp |grep "temp" | cut -d "" -f1 | cut -d "=" -f2')
    temp = cputemp.read().strip()
    return temp

def main():

    while True:
        try:
            host = get_hostname()
            time = get_time()
            ip = get_ip()
            temp = get_temp()
            lcd.text('IP:' + ip , 1)
            lcd.text('Time:' + time,2)
            lcd.text('host:' + host, 3)
            lcd.text('CPU:' + temp, 4)
            sleep(5)
            lcd.clear()
        except KeyboardInterrupt:
           lcd.clear()
           break
        except:
           continue
main()