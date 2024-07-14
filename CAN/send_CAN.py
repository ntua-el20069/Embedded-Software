import can
import time

'''
# Firstly, you need to create a virtual CAN interface by these commands in Linux terminal:
# You can detect the CAN messages in vcan0 channel by using Wireshark 
sudo modprobe vcan
# Create a vcan network interface with a specific name
sudo ip link add dev vcan0 type vcan
sudo ip link set vcan0 up
'''

# program to send CAN messages
bus = can.interface.Bus(interface='socketcan', channel='vcan0', bitrate=500000)
counter = 0
while True:
    time.sleep(0.5)
    counter += 1
    msg = can.Message(
        arbitration_id=0xC0FFEE,
        data=[ counter % x for x in [4, 5, 2, 6, 7, 10, 14, 11] ],
        is_extended_id=True
    )
    if counter % 10 < 4: msg = can.Message(is_error_frame=True) # for the 40% of the time, send an error frame
    
    try:
        bus.send(msg)
        print(f"Message sent on {bus.channel_info}: {msg}")
    except can.CanError:
        print("#####  Message NOT sent  #####")

# Close the bus (if you do not use infinite loop)
bus.shutdown()