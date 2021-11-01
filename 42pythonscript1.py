#!/usr/bin/env python3

import os
import socket
import ast

file_list = os.popen("ls").read()
file_list = file_list.split('\n')
if 'server_IPs.txt' in file_list:
    pass
else:
    with open('server_IPs.txt', 'w') as file:
        file.write("{'drive.google.com': 1, 'mail.google.com': 2, 'google.com': 3}")

with open('server_IPs.txt', 'r') as file:
    servers = file.read()
    dict_new = ast.literal_eval(servers)
    old_IPs = dict_new
    new_IPs = dict_new
    key_list = old_IPs.keys()
    for key in key_list:
        temp = socket.gethostbyname(key)
        if temp != old_IPs[key]:
            print('[ERROR] ', key, ' IP mismatch: ', old_IPs[key], ' - ', temp, '\n')
        else:
                print(key, ' IP didn\'t change.\n')
        new_IPs[key] = temp
    result = str(new_IPs)
    with open('server_IPs.txt', 'w') as old_file:
        old_file.write(result)