import youtube_dl

def download_video(url):
    ydl_opts = {
        'format': 'best',  # Download best quality.
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        ydl.download([url])
    video_path = ydl.prepare_filename(info_dict)
    return video_path
