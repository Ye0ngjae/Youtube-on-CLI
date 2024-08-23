from youtube_downloader import video_download
from video_to_ascii import frame_from_video
import os

def main():
    url = input("Enter the URL of the YouTube video: ")
    video_name = video_download(url)
    frame_from_video(video_name+'.mp4')

    os.remove(f'audios/{video_name}.mp3')
    os.remove(f'videos/{video_name}.mp4')

if __name__ == "__main__":
    main()
    
