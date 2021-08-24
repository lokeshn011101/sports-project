import time
import os
import cv2
import sys
import matplotlib.pyplot as plt


def extract_frames():
    # Chrono
    start_time = time.time()

    cap = cv2.VideoCapture('./data/videos/468477648.mp4')
    length_video = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_number = 0

    # Check if video uploaded
    if not cap.isOpened():
        sys.exit("Unable to open the video, check the path.\n")

    while frame_number < length_video:
        _, rgb = cap.read()

        if _ == 1:

            cv2.imwrite('./468477648' + str('%08d.png' % frame_number), rgb)
            frame_number += 1
        else:
            print("error")
            break
    cap.release()
    print(-start_time + time.time())


extract_frames()
