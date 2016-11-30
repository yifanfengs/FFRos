# coding=utf-8
import socket
import os


lan_ip = os.popen("uci get network.lan.ipaddr").read().rstrip();
#lan_ip = '127.0.0.1'
port = 1234

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
    create_srv()

if __name__ == '__main__':
    main()





