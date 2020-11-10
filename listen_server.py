import socket, traceback
import pandas as pd
import xml.dom.minidom
from datetime import datetime, timedelta
import itertools
import io
import time
import numpy as np
import xml.etree.ElementTree as ET


host = ''
port = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))

#used for debugging
# 1. Open a file to write too
# 2. Convert data to csv format 
# a. Convert time - dt_object = datetime.fromtimestamp(timestamp)
print("Success binding")
flag = 0
flagm = 0.0
f = open("testkneesStephen.csv", "w")
f.write("time,X_value,Y_value,Z_value\n")
count = 1800

while count > 0:
    message, address = s.recvfrom(8192)
    messageString = message.decode("utf-8")
    val = messageString.split('>')
    
    x_val = round(float(val[5].split('<')[0]), 5)
    y_val = round(float(val[7].split('<')[0]), 5)
    z_val = round(float(val[9].split('<')[0]), 5)

    sec = 0
    timestamp = val[12].split('<')[0]
    date = int(timestamp)
    UTC = date / 1000
    dt = (datetime.fromtimestamp(UTC))
    mil = dt.strftime("%f")
    

    milli = (float(mil) / 1000000.0)
    print("mil %f\n" % (float(mil) / 1000000.0))
    if flag == 0:
        flag = (dt.second)
        flagm = milli
    sec = float((dt.second - flag)) + (milli - flagm)
    print("Second: %d\n" % dt.second)
    f.write("%.3f,%.5f,%.5f,%.5f\n" % (sec, x_val,y_val,z_val))

    count = count - 1
    print(count)
    
f.close()