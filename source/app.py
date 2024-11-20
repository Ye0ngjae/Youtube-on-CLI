from youtube_downloader import video_download
from video_to_ascii import frame_from_video, print_video
import os
import sys

def main():
    url = sys.argv[1]

    os.system('cls')

    video_name = video_download(url)
    print(f"Downloaded video: {video_name}.mp4")
    
    video, framerate = frame_from_video(video_name)
    print(f"Playing video: {video_name}.mp4")

    if video:
        print_video(video, framerate)

    else:
        print("Error processing video. Please try again.")

    try:
        os.remove(f'videos/{video_name}.mp4')
    except:
        pass
    #os.system('cls')

if __name__ == "__main__":
    main()
    
