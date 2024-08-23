from pytubefix import YouTube

def video_download(url):
    audio_download(url)

    yt = YouTube(url)

    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    video.download(output_path='videos', filename=f"{yt.title}.mp4",)

    return yt.title

def audio_download(url):
    yt = YouTube(url)
    
    audio = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
    audio.download(output_path='audios', filename=f"{yt.title}.mp3")

    return yt.title