#!/usr/bin/env python
import serial
import signal
import sys
import time
import argparse

parser = argparse.ArgumentParser(description='Dump the values read by the teensy via serial port out to this terminal.')
parser.add_argument('serial_port_name', metavar='SERIAL_PORT', help="The name of the serial port to connect to. E.g. 'COM1' (windows) or '/dev/tty.usbserial-1' (OSX). See this link to find the serial port on macs: https://stackoverflow.com/questions/12254378/how-to-find-the-serial-port-number-on-mac-os-x")


serial_port = serial.Serial()

def connect(serial_port_name):
	serial_port.baudrate = 9600
	serial_port.port = serial_port_name
	serial_port.open()
	print("connected to: " + serial_port.portstr)


def read_serial_data_and_print():
	while True:
		line = serial_port.readline()
		print(line.decode('utf-8'), end='')


def close_serial_port_connection():
	serial_port.close()

def signal_handler(sig, frame):
    print('You pressed Ctrl+C! Closing Serial Port connection and exiting.')
    close_serial_port_connection()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
if __name__ == '__main__':
	if len(sys.argv) < 2:
	    parser.print_help()
	    print('')
	args = parser.parse_args()
	connect(args.serial_port_name)
	time.sleep(1)
	read_serial_data_and_print()

