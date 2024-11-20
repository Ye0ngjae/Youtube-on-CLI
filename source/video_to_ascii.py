import cv2
import time
import sys
from collections import deque
import os

CHARSET = " ⠁⠃⠇⠗⠶⠷⠿"

def rgb_to_ansi(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def resize_frame(frame, new_width):
    height, width, _ = frame.shape
    aspect_ratio = width / height
    new_height = int(new_width / aspect_ratio / 2)
    return cv2.resize(frame, (new_width, new_height))

def frame_to_ascii(frame):
    try:
        new_width = 150
        if frame is None:
            return None
        resized_frame = resize_frame(frame, new_width)
        new_height, new_width, _ = resized_frame.shape
        
        gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

        ascii_frame = []
        for y in range(new_height):
            row = []
            for x in range(new_width):
                gray_value = gray_frame[y, x]
                ascii_index = int(gray_value / 255 * (len(CHARSET) - 1))
                b, g, r = resized_frame[y, x]
                row.append((rgb_to_ansi(r, g, b), CHARSET[ascii_index]))
            ascii_frame.append(row)

        return ascii_frame
    except Exception as e:
        print(e)
        return None

def frame_from_video(video_name):
    video_path = f'./videos/{video_name}.mp4'

    if not os.path.exists(video_path):
        print(f"Video file not found: {video_path}")
        return None, None
    
    cap = cv2.VideoCapture(video_path)
    video = []

    if not cap.isOpened():
        print("Error opening video file")
        return None, None

    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    framerate = int(cap.get(cv2.CAP_PROP_FPS))

    for i in range(length):
        print(f"Processing... {round((i/length)*100)}%", end="\r")

        ret, frame = cap.read()
        if not ret:
            print("Error reading frame")
            break
        
        video.append(frame_to_ascii(frame))
        
    cap.release()
    return video, framerate

def print_video(video, framerate):
    for frame in video:
        sys.stdout.write("\033[0;0H")  
        for row in frame:
            for color, char in row:
                sys.stdout.write(f"{color}{char}")
            sys.stdout.write("\033[0m\n")
        sys.stdout.flush()
        time.sleep(1/framerate)  