from utils.download import download_video
from utils.audio_to_text import convert_audio_to_text
from utils.highlight_extraction import extract_highlights
from utils.post_processing import add_captions

def main():
    video_path = download_video("https://www.youtube.com/watch?v=bjLHKWdzbtI")
    text = convert_audio_to_text(video_path)
    highlights = extract_highlights(video_path)
    final_video_path = add_captions(highlights, "final_output.mp4")

if __name__ == "__main__":
    main()
