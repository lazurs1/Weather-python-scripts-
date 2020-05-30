 #!/usr/bin/python
import serial
from datetime import datetime
import time
import urllib
import pdb

port=serial.Serial(port='/dev/ttyS0',baudrate=9600, timeout=1.0)
eof = "\xff\xff\xff"
rcvd =''
#temp


txtestx = 'hello there'
txx1 = 'page0.txx1.txt="'+txtestx+'"'+eof
port.write(txx1)
print (str (txx1))

#while True:
    #Serial_line = port.readline()
    #touch=port.read_until(eof)
    #print str(touch)
    #read_byte = port.read()
    #print '%x' % ord(read_byte)

while True:s
    c = port.read()
    if len(c) == 0:
        print("blank")
   
    for ch in c:
        print ord(ch), " ",

#Enter Key 101   1   11   1   255   255   255   blank
#Enter Key 101DEVICE   1-Screen   11-Button   1   255END   255END   255END   blank
