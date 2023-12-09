import asyncio
import random

sensor1 = 0
sensor2 = 0
sensor3 = 0
sensor4 = 0
sensor5 = 0
sensor6 = 0
sensor7 = 0

async def upSensor1(var):
    while True:
        var = random.randrange(0,100)
        await asyncio.sleep(1)

# loop1 = asyncio.get_event_loop()

def getSensor1(sensor):
    asyncio.ensure_future(upSensor1(sensor))
    # loop1.run_forever()

def getSensor2():
    global sensor2
    return sensor2

def getSensor3():
    global sensor3
    return sensor3

def getSensor4():
    global sensor4
    return sensor4

def getSensor5():
    global sensor5
    return sensor5

def getSensor6():
    global sensor6
    return sensor6

def getSensor7():
    global sensor7
    return sensor7