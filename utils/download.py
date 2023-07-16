from pytube import YouTube

def download_video(url):
    youtube = YouTube(url)
    video = youtube.streams.get_highest_resolution()
    # Specify output path if needed, by default it downloads to working directory
    file_path = video.download()
    return file_path
