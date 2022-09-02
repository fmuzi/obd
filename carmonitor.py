#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 00:58:21 2022

@author: fmuzi
"""

import obd, time, json
from datetime import datetime

lst_once=["FUEL_STATUS","O2_SENSORS","RUN_TIME_MIL","TIME_SINCE_DTC_CLEARED","DTC_STATUS","DTC_ENGINE_LOAD","DTC_RPM","DTC_SPEED","DTC_MAF","DTC_THROTTLE_POS","DTC_O2_SENSORS","DTC_O2_B1S2","DTC_O2_B2S2","DTC_RUN_TIME","DTC_DISTANCE_W_MIL","DTC_DISTANCE_SINCE_DTC_CLEAR","DTC_THROTTLE_POS_B","DTC_RUN_TIME_MIL","DTC_TIME_SINCE_DTC_CLEARED","GET_DTC"]


def retrieve_value(metric):
    time.sleep(.5)
    return connection.query(obd.commands[metric]).value

#connection = obd.OBD() # auto-connects to USB or RF port
#connection = obd.OBD("/dev/ttys004", baudrate=(9600)) # MacOS
connection = obd.OBD('COM7', fast=False, timeout=30) # Windows

supported_command_list=list(connection.supported_commands)

for x in range(len(supported_command_list)):
    scl_vars=vars(supported_command_list[x])
    print(f"{scl_vars.get('command')}\t{scl_vars.get('name')}\t{scl_vars.get('desc')}\t{scl_vars.get('ecu')}")

print(retrieve_value("GET_DTC"))

input("Press Enter to continue...")

for j in lst_once:
    item_resp=retrieve_value(j)
    x = {
        "timestamp": f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')}",
        f"{j}": f'{item_resp}'
    }
    y = json.dumps(x)
    print(y)

for i in range(150):
    x = {
        "timestamp": f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')}",
        "MAF": f'{retrieve_value("MAF")}',
        "ENGINE_LOAD": f'{retrieve_value("ENGINE_LOAD")}',
        "RPM": f'{retrieve_value("RPM")}',
        "O2_B1S2": f'{retrieve_value("O2_B1S2")}',
        "O2_B2S2": f'{retrieve_value("O2_B2S2")}',
        "THROTTLE_POS": f'{retrieve_value("THROTTLE_POS")}',
        "SPEED": f'{retrieve_value("SPEED")}'
    }
    y = json.dumps(x)
    print(y)
    time.sleep(1)
