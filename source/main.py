from youtube_downloader import video_download
from video_to_ascii import frame_from_video, print_video
import pyglet
import os

def main():
    url = input("Enter the URL of the YouTube video: ")

    os.system('cls')
    video_name = video_download(url)

    video = frame_from_video(video_name)

    if video:
        song = pyglet.media.load(f'audios/{video_name}.mp3')
        song.play()
        print_video(video)

    os.remove(f'audios/{video_name}.mp3')
    os.remove(f'videos/{video_name}.mp4')
    os.system('cls')

if __name__ == "__main__":
    main()
    
