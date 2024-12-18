import os
import sys
import json
from openai import OpenAI
from dotenv import load_dotenv
from unidecode import unidecode

load_dotenv()
client = OpenAI()


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


def transcribe_file(file_path, info):
    """
    Transcribe an audio file to text if it is not already transcribed.

    Args:
        file_path (str): Path to the audio file.
        info (dict): Additional information about the audio file.

    Returns:
        None
    """
    filename, extension = os.path.splitext(file_path)
    if extension != ".mp3":
        print(f"Skipping unsupported file type: {file_path}")
        return

    output_file = f"{filename}.txt"
    if os.path.isfile(f"{filename}.json"):
        print(f"Transcript already exists for: {file_path}")
        return

    print(f"Transcribing: {file_path}")
    with open(file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            language="de",
            response_format="text",
            prompt=(
                "Diese Transkripte sind von Reden am Samstag, den 14. Dezember 2024, "
                "vom Landesparteitag der GRÜNEN in Hessen. Mit den Reden bewerben sich "
                "die Kandidat:innen um für die Landesliste gewählt zu werden."
            ),
        )

    with open(output_file, "w") as output:
        output.write(transcription)


def process_speeches(folder, speech_info_file):
    """
    Process all speeches by transcribing corresponding audio files.

    Args:
        folder (str): Path to the folder containing speech audio files.
        speech_info_file (str): Path to the JSON file containing speech metadata.

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
        audio_file = os.path.join(folder, f"{export_name}.mp3")

        print(f"Working on: {audio_file}")
        transcribe_file(audio_file, info)
        print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <speech_info_file>")
        sys.exit(1)

    FOLDER = "speeches/"
    SPEECH_INFO_FILE = sys.argv[1]

    process_speeches(FOLDER, SPEECH_INFO_FILE)
