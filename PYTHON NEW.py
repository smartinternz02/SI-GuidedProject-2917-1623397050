import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "l9v8q5",
        "typeId": "iotdevice",
        "deviceId":"1001"
    },
    "auth": {
        "token": "123456789"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    temp=random.randint(-20,125)
    hum=random.randint(0,100)
    id1=12345
    id2=98672
    id3=13245   
    myData={'ID1':id1, 'ID2':id2, 'ID3':id3 }
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
