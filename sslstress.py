#!/usr/bin/env python
from socket import error as socket_error
from socket import socket
from ssl import SSLContext
from ssl import PROTOCOL_SSLv23
import errno
import sys

CTX = SSLContext(PROTOCOL_SSLv23)

args = sys.argv
def Connect(addr):
    sock = socket()
    sock.connect(addr)
    try:
        sslobj = CTX._wrap_socket(sock._sock, server_side=False)
        sslobj.do_handshake()
    except Exception as ex:
        raise
        

def DoConnect(hs,addrs):
    Port = 443
    address = addrs
    if (len(addrs.split(':')) == 2):
        try:
            Port = int(addrs.split(':')[1])
        except ValueError:
            print "Error: invalid port number."
            exit(2)
        address = addrs.split(':')[0]
    try:
        Handshakes = 0
        if (hs > 0):
            while (Handshakes != hs):
                Handshakes+=1
                Connect((address,Port))
                Out = str(Handshakes)+" Sucessuful handshakes.."
                sys.stdout.write('\r')
                sys.stdout.write(Out)
                sys.stdout.flush()
        
        elif (hs == 0):
            while True:
                Handshakes+=1
                Connect((address,Port))
                Out = str(Handshakes)+" Sucessuful handshakes.."
                sys.stdout.write('\r')
                sys.stdout.write(Out)
                sys.stdout.flush()
        print
    except KeyboardInterrupt:
        print


if (len(args) == 3):
    try:
        int(args[2])
    except:
        print "Incorrect number of handshakes."
        exit(2)
    try:
        DoConnect(int(args[2]),args[1])
    except socket_error as serr:
        if serr.errno != errno.ECONNREFUSED:
            raise serr
        print "Error: Connection Refused."
        
        

elif (len(args) == 2):
        DoConnect(0,args[1])
else:
    print "Usage: "+args[0]+" host:port <number of Handshakes>"

print "Bye!"




