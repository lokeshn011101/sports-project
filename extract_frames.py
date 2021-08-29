import time
import os
import cv2
import sys
import matplotlib.pyplot as plt
import torch

# or yolov5m, yolov5l, yolov5x, custom
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')


def extract_frames(video_name):
    start_time = time.time()

    cap = cv2.VideoCapture(f'./data/videos/{video_name}.mp4')
    length_video = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_number = 0

    # Check if video uploaded
    if not cap.isOpened():
        sys.exit("Unable to open the video, check the path.\n")

    while frame_number < length_video:
        _, rgb = cap.read()

        if _ == 1:

            results = model(rgb)
            tags = list(results.pandas().xyxy[0].name)

            for vals in tags:
                if vals == "sports ball":
                    newpath = f'FramesOf{video_name}'
                    if not os.path.exists(newpath):
                        os.makedirs(newpath)
                    cv2.imwrite(
                        f'./FramesOf{video_name}/' + str('%08d.png' % frame_number), rgb)
                    break

            frame_number += 1

        else:
            print("error")
            break
    cap.release()
    print(-start_time + time.time())


# pass the file name to extract the frames which have the ping pong ball
extract_frames('129114896')
