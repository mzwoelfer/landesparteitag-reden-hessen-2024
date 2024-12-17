import sys
import os
from openai import OpenAI
import json
from dotenv import load_dotenv
from unidecode import unidecode

load_dotenv()

def createExportName(info):
    """Returns the export name based on speaker name"""
    export_name = unidecode(info["name"]).strip().lower().replace(" ", "_")
    if info["reminder"]:
        return "reminder_" + export_name

    return export_name


def transcribeFile(file, info):
    filename, extension = os.path.splitext(file)
    if extension != '.mp3':
        return

    print("Transcribing:", file)
    if os.path.isfile(os.path.join(filename + ".json")):
        return
    with open(file, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            language="de",
            response_format="text",
            prompt="Diese Transkripte sind von Reden am Samstag, den 14. Dezember 2024, vom Landesparteitag der GRÜNEN in Hessen. Mit den Reden bewerben sich die Kandidat:innen um für die Landesliste gewählt zu werden."
        )
    with open(os.path.join(filename + ".txt"), "w") as f:
        f.write(transcription)


folder = "speeches/"
speech_info_file = sys.argv[1]

client = OpenAI()

with open(sys.argv[1], "r") as f:
    speech_info_list = json.load(f)

for info in speech_info_list:
    if "youtube_id" in info:
        continue
    export_name = createExportName(info)
    audioFile = os.path.join(folder, export_name + ".mp3")
    print("Working on:", audioFile)

    transcribeFile(audioFile, info)
    print()
