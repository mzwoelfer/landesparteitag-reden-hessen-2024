import os
import sys
import json
from unidecode import unidecode


def cut_audio(source_audio, info, output_file):
    """
    Extracts a portion of an audio file based on start and end timestamps.

    Args:
        source_audio (str): Path to the source audio file.
        info (dict): Dictionary containing start and end timestamps.
        output_file (str): Path to save the extracted audio file.

    Returns:
        None
    """
    command = (
        f"ffmpeg -i {source_audio} -ss {info['beginSpeech']} -to {info['endSpeech']} "
        f"-c copy {output_file}"
    )
    os.system(command)
    print(f"Audio segment saved to: {output_file}")


def create_export_name(info):
    """
    Generate an export name based on the speaker's name.

    Args:
        info (dict): Dictionary containing speaker information.

    Returns:
        str: Export name for the file.
    """
    export_name = unidecode(info["name"]).strip().lower().replace(" ", "_")
    return f"reminder_{export_name}" if info.get("reminder") else export_name


def process_audio_segments(folder, speech_info_file, source_audio):
    """
    Process audio segments based on metadata and save them as individual files.

    Args:
        folder (str): Directory to save processed audio files.
        speech_info_file (str): Path to the JSON file containing speech metadata.
        source_audio (str): Path to the source audio file.

    Returns:
        None
    """
    with open(speech_info_file, "r") as file:
        speech_info_list = json.load(file)

    for info in speech_info_list:
        if "youtube_id" in info:
            print(f"Skipping YouTube-based speech: {info['name']}")
            continue

        export_name = create_export_name(info)
        output_file = os.path.join(folder, f"{export_name}.mp3")

        print(f"Working on: {output_file}")
        if not os.path.isfile(output_file):
            cut_audio(source_audio, info, output_file)
        else:
            print(f"File already exists: {output_file}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <speech_info_file> <source_audio>")
        sys.exit(1)

    FOLDER = "speeches/"
    SPEECH_INFO_FILE = sys.argv[1]
    SOURCE_AUDIO = sys.argv[2]

    process_audio_segments(FOLDER, SPEECH_INFO_FILE, SOURCE_AUDIO)
