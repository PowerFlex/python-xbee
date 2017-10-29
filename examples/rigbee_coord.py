#! /usr/bin/python

"""
intercept_sample.py

derived from receive_samples.py

By Paul Malmsten, 2010
pmalmsten@gmail.com

This example continuously reads the serial port and processes IO data
received from a remote XBee.
"""

from xbee.thread import XBee, ZigBee
import serial
import sys

print sys.path

PORT = '/dev/ttyXBC0'
BAUD_RATE = 19200

# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)

# Create API object
xbee = ZigBee(ser)

print xbee

# Continuously read and print packets
while True:
    try:
        response = xbee.wait_sniff_sent_frame()
        print "RESPONSE", response
    except KeyboardInterrupt:
        break

ser.close()
