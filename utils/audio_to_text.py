import speech_recognition as sr

def convert_audio_to_text(audio_path):
    r = sr.Recognizer()
    audio = None
    with sr.AudioFile(audio_path) as source:
        audio = r.record(source)
    text = None
    try:
        text = r.recognize_google(audio)
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    return text
