from openai import OpenAI
import os
from dotenv import load_dotenv
import json
from glob import glob
import time

load_dotenv()
folder = "speeches"
client = OpenAI()

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
        "Eine Zusammenfassung der Rede in weniger als drei Sätzen. Für Leute die die Veranstaltung nicht besuchten:\n\n"
    )

    summary = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": summarize_prompt
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": speech_text
                    }
                ]
            }
        ],
        temperature=1,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    buzzword = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": buzzword_prompt
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": speech_text
                    }
                ]
            }
        ],
        temperature=1,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    jsonData["text"] = speech_text
    jsonData["summary"] = summary.choices[0].message.content.strip()
    jsonData["buzzword"] = buzzword.choices[0].message.content.strip()
    jsonData["youtube_id"] = "L9ePHyT1fZM"

    with open(speech_json_file, "w", encoding="utf-8") as f:
        json.dump(jsonData, f, ensure_ascii=False, indent=4)

    print(f"Summary and buzzwords saved to: {speech_json_file}")
