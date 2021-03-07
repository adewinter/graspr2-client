#!/usr/bin/env python
import serial
import signal
import sys
import time

serial_port = serial.Serial()

def connect():
	serial_port.baudrate = 9600
	serial_port.port = 'COM7'
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
	connect()
	time.sleep(1)
	read_serial_data_and_print()