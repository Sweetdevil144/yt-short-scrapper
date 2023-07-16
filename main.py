from utils.download import download_video
from utils.audio_conversion import convert_audio_to_wav
from utils.audio_to_text import convert_audio_to_text
from utils.highlight_extraction import extract_highlights
from utils.post_processing import add_captions


def main():
    video_url = "https://www.youtube.com/watch?v=bjLHKWdzbtI"
    download_dir = "/Users/abhinavpandey/AI-and-ML/Timestamper/"
    final_video_name = "Craziest Interrogation Moments Of ALL TIME.mp4"
    downloaded_video_path = download_dir + final_video_name  # Full path of the downloaded video

    extracted_audio_path = download_dir + "audio.wav"  # Full path of the audio file in .wav format
    convert_audio_to_wav(downloaded_video_path, extracted_audio_path)

    text = convert_audio_to_text(extracted_audio_path)
    highlights_path = extract_highlights(downloaded_video_path)  # this will be "clip.mp4" by default

    final_output_path = download_dir + "final_output.mp4"  # Full path of the final output video
    final_video_path = add_captions(highlights_path, final_output_path)


if __name__ == "__main__":
    main()
