import can
import time

# Simple CAN receiver program
bus = can.Bus(channel='vcan0', interface='socketcan', bitrate=500000)
start = time.time()
while True:
    message = bus.recv(timeout=0.05)
    if message: print(message)

