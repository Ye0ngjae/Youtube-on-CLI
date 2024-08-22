from youtube_downloader import video_download, audio_download
from video_to_ascii import frame_to_ascii, frame_from_video
from pydub import AudioSegment
import simpleaudio as sa

def play_audio(file_path):
    audio = AudioSegment.from_mp3(file_path)
    
    wav_path = file_path.replace('.mp3', '.wav')
    audio.export(wav_path, format='wav')

    wave_obj = sa.WaveObject.from_wave_file(wav_path)
    play_obj = wave_obj.play()
    play_obj.wait_done()  

if __name__ == "__main__":
    url = 'https://youtu.be/RSNmgE6L8AU'
    title = video_download(url)  
    frame_from_video(f'{title}.mp4')
    play_audio(f'audios/{title}.mp3')
