#!/usr/bin/env python3

import socket

list_servers = {1:'drive.google.com', 2:'mail.google.com', 3:'google.com'}

def IP_get():
    for key, value in list_servers:
        old_IP = key
        list_server[key] = [socket.gethostbyname(value)]
        print(old_IP, ' - ', key)

def IP_check():
    for key, value in list_servers:
        list_server = [socket.gethostbyname(server)]
        IPs_old = [list_servers.keys()]
        result = []
        for newIP in IPs_new:
            for oldIP in IPs_old:
                if newIP != oldIP:
                    print('[ERROR] ', server, ' IP mismatch: ', oldIP, ' - ', newIP)
                    continue

IP_get()
IP_check()

