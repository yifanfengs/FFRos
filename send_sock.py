# coding=utf-8
import socket
import os
import fcntl
import struct
import urllib2
import urllib
import time
import random
import hashlib
import base64

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])





def sock_dev_info():
	HOST='60.169.73.108'
	PORT=30521
	dev_id='00001'
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((HOST,PORT))
	cmd=raw_input("Please input cmd:")
	s.send(cmd)
	data=s.recv(1024)
	print data
	s.close()



def main():
	#while 1:
	#	post_dev_info()
	#	time.sleep(30)SS
	while 1:
		sock_dev_info()

if __name__ == '__main__':
	main()
