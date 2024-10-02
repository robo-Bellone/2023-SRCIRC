import time
import cv2
import numpy as np

from Drive_motors import *
from config import *
from vis_utils import *
from utils import *

r_lower, r_upper = color_getter(cam_name, 'r')
g_lower, g_upper = color_getter(cam_name, 'g')
b_lower, b_upper = color_getter(cam_name, 'b')

def basketBall():
    camera = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    flag = 0
    move_motor(neck_UD, 237)
    move_motor(neck_LR, 180)
    send_txt(CLAP)
    time.sleep(1)

    tag = 0

    while True:
        frame = grab_frame(camera)
        r_channel, r_mask = filter_hsv(frame, r_lower, r_upper)
        g_channel, g_mask = filter_hsv(frame, g_lower, g_upper)
        b_channel, b_mask = filter_hsv(frame, b_lower, b_upper)

        if flag == 0:
            send_txt(WALK_FORWARD)
            time.sleep(1)
            if masked_channel_perc(b_mask) > 5.0:
                flag = 1

        elif flag == 1:
            for i in range(3):
                send_txt(WALK_SLIGHT)
                time.sleep(1)
            flag = 2

        elif flag == 2:
            move_motor(neck_UD, 170)
            move_motor(neck_UD, 170)
            time.sleep(0.7)
            waise_angle = 180
            flag = 3
        
        elif flag == 3:
            send_txt(THROW_STEADY)
            time.sleep(1)
            flag = 4
        elif flag == 4:
            cX, _, _ = weighted_sum_moment(get_contours(b_mask))
            if (X_size/2) - cX < 5:
                waist_angle = waise_angle - 1
                move_motor(waist_LR, waist_angle)
                tag = 0
                time.sleep(0.1)
            elif (X_size/2) - cX > 5:
                waist_angle = waise_angle + 1
                move_motor(waist_LR, waist_angle)
                tag = 0
                time.sleep(0.8)
            else:
                tag = tag + 1
                if tag > 10:
                    flag = 5

        elif flag == 5:
            move_motor(right_arm_UD, 153)
            move_motor(left_arm_UD, 3)
            move_motor(right_ankle, 293)
            time.sleep(5)
        else:
            print("finished")
