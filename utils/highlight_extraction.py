from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def extract_highlights(video_path):
    start_time = 10  # Start time in seconds.
    end_time = 25  # End time in seconds.

    ffmpeg_extract_subclip(video_path, start_time, end_time, targetname="clip.mp4")
    return "clip.mp4"
