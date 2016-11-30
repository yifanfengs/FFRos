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


def post_dev_info():
    data = {}
    sn = '123'
    ip = get_ip_address('vmnet8')
    timestamp =  int(time.time())
    token = '{"sn":"%s","ip":"%s","timestamp":%s}' % (sn, ip, timestamp)
    data['token'] = Ljcode(token)
    url = 'http://ip.mengdie.com/api/server/report_ip'
    post_data = urllib.urlencode(data)
    req = urllib2.urlopen(url, post_data)
    content = req.read()
    print content


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


def get_rand():
	str=""
	for i in range(0,13):
		str+=random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()')
	return str

def Ljcode(in_str):
	rand=get_rand()
	curltime=str(int(time.time()))+"000"
	key="lingjiang.com"
	TRK=""
	TRK=curltime+rand+key
	md=hashlib.md5()
	md.update(TRK)
	TRK=md.hexdigest()
	in_str_64=base64.b64encode(in_str)
	step1=xor_encode(in_str_64, TRK)
	step2=xor_encode(curltime, rand)
	step3=xor_encode(rand, key)
	step4=step1+step2+step3
	return base64.b64encode(step4)

def xor_encode(str1,str2):
    orxstr=""
    for i in range(0,len(str1)):
        rst=ord(list(str1)[i])^ord(list(str2)[i%len(str2)])
        orxstr=orxstr+ chr(rst)
    return orxstr

def main():
	while 1:
		post_dev_info()
		time.sleep(30)
	#while 1:
	#	sock_dev_info()

if __name__ == '__main__':
	main()

