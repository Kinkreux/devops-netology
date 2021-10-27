Домашнее задание к занятию "4.3. Языки разметки JSON и YAML"
Марина Пустовит

**1. Мы выгрузили JSON, который получили через API запрос к нашему сервису:**

````
{ "info" : "Sample JSON output from our service\t",
    "elements" :[
        { "name" : "first",
        "type" : "server",
        "ip" : 7175 
        },
        { "name" : "second",
        "type" : "proxy",
        "ip : 71.78.22.43
        }
    ]
}
````
**Нужно найти и исправить все ошибки, которые допускает наш сервис**

Исправленная версия. Для себя разнесла по строчкам все скобки, чтобы не запутаться. Видела такую запись раньше.
В IP добавила точки, потому что что это за IP без точек.

````
{
  "info": "Sample JSON output from our service\t",
  "elements" : [
        {
          "name": "first",
          "type": "server",
          "ip": "7.1.7.5"
        },
        
        {
          "name": "second",
          "type": "proxy",
          "ip": "71.78.22.43"
        }
              ]
}
````

Проверила эту версию валидатором, он скушал с удовольствием.


**2. В прошлый рабочий день мы создавали скрипт, позволяющий опрашивать веб-сервисы и получать их IP. К уже реализованному функционалу нам нужно добавить возможность записи JSON и YAML файлов, описывающих наши сервисы. Формат записи JSON по одному сервису: { "имя сервиса" : "его IP"}. Формат записи YAML по одному сервису: - имя сервиса: его IP. Если в момент исполнения скрипта меняется IP у сервиса - он должен так же поменяться в yml и json файле.**

Вроде более-менее я победила эту штуку. Да, ошибки сыпятся по 3 штуки (я думаю, цикл проверки на совпадение IP сделан неоптимально, стоило сравнивать попарно, но я уже боюсь переделывать). И да, красивый вывод я не осилила, пробовала много всякого разного, в т.ч. стороннего. Увы.

Закомментированные строки отражают мою попытку вывести уникальные ошибки, но я потерпела фиаско.

Первая ходка файла всегда дает ошибку, потому что там стоят 1 вместо IP. Но у меня все ходки давали ошибки, потому что IP во всех трех сервисах постоянно меняется))

````
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
````