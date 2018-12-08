from pytz import timezone
from datetime import datetime
import time as tm
import numpy as np
import socket, sys, json, random, yaml, signal

if(len(sys.argv) != 2):
    print('Usage: ".py [path to json config file]"')
    sys.exit()

def signal_handler(sig, frame):
        print('You pressed Ctrl+C!')
        for i in range(len(socketList)):
            socketList[i].close()
        #print(socketList)
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

PATH = sys.argv[1]
configFile = open(PATH, "r");
configDict = yaml.load(configFile.read())

host = configDict["host"]
region = configDict["region"]
dstIp = configDict["dstIp"]
dstPort = configDict["dstPort"]
numberOfData = configDict["numberOfData"]
numberOfSocket = configDict["numberOfSocket"];
sleepTime = configDict["sleepTime"]

measurement = "temperature"
mu, sigma = 25, 10
socketList = []

if numberOfSocket > 1:
    i = 0;
    while True:
        if i < numberOfSocket:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((dstIp, dstPort))
            socketList.append(s)
            print("socket %d connected" % s.fileno())
            i += 1

elif numberOfSocket == 1:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((dstIp, dstPort))
    for i in range(numberOfData):
    
        time = datetime.now(timezone('Asia/Tokyo'))
        #temperature = int(np.random.normal(mu, sigma, 1))
        temperature = random.randint(0,100)
    
        json_body = {
            "measurement": measurement,
            "tags": {
                "host": host,
                "region": region
            },
            "time": str(time),
            "fields": {
                "value": temperature,
            }
        }
    
        msg = json.dumps(json_body)
        msg += "\n"
    
        s.send(msg.encode('utf-8'))
        tm.sleep(sleepTime)

    s.close()