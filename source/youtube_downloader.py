from pytubefix import YouTube
import os

def video_download(url):
    os.makedirs('videos', exist_ok=True)
    
    yt = YouTube(url)
    safe_title = "video"
    
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    video.download(output_path='videos', filename=safe_title)
    
    return safe_title