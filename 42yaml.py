#!/usr/bin/env python3

import os
import socket
import yaml
import json
import ast

file_list = os.popen("ls").read()
file_list = file_list.split('\n')
#print(file_list)
if 'server_IPs.txt' in file_list:
    pass
else:
    with open('server_IPs.txt', 'w') as file:
        file.write("{'drive.google.com': '1', 'mail.google.com': '1', 'google.com': '1'}")

with open('server_IPs.txt', 'r') as file:
    servers = file.read()
    #print(servers)
    type = type(servers)
    #print(type)
    dict = ast.literal_eval(servers)
    old_IPs = dict
    new_IPs = dict
#    errors = []
    for key_new, value_new in new_IPs.items():
        for key_old, value_old in old_IPs.items():
            value_new = [socket.gethostbyname(key_new)]
            new_IPs[key_new] = value_new
            if value_new != value_old:
                print('[ERROR] ', key_new, ' IP mismatch: ', value_old, ' - ', value_new, '\n')
#                error = "'[ERROR] ', key_new, ' IP mismatch: ', value_old, ' - ', value_new, '\n'"
#                errors.append(error)
#    unique_error_list = []
#    for i in errors:
#        if i not in errors:
#            unique_error_list.append(i)
#    print(unique_error_list)
#    error_message = "\n".join(str(x) for x in unique_error_list)
    print(new_IPs)
#    print(error_message)
    result = str(new_IPs)
    with open('server_IPs.txt', 'w') as old_file:
        old_file.write(result)
    with open('server_IPs.json', 'w') as json_file:
        json_file.write(json.dumps(new_IPs))
    with open('server_IPs.yaml', 'w') as yaml_file:
        yaml_file.write(yaml.dump(new_IPs))