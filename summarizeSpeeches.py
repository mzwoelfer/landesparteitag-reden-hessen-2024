import openai
import os
from dotenv import load_dotenv
import json
from glob import glob
import time

load_dotenv()
openai.api_key = os.getenv("OPENAPI_KEY")
folder = "speeches"

for speech_txt_file in glob(folder + '/*.txt'):
    print("Getting summary and buzzwords for:", speech_txt_file)

    with open(speech_txt_file, "r", encoding="utf-8") as f:
        speech_text = f.read()

    speech_json_file = speech_txt_file.replace(".txt", ".json")

    if os.path.exists(speech_json_file):
        with open(speech_json_file, "r", encoding="utf-8") as f:
            jsonData = json.load(f)
        if "summary" in jsonData:
            print(f"Summary already exists for: {speech_json_file}, skipping.")
            continue
    else:
        jsonData = {}

    buzzword_prompt = (
        "Extrahiere die 5 wichtigsten Schlagworte und konkreten politischen Forderungen aus dieser Rede als Python-Liste:\n\n"
    )
    summarize_prompt = (
        "Eine Zusammenfassung der Rede in weniger als vier Sätzen für Leute, die die Veranstaltung nicht besuchten:\n\n"
    )

    summary = openai.Completion.create(
        model="text-davinci-003",
        prompt=summarize_prompt + speech_text,
        temperature=0.73,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0.8,
        presence_penalty=0
    )

    buzzword = openai.Completion.create(
        model="text-davinci-003",
        prompt=buzzword_prompt + speech_text,
        temperature=0.73,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0.8,
        presence_penalty=0
    )

    jsonData["text"] = speech_text
    jsonData["summary"] = summary["choices"][0]["text"].strip()
    jsonData["buzzword"] = buzzword["choices"][0]["text"].strip()
    jsonData["youtube_id"] = "L9ePHyT1fZM"

    with open(speech_json_file, "w", encoding="utf-8") as f:
        json.dump(jsonData, f, ensure_ascii=False, indent=4)

    print(f"Summary and buzzwords saved to: {speech_json_file}")
