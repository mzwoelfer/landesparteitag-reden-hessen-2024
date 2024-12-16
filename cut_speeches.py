import sys
import os
import json
from unidecode import unidecode

def cutAudio(info, audioFile):
    os.system(f"ffmpeg -i {sourceAudio} -ss {info['beginSpeech']} -to {info['endSpeech']} -c copy {audioFile}")
    return


def createExportName(info):
    """Returns the export name based on speaker name"""
    export_name = unidecode(info["name"]).strip().lower().replace(" ", "_")
    if info["reminder"]:
        return "reminder_" + export_name

    return export_name


folder = "speeches/"
speech_info_file = sys.argv[1]
sourceAudio = sys.argv[2]

with open(sys.argv[1], "r") as f:
    speech_info_list = json.load(f)

for info in speech_info_list:
    if "youtube_id" in info:
        continue
    export_name = createExportName(info)
    audioFile = os.path.join(folder, export_name + ".mp3")
    print("Working on:", audioFile)

    if not os.path.isfile(audioFile):
        cutAudio(info, audioFile)
    print()
