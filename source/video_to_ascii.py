import cv2
import os
import time

CHARSET = " .:-=+*#%@"

def frame_to_ascii(frame):
    height, width, _ = frame.shape
    aspect_ratio = width / height
    new_width = 100  # Desired width of the ASCII art
    new_height = int(new_width / aspect_ratio / 2)  # Adjust height to maintain aspect ratio
    resized_frame = cv2.resize(frame, (new_width, new_height))
    

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

    # Map the grayscale values to ASCII characters
    ascii_frame = ""
    for y in range(new_height):
        for x in range(new_width):
            gray_value = gray_frame[y, x]
            # Normalize the gray value to the range of CHARSET
            ascii_index = int(gray_value / 255 * (len(CHARSET) - 1))
            ascii_frame += CHARSET[ascii_index]
        ascii_frame += "\n"
    
    os.system("clear")
    print(ascii_frame) # Print the ASCII frame
    time.sleep(1 / 33)  # Delay to match the video frame rate

def frame_from_video(video_name):
    cap = cv2.VideoCapture('./videos/' + video_name)
    
    while cap.isOpened():
        ret, frame = cap.read()
        
        if not ret:
            break
        
        frame_to_ascii(frame)
        
    cap.release()
