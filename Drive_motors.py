import time
import numpy as np
import serial
from config import state_comm

class nothing:
    def write(str, str2):
        pass


if state_comm == 0:
    s = serial.Serial(port='COM5',baudrate=115200)
elif state_comm == 1:
    s = serial.Serial(port='COM7',baudrate=115200)
else:
    s = nothing()


def move_motor(id, a , s = s):
    a = int((a * 55) + 20000)
    id = format(id, '02')
    mv_data = f'PS000{id},{a};'
    s.write(mv_data.encode())
    #print(f'S: {mv_data}')
    time.sleep(0.01)
    '''print(f'R : {s.readline()}')
    time.sleep(0.0001)'''


def move_to_point(arr, s = s, t = 10):
    for idx, ang in arr:
        idx = format(idx, '02')
        ang = (ang * 55) + 20000
        ud_data = f'SP00039,000{idx},{ang};'
        s.write(ud_data.encode())
        time.sleep(0.01)
    t = format(t,'05')
    ud_data = f'PP00039,{t}'
    print(f'S : {ud_data}')
    time.sleep(0.01)
    '''print(f'R : {s.readline()}')
    time.sleep(0.0001)'''

def move_motors(arr, s = s ):
    for idx,ang in arr:
        idx = format(idx, '02')
        ud_data = f'PS000{idx},{ang}'
        s.write(ud_data.encode)
        time.sleep(0.01)

def send_txt(msg_c, s = s):
    s.write(msg_c.encode())
    print(f'S: {msg_c}')


