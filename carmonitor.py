#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 00:58:21 2022

@author: fmuzi
"""

import obd, time, json
from datetime import datetime

def retrieve_value(metric):
    time.sleep(.2)
    return connection.query(obd.commands[metric]).value

connection = obd.OBD("/dev/ttys002", baudrate=(9600)) # auto-connects to USB or RF port
supported_command_list=list(connection.supported_commands)

for x in range(len(supported_command_list)):
    print(supported_command_list[x])

print(retrieve_value("GET_DTC"))

for i in range(10):
    x = {
        "timestamp": f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')}",
        "MAF": f'{retrieve_value("MAF")}',
        "ENGINE_LOAD": f'{retrieve_value("ENGINE_LOAD")}',
        "INTAKE_PRESSURE": f'{retrieve_value("INTAKE_PRESSURE")}',
        "O2_SENSORS": f'{retrieve_value("O2_SENSORS")}',
        "SPEED": f'{retrieve_value("SPEED")}'
    }
    y = json.dumps(x)
    print(y)
    time.sleep(.1)

