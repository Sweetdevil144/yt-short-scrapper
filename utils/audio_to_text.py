import speech_recognition as sr
from pydub import AudioSegment
from moviepy.editor import VideoFileClip

def convert_audio_to_text(video_path):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile("audio.wav")

    sound = AudioSegment.from_wav("audio.wav")
    sound.export("audio.flac", format="flac")

    r = sr.Recognizer()
    audio_file = sr.AudioFile("audio.flac")

    with audio_file as source:
        audio = r.record(source)
    text = r.recognize_google(audio)
    return text
