import subprocess

def convert_audio_to_wav(input_audio_path, output_audio_path):
    command = ["ffmpeg", "-i", input_audio_path, "-ab", "160k", "-ac", "2", "-ar", "44100", "-vn", output_audio_path]
    subprocess.run(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
