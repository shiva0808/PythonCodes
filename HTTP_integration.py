import requests
import json

####################Setting JSON
USER_CRED = {"data": {"username": "shiva", "password": "xxxxxxxxxxxx", "port": "8980"}, "time": 1582226193364}
GET_PRECINT = {"time": 1586220883, "data": {"page_size": "5000", "page_no": "1"}}
GET_DEVICE = {"time": 1586220883, "data": {"page_size": "5000", "page_no": "1"}}
GET_DISCONNECT_DEVICE = {"time": 1586220883, "data": {"page_size": "5000", "page_no": "1"}}
HEART_BEAT = {}
####################Setting URL
URL_LOGIN = "http://127.0.0.1:8085/north/login"
URL_PRECINCT = "http://127.0.0.1:8085/north/get_precinct"
URL_DEVICE = "http://127.0.0.1:8085/north/get_device"
URL_DISCONNECT_DEVICE = "http://127.0.0.1:8085/north/get_disconnect_device"
URL_HEARTBEAT = "http://127.0.0.1:8085/north/heartbeat"

###################Login Code
RESP_LOGIN = requests.post(URL_LOGIN, data=json.dumps(USER_CRED))
RESP_CODE_LOGIN = RESP_LOGIN.status_code
#print(f"{RESP_CODE_LOGIN}")
if RESP_CODE_LOGIN == 200:
    print(RESP_LOGIN.json())
    RESPONSE_JSON_LOGIN = RESP_LOGIN.json()
else:
    print(f"error in getting login response {RESP_CODE_LOGIN}")

PASSWORD = RESPONSE_JSON_LOGIN['data']['token']
print(f"Auth Token : {PASSWORD}")

#########################Setting Password Token
HEADER = {"token": PASSWORD}

#######################Heart Beat
print("\n\nchecking heartbeat")
RESP_HEARTBEAT = requests.post(URL_HEARTBEAT, data=json.dumps(HEART_BEAT), headers=HEADER)
if RESP_HEARTBEAT.status_code == 200:
    print("heartbeat OK")
else:
    print("heart beat not ok")

#######################get_precint
RESP_PRECINT = requests.post(URL_PRECINCT, data=json.dumps(GET_PRECINT), headers=HEADER)
RESP_PRECINT_CODE=RESP_PRECINT.status_code
#print(f"{RESP_PRECINT_CODE}")
if RESP_PRECINT_CODE == 200:
    print("\n\n")
    print("Json for Precint")
    print(RESP_PRECINT.json())
    RESP_PRECINT_JSON = RESP_PRECINT.json()
else:
    print(f"error in getting response precint {RESP_PRECINT_CODE}")

PRECINT_LIST = []
#print(f"{RESP_PRECINT_JSON['data']['nodes'][1]['precinct_id']}")

for precint in RESP_PRECINT_JSON['data']['nodes']:
    #print(f"{precint['precinct_id']};{precint['precinct_kind']};{precint['precinct_name']};{precint['up_precinct_id']}")
    PRECINT_LIST.append(precint['precinct_id'])
print("\n\n\n\n")
print("printing precint")
print(f"{PRECINT_LIST}")                   #Enable printing of precint ID


#######################Send HeartBeat##################
print("\n\nchecking heartbeat")
RESP_HEARTBEAT = requests.post(URL_HEARTBEAT, data=json.dumps(HEART_BEAT), headers=HEADER)
if RESP_HEARTBEAT.status_code == 200:
    print("heartbeat OK")
else:
    print("heart beat not ok")

##################Code for getting Devices
RESP_DEVICE = requests.post(URL_DEVICE, data=json.dumps(GET_DEVICE), headers=HEADER)
RESP_DEVICE_CODE = RESP_DEVICE.status_code
#print(f"{RESP_PRECINT_CODE}")
if RESP_DEVICE_CODE == 200:
    print("\n\n\n printing device json")
    print(RESP_DEVICE.json())
    RESP_DEVICE_JSON = RESP_DEVICE.json()
else:
    print(f"error in getting response precint {RESP_PRECINT_CODE}")

#DEVICE_LIST = []
#DEVICE_PRECINT_ID = []
#print(f"{RESP_PRECINT_JSON['data']['nodes'][1]['precinct_id']}")

#for device in RESP_DEVICE_JSON['data']['nodes']:
    #print(f"{precint['precinct_id']};{precint['precinct_kind']};{precint['precinct_name']};{precint['up_precinct_id']}")
#    DEVICE_LIST.append(device['device_id'])
#    DEVICE_PRECINT_ID.append(device['precinct_id'])

#Print("Printing Device an Device PreceintID")
#print(f"{DEVICE_LIST}")
#print(f"{DEVICE_PRECINT_ID}")

#######################Send HeartBeat##################
print("\n\nchecking heartbeat")
RESP_HEARTBEAT = requests.post(URL_HEARTBEAT, data=json.dumps(HEART_BEAT), headers=HEADER)
if RESP_HEARTBEAT.status_code == 200:
    print("heartbeat OK")
else:
    print("heart beat not ok")

################################Precint and Device Mapping in CSV#####
print("\n\n\nCSV for device and precint infomation")
print(f"pricintID,DeviceID,DeviceName,DeviceType,DeviceTypeName,PrecintID")
for precint in PRECINT_LIST:
    #print(f"Devices under precint ID {precint}")
    x = 0
    for device in RESP_DEVICE_JSON['data']['nodes']:
        #print(device['precinct_id'], precint)
        if device['precinct_id'] == precint:
            x += 1
            print(f"{precint}, {device['device_id']}, {device['device_name']}, {device['device_type']}, {device['device_type_name']}, {device['precinct_id']}")
    if x == 0:
        print(f"no device found under {precint}")

#######################Send HeartBeat##################
print("\n\nchecking heartbeat")
RESP_HEARTBEAT = requests.post(URL_HEARTBEAT, data=json.dumps(HEART_BEAT), headers=HEADER)
if RESP_HEARTBEAT.status_code == 200:
    print("heartbeat OK")
else:
    print("heart beat not ok")

#############################Code for Get Disconnect Device#######################
RESP_DISCONNECT_DEVICE = requests.post(URL_DISCONNECT_DEVICE, data=json.dumps(GET_DISCONNECT_DEVICE), headers=HEADER)
RESP_DISCONNECT_DEVICE_CODE = RESP_PRECINT.status_code
#print(f"{RESP_PRECINT_CODE}")
if RESP_DISCONNECT_DEVICE_CODE == 200:
    print("\n\n")
    print("Json for Disconnected Device")
    print(RESP_DISCONNECT_DEVICE.json())
    RESP_DISCONNECT_DEVICE_JSON = RESP_DISCONNECT_DEVICE.json()
else:
    print(f"error in getting response precint {RESP_PRECINT_CODE}")


DISCONNECT_DEVICE_LIST = RESP_DISCONNECT_DEVICE_JSON["data"]["device_ids"].split(",")

print(f"printing Disconnected Device \n {DISCONNECT_DEVICE_LIST}")

