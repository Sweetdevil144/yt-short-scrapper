from moviepy.editor import TextClip, CompositeVideoClip, VideoFileClip

def add_captions(video_path, output_path):
    clip = VideoFileClip(video_path)
    txt_clip = TextClip("My Caption", fontsize=24, color='white')
    txt_clip = txt_clip.set_pos('bottom').set_duration(clip.duration)
    video = CompositeVideoClip([clip, txt_clip])

    video.write_videofile(output_path)
    return output_path
