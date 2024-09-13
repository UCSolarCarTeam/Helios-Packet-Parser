data =[
    {
        "DriverControls": [
            {"Name": "PackageID", "Offset": 0, "Type": "uchar", "Unit": "", "detail": "ID=4"},
            {"Name": "DriverControlsBoardAlive", "Offset":1, "Type":"uchar", "Unit":"boolean","detail":""},
            {"Name": "LightsInputs", "Offset":2, "Type":"uchar", "Unit":"bitflag", "detail": [  { "0x01": "Headlights Off" },
  { "0x02": "Headlights Low" },
  { "0x04": "Headlights High" },
  { "0x08": "Signal Right" },
  { "0x10": "Signal Left" },
  { "0x20": "Hazard" },
  { "0x40": "Interior" }]},
            {"Name": "MusicInputs", "Offset":3,"Type":"uchar","Unit":"bitflag","detail": [{ "0x01": "Volume Up" },
  { "0x02": "Volume Down" },
  { "0x04": "Next Song" },
  { "0x08": "Previous Song" }]},
            {"Name": "Acceleration", "Offset": 4, "Type": "short uint", "Unit": "12bit uint", "detail": ""},
            {"Name": "RegenBraking", "Offset": 6, "Type": "short uint", "Unit": "12bit uint", "detail": "" },
            {"Name": "DriverInputs", "Offset": 8, "Type": "uchar", "Unit": "bitflag", "detail": [ { "0x01": "Brakes" },
  { "0x02": "Forward" },
  { "0x04": "Reverse" },
  { "0x08": "Push To Talk" },
  { "0x10": "Horn" },
  { "0x20": "Reset" },
  { "0x40": "Aux" },
  { "0x80": "Lap"}]},
        ]
    },
#     {
#     "MotorFaults": [
#         {"Name": "M0 Error Flags", "Offset": 1, "Type": "uchar", "Unit": "bitflag", "detail": [
#             {"0x01": "Motor Over Speed"},
#             {"0x02": "Software Over Current"},
#             {"0x04": "Dc Bus Over Voltage"},
#             {"0x08": "Bad Motor Position Hall Sequence"},
#             {"0x10": "Watchdog Caused Last Reset"},
#             {"0x20": "Config Read Error"},
#             {"0x40": "Rail Under Voltage Lock Out"},
#             {"0x80": "Desaturation Fault"}
#         ]},
#         {"Name": "M1 Error Flags", "Offset": 2, "Type": "uchar", "Unit": "bitflag", "detail": [
#             {"0x01": "Motor Over Speed"},
#             {"0x02": "Software Over Current"},
#             {"0x04": "Dc Bus Over Voltage"},
#             {"0x08": "Bad Motor Position Hall Sequence"},
#             {"0x10": "Watchdog Caused Last Reset"},
#             {"0x20": "Config Read Error"},
#             {"0x40": "Rail Under Voltage Lock Out"},
#             {"0x80": "Desaturation Fault"}
#         ]},
#         {"Name": "M0 Limit Flags", "Offset": 3, "Type": "uchar", "Unit": "bitflag", "detail": [
#             {"0x01": "Output Voltage Pwm Limit"},
#             {"0x02": "Motor Current Limit"},
#             {"0x04": "Velocity Limit"},
#             {"0x08": "Bus Current Limit"},
#             {"0x10": "Bus Voltage Upper Limit"},
#             {"0x20": "Bus Voltage Lower Limit"},
#             {"0x40": "Ipm Or Motor Temperature Limit"}
#         ]},
#         {"Name": "M1 Limit Flags", "Offset": 4, "Type": "uchar", "Unit": "bitflag", "detail": [
#             {"0x01": "Output Voltage Pwm Limit"},
#             {"0x02": "Motor Current Limit"},
#             {"0x04": "Velocity Limit"},
#             {"0x08": "Bus Current Limit"},
#             {"0x10": "Bus Voltage Upper Limit"},
#             {"0x20": "Bus Voltage Lower Limit"},
#             {"0x40": "Ipm Or Motor Temperature Limit"}
#         ]},
#         {"Name": "M0 Can Rx Error Count", "Offset": 5, "Type": "uchar", "Unit": "#", "detail": ""},
#         {"Name": "M0 Can Tx Error Count", "Offset": 6, "Type": "uchar", "Unit": "#", "detail": ""},
#         {"Name": "M1 Can Rx Error Count", "Offset": 7, "Type": "uchar", "Unit": "#", "detail": ""},
#         {"Name": "M1 Can Tx Error Count", "Offset": 8, "Type": "uchar", "Unit": "#", "detail": ""}
#     ]
# },
{"AuxBms":[
    {
    "Name": "PackageID",
    "Offset": 0,
    "Type": "uchar",
    "Unit": "-",
    "detail": [
        {"ID=11": ""}
    ]
    },
    {
    "Name": "Precharge State",
    "Offset": 1,
    "Type": "uchar",
    "Unit": "flag",
    "detail": [
        {"0": "OFF"},
        {"1": "COMMON_ENGAGED"},
        {"2": "CHARGE_ENGAGED"},
        {"3": "DISCHARGE_ENGAGED"},
        {"4": "ALL_ENGAGED"},
        {"5": "INVALID_STATE"}
    ]
    },
    {
    "Name": "Aux Voltage",
    "Offset": 2,
    "Type": "uchar",
    "Unit": "mV",
    "detail": []
    },
    {
    "Name": "Aux Bms Alive",
    "Offset": 3,
    "Type": "uchar",
    "Unit": "Boolean",
    "detail": []
    },
    {
    "Name": "Strobe Bms Light",
    "Offset": 4,
    "Type": "uchar",
    "Unit": "Boolean",
    "detail": []
    },
    {
    "Name": "Allow Charge",
    "Offset": 5,
    "Type": "uchar",
    "Unit": "Boolean",
    "detail": []
    },
    {
    "Name": "High Voltage Enable State",
    "Offset": 6,
    "Type": "uchar",
    "Unit": "Boolean",
    "detail": []
    },
    {
    "Name": "Allow Discharge",
    "Offset": 7,
    "Type": "uchar",
    "Unit": "Boolean",
    "detail": []
    },
    {
    "Name": "Orion Can Received Recently",
    "Offset": 8,
    "Type": "uchar",
    "Unit": "Boolean",
    "detail": []
    },
    {
    "Name": "Aux Contactor Debug Info",
    "Offset": 9,
    "Type": "uchar",
    "Unit": "bitflag",
    "detail": [
        {"0x01": "Charge Contactor Error"},
        {"0x02": "Discharge Contactor Error"},
        {"0x04": "Common Contactor Error"},
        {"0x08": "Discharge Should Trip"},
        {"0x10": "Charge Should Trip"},
        {"0x20": "Charge Open But Should Be Closed"},
        {"0x40": "Discharge Open But Should Be Closed"}
    ]
    },
    {
    "Name": "Aux Trip",
    "Offset": 10,
    "Type": "short uint",
    "Unit": "bitflag",
    "detail": [
        {"0x0001": "Charge Trip Due To High Cell Voltage"},
        {"0x0002": "Charge Trip Due To High Temperature And Current"},
        {"0x0004": "Charge Trip Due To Pack Current"},
        {"0x0008": "Discharge Trip Due To Low Cell Voltage"},
        {"0x0010": "Discharge Trip Due To High Temperature And Current"},
        {"0x0020": "Discharge Trip Due To Pack Current"},
        {"0x0040": "Protection Trip"},
        {"0x0080": "Trip Due To Orion Message Timeout"},
        {"0x0100": "Charge Not Closed Due To High Current"},
        {"0x0200": "Discharge Not Closed Due To High Current"},
        {"0x0400": "Trip Due To Contactor Disconnected Unexpectedly"}
    ]
    },
    ]
},
# {"BatteryFaults":[
#     {
#     "Name": "Error Flags",
#     "Offset": 1,
#     "Type": "uint",
#     "Unit": "bitflag",
#     "detail": [
#         {"0x00000001": "Internal Communication Fault"},
#         {"0x00000002": "Internal Conversion Fault"},
#         {"0x00000004": "Weak Cell Fault"},
#         {"0x00000008": "Low Cell Voltage Fault"},
#         {"0x00000010": "Open Wiring Fault"},
#         {"0x00000020": "Current Sensor Fault"},
#         {"0x00000040": "Pack Voltage Sensor Fault"},
#         {"0x00000080": "Weak Pack Fault"},
#         {"0x00000100": "Voltage Redundancy Fault"},
#         {"0x00000200": "Fan Monitor Fault"},
#         {"0x00000400": "Thermistor Fault"},
#         {"0x00000800": "Canbus Communications Fault"},
#         {"0x00001000": "Always On Supply Fault"},
#         {"0x00002000": "High Voltage Isolation Fault"},
#         {"0x00004000": "Power Supply 12V Fault"},
#         {"0x00008000": "Charge Limit Enforcement Fault"},
#         {"0x00010000": "Discharge Limit Enforcement Fault"},
#         {"0x00020000": "Charger Safety Relay Fault"},
#         {"0x00040000": "Internal Memory Fault"},
#         {"0x00080000": "Internal Thermistor Fault"},
#         {"0x00100000": "Internal Logic Fault"}
#     ]
# },
# {
#     "Name": "Limit Flags",
#     "Offset": 4,
#     "Type": "short uint",
#     "Unit": "bitflag",
#     "detail": [
#         {"0x0001": "Dcl Reduced Due To Low Soc"},
#         {"0x0002": "Dcl Reduced Due To High Cell Resistence"},
#         {"0x0004": "Dcl Reduced Due To Temperature"},
#         {"0x0008": "Dcl Reduced Due To Low Cell Voltage"},
#         {"0x0010": "Dcl Reduced Due To Low Pack Voltage"},
#         {"0x0040": "Dcl And Ccl Reduced Due To Voltage Failsafe"},
#         {"0x0080": "Dcl And Ccl Reduced Due To Communication Failsafe"},
#         {"0x0200": "Ccl Reduced Due To High Soc"},
#         {"0x0400": "Ccl Reduced Due To High Cell Resistence"},
#         {"0x0800": "Ccl Reduced Due To Temperature"},
#         {"0x1000": "Ccl Reduced Due To High Cell Voltage"},
#         {"0x2000": "Ccl Reduced Due To High Pack Voltage"},
#         {"0x4000": "Ccl Reduced Due To Charger Latch"},
#         {"0x8000": "Ccl Reduced Due To Alternate Current Limit"}
#     ]
# }
# ]},
 {
    "Lights":
    [
    {
    "Name": "Lights Alive",
    "Offset": 1,
    "Type": "uchar",
    "Unit": "Boolean",
    "detail": [
        {"0": "Off"},
        {"1": "On"}
    ]
    },
    {
        "Name": "Lights Status",
        "Offset": 2,
        "Type": "uchar",
        "Unit": "bitflag",
        "detail": [
            {"0x01": "Low Beams"},
            {"0x02": "High Beams"},
            {"0x04": "Brake Lights"},
            {"0x08": "Left Signal"},
            {"0x10": "Right Signal"},
            {"0x20": "Bms Strobe Light"}
        ]
    }
    ]
},
# {
#     "MotorDetails": [
#         {
#             "Name": "M0 Alive",
#             "Offset": 1,
#             "Type": "uchar",
#             "Unit": "boolean",
#             "detail": [
#                 {"0x01": "Alive"}
#             ]
#         },
#         {
#             "Name": "M0 Set Current",
#             "Offset": 2,
#             "Type": "float",
#             "Unit": "%"
#         },
#         {
#             "Name": "M0 Set Velocity",
#             "Offset": 6,
#             "Type": "float",
#             "Unit": "RPM"
#         },
#         {
#             "Name": "M0 Bus Current",
#             "Offset": 10,
#             "Type": "float",
#             "Unit": "A"
#         },
#         {
#             "Name": "M0 Bus Voltage",
#             "Offset": 14,
#             "Type": "float",
#             "Unit": "V"
#         },
#         {
#             "Name": "M0 Vehicle Velocity",
#             "Offset": 18,
#             "Type": "float",
#             "Unit": "m/s"
#         },
#         {
#             "Name": "M1 Alive",
#             "Offset": 22,
#             "Type": "uchar",
#             "Unit": "boolean",
#             "detail": [
#                 {"0x01": "Alive"}
#             ]
#         },
#         {
#             "Name": "M1 Set Current",
#             "Offset": 23,
#             "Type": "float",
#             "Unit": "%"
#         },
#         {
#             "Name": "M1 Set Velocity",
#             "Offset": 27,
#             "Type": "float",
#             "Unit": "RPM"
#         },
#         {
#             "Name": "M1 Bus Current",
#             "Offset": 31,
#             "Type": "float",
#             "Unit": "A"
#         },
#         {
#             "Name": "M1 Bus Voltage",
#             "Offset": 35,
#             "Type": "float",
#             "Unit": "V"
#         },
#         {
#             "Name": "M1 Vehicle Velocity",
#             "Offset": 39,
#             "Type": "float",
#             "Unit": "m/s"
#         }
#     ]
# },
# {
#     "BatteryDetails": [
#         {
#             "Name": "BMU Alive",
#             "Offset": 1,
#             "Type": "uchar",
#             "Unit": "Boolean"
#         },
#         {
#             "Name": "BMS Relay Status",
#             "Offset": 2,
#             "Type": "uchar",
#             "Unit": "bitflag",
#             "detail": [
#                 {"0x01": "Discharge relay enabled"},
#                 {"0x02": "Charge relay enabled"},
#                 {"0x04": "Charger safety enabled"},
#                 {"0x08": "Malfunction indicator active (DTC status)"},
#                 {"0x10": "Multi-Purpose Input signal status"},
#                 {"0x20": "Always-on signal status"},
#                 {"0x40": "Is-Ready signal status"},
#                 {"0x80": "Is-Charging signal status"}
#             ]
#         },
#         {
#             "Name": "Populated Cells",
#             "Offset": 3,
#             "Type": "uchar",
#             "Unit": "#"
#         },
#         {
#             "Name": "12v Input Voltage",
#             "Offset": 4,
#             "Type": "float",
#             "Unit": "0.1 V"
#         },
#         {
#             "Name": "Fan Voltage",
#             "Offset": 8,
#             "Type": "float",
#             "Unit": "0.01 V"
#         },
#         {
#             "Name": "Pack Current",
#             "Offset": 12,
#             "Type": "float",
#             "Unit": "0.1 A"
#         },
#         {
#             "Name": "Pack Voltage",
#             "Offset": 16,
#             "Type": "float",
#             "Unit": "0.1 V"
#         },
#         {
#             "Name": "Pack State of Charge",
#             "Offset": 20,
#             "Type": "float",
#             "Unit": "0.5 %"
#         },
#         {
#             "Name": "Pack Amphours",
#             "Offset": 24,
#             "Type": "float",
#             "Unit": "0.1 Ah"
#         },
#         {
#             "Name": "Pack Depth of Discharge (DOD)",
#             "Offset": 28,
#             "Type": "float",
#             "Unit": "0.5 %"
#         },
#         {
#             "Name": "High Temperature",
#             "Offset": 32,
#             "Type": "uchar",
#             "Unit": "°C"
#         },
#         {
#             "Name": "High Thermistor ID",
#             "Offset": 33,
#             "Type": "uchar",
#             "Unit": "#"
#         },
#         {
#             "Name": "Low Temperature",
#             "Offset": 34,
#             "Type": "uchar",
#             "Unit": "°C"
#         },
#         {
#             "Name": "Low Thermistor ID",
#             "Offset": 35,
#             "Type": "uchar",
#             "Unit": "#"
#         },
#         {
#             "Name": "Average Temperature",
#             "Offset": 36,
#             "Type": "uchar",
#             "Unit": "°C"
#         },
#         {
#             "Name": "Internal Temperature",
#             "Offset": 37,
#             "Type": "uchar",
#             "Unit": "°C"
#         },
#         {
#             "Name": "Fan Speed",
#             "Offset": 38,
#             "Type": "uchar",
#             "Unit": "# (0 - 6 Speed)"
#         },
#         {
#             "Name": "Requested Fan Speed",
#             "Offset": 39,
#             "Type": "uchar",
#             "Unit": "# (0 - 6 Speed)"
#         },
#         {
#             "Name": "Low Cell Voltage",
#             "Offset": 40,
#             "Type": "short uint",
#             "Unit": "0.1 mV"
#         },
#         {
#             "Name": "Low Cell Voltage ID",
#             "Offset": 42,
#             "Type": "uchar",
#             "Unit": "#"
#         },
#         {
#             "Name": "High Cell Voltage",
#             "Offset": 43,
#             "Type": "short uint",
#             "Unit": "0.1 mV"
#         },
#         {
#             "Name": "High Cell Voltage ID",
#             "Offset": 45,
#             "Type": "uchar",
#             "Unit": "#"
#         },
#         {
#             "Name": "Average Cell Voltage",
#             "Offset": 46,
#             "Type": "short uint",
#             "Unit": "0.1 mV"
#         }
#     ]
# }
]