# obd

pip install obd

added
  delay=0.1
under 
  Python39\Lib\site-packages\obd\elm327.py
  def __send


c:\Temp\personal>python carmonitor.py
Press Enter to continue...
b'024C': DTC Commanded throttle actuator
b'063D': Purge Flow Monitor
b'0249': DTC Accelerator pedal position D
b'0602': O2 Sensor Monitor Bank 1 - Sensor 2
b'022F': DTC Fuel Level Input
b'0642': O2 Sensor Heater Monitor Bank 1 - Sensor 2
b'0111': Throttle Position
b'0149': Accelerator pedal position D
b'0232': DTC Evaporative system vapor pressure
b'06A0': Supported MIDs [A1-C0]
b'0220': DTC Supported PIDs [21-40]
b'0131': Distance traveled since codes cleared
b'0108': Short Term Fuel Trim - Bank 2
b'0247': DTC Absolute throttle position B
b'0230': DTC Number of warm-ups since codes cleared
b'0242': DTC Control module voltage
b'024E': DTC Time since trouble codes cleared
b'0228': DTC 02 Sensor 5 WR Lambda Voltage
b'023C': DTC Catalyst Temperature: Bank 1 - Sensor 1
b'020D': DTC Vehicle Speed
b'0204': DTC Calculated Engine Load
b'0600': Supported MIDs [01-20]
b'06A7': Misfire Cylinder 6 Data
b'011F': Engine Run Time
b'0207': DTC Long Term Fuel Trim - Bank 1
b'0620': Supported MIDs [21-40]
b'0206': DTC Short Term Fuel Trim - Bank 1
b'03': Get DTCs
b'0240': DTC Supported PIDs [41-60]
b'0622': Catalyst Monitor Bank 2
b'0133': Barometric Pressure
b'0142': Control module voltage
b'0636': VVT Monitor Bank 2
b'020C': DTC Engine RPM
b'0233': DTC Barometric Pressure
b'022E': DTC Commanded Evaporative Purge
b'06A3': Misfire Cylinder 2 Data
b'0245': DTC Relative throttle position
b'010F': Intake Air Temp
b'0601': O2 Sensor Monitor Bank 1 - Sensor 1
b'06A6': Misfire Cylinder 5 Data
b'013C': Catalyst Temperature: Bank 1 - Sensor 1
b'0605': O2 Sensor Monitor Bank 2 - Sensor 1
b'0128': 02 Sensor 5 WR Lambda Voltage
b'0640': Supported MIDs [41-60]
b'010D': Vehicle Speed
b'024A': DTC Accelerator pedal position E
b'0203': DTC Fuel System Status
b'0243': DTC Absolute load value
b'010E': Timing Advance
b'0201': DTC Status since DTCs cleared
b'021F': DTC Engine Run Time
b'0221': DTC Distance Traveled with MIL on
b'0107': Long Term Fuel Trim - Bank 1
b'ATRV': Voltage detected by OBD-II adapter
b'0208': DTC Short Term Fuel Trim - Bank 2
b'063C': EVAP Monitor (0.020")
b'0104': Calculated Engine Load
b'0143': Absolute load value
b'0680': Supported MIDs [81-A0]
b'0224': DTC 02 Sensor 1 WR Lambda Voltage
b'0130': Number of warm-ups since codes cleared
b'011C': OBD Standards Compliance
b'014C': Commanded throttle actuator
b'0110': Air Flow Rate (MAF)
b'014E': Time since trouble codes cleared
b'0210': DTC Air Flow Rate (MAF)
b'0100': Supported PIDs [01-20]
b'021C': DTC OBD Standards Compliance
b'012F': Fuel Level Input
b'0105': Engine Coolant Temperature
b'0209': DTC Long Term Fuel Trim - Bank 2
b'0205': DTC Engine Coolant Temperature
b'0124': 02 Sensor 1 WR Lambda Voltage
b'010C': Engine RPM
b'0132': Evaporative system vapor pressure
b'0646': O2 Sensor Heater Monitor Bank 2 - Sensor 2
b'023D': DTC Catalyst Temperature: Bank 2 - Sensor 1
b'0213': DTC O2 Sensors Present
b'0141': Monitor status this drive cycle
b'0645': O2 Sensor Heater Monitor Bank 2 - Sensor 1
b'0147': Absolute throttle position B
b'04': Clear DTCs and Freeze data
b'0140': Supported PIDs [41-60]
b'06A1': Misfire Monitor General Data
b'014D': Time run with MIL on
b'0241': DTC Monitor status this drive cycle
b'0231': DTC Distance traveled since codes cleared
b'013D': Catalyst Temperature: Bank 2 - Sensor 1
b'0120': Supported PIDs [21-40]
b'063B': EVAP Monitor (0.040")
b'0219': DTC O2: Bank 2 - Sensor 2 Voltage
b'0621': Catalyst Monitor Bank 1
b'0681': Fuel System Monitor Bank 1
b'0215': DTC O2: Bank 1 - Sensor 2 Voltage
b'0244': DTC Commanded equivalence ratio
b'0121': Distance Traveled with MIL on
b'0144': Commanded equivalence ratio
b'0606': O2 Sensor Monitor Bank 2 - Sensor 2
b'020E': DTC Timing Advance
b'0660': Supported MIDs [61-80]
b'0635': VVT Monitor Bank 1
b'0106': Short Term Fuel Trim - Bank 1
b'0115': O2: Bank 1 - Sensor 2 Voltage
b'014A': Accelerator pedal position E
b'0109': Long Term Fuel Trim - Bank 2
b'020F': DTC Intake Air Temp
b'0119': O2: Bank 2 - Sensor 2 Voltage
b'012E': Commanded Evaporative Purge
b'06A5': Misfire Cylinder 4 Data
b'0682': Fuel System Monitor Bank 2
b'06A4': Misfire Cylinder 3 Data
b'07': Get DTCs from the current/last driving cycle
b'0103': Fuel System Status
b'0211': DTC Throttle Position
b'0101': Status since DTCs cleared
b'0145': Relative throttle position
b'0641': O2 Sensor Heater Monitor Bank 1 - Sensor 1
b'ATI': ELM327 version string
b'024D': DTC Time run with MIL on
b'0639': EVAP Monitor (Cap Off / 0.150")
b'06A2': Misfire Cylinder 1 Data
b'0113': O2 Sensors Present
Press Enter to continue...
[('P0101', 'Mass or Volume Air Flow Circuit Range/Performance')]
Press Enter to continue...
[obd.obd] 'b'010B': Intake Manifold Pressure' is not supported
{"timestamp": "2022-09-02 13:20:29.334572", "MAF": "3.0500000000000003 gps", "ENGINE_LOAD": "21.96078431372549 percent", "INTAKE_PRESSURE": "None", "O2_SENSORS": "((), (False, False, True, True), (False, False, True, True))", "SPEED": "0.0 kph"}
Press Enter to continue...
[obd.obd] 'b'010B': Intake Manifold Pressure' is not supported
{"timestamp": "2022-09-02 13:20:38.913931", "MAF": "3.0500000000000003 gps", "ENGINE_LOAD": "22.352941176470587 percent", "INTAKE_PRESSURE": "None", "O2_SENSORS": "((), (False, False, True, True), (False, False, True, True))", "SPEED": "0.0 kph"}

