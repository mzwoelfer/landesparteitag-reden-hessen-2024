import os
import json
import time
from glob import glob
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()
FOLDER = "speeches"


def load_speech_text(file_path):
    """
    Load the content of a speech text file.

    Args:
        file_path (str): Path to the text file.

    Returns:
        str: Content of the text file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def load_or_initialize_json(file_path):
    """
    Load JSON data from a file or initialize an empty dictionary if the file doesn't exist.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        dict: JSON data or an empty dictionary.
    """
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}


def save_json(data, file_path):
    """
    Save JSON data to a file.

    Args:
        data (dict): JSON data to save.
        file_path (str): Path to the file.

    Returns:
        None
    """
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def get_summary_and_buzzwords(speech_text):
    """
    Generate a summary and extract buzzwords from a speech text.

    Args:
        speech_text (str): The content of the speech.

    Returns:
        tuple: Summary and buzzwords as strings.
    """
    buzzword_prompt = "Extrahiere die 5 wichtigsten Schlagworte und konkreten politischen Forderungen aus dieser Rede als Python-Liste:\n\n"
    summarize_prompt = "Eine Zusammenfassung der Rede in weniger als drei Sätzen. Für Leute die die Veranstaltung nicht besuchten:\n\n"

    summary_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": summarize_prompt},
            {"role": "user", "content": speech_text},
        ],
        temperature=1,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    buzzword_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": buzzword_prompt},
            {"role": "user", "content": speech_text},
        ],
        temperature=1,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    summary = summary_response.choices[0].message.content.strip()
    buzzwords = buzzword_response.choices[0].message.content.strip()

    return summary, buzzwords


def process_speech_file(speech_txt_file):
    """
    Process a speech text file to generate a summary and buzzwords.

    Args:
        speech_txt_file (str): Path to the speech text file.

    Returns:
        None
    """
    print(f"Processing: {speech_txt_file}")
    speech_text = load_speech_text(speech_txt_file)
    speech_json_file = speech_txt_file.replace(".txt", ".json")

    json_data = load_or_initialize_json(speech_json_file)

    if "summary" in json_data:
        print(f"Summary already exists for: {speech_json_file}, skipping.")
        return

    summary, buzzwords = get_summary_and_buzzwords(speech_text)

    json_data.update(
        {
            "text": speech_text,
            "summary": summary,
            "buzzword": buzzwords,
            "youtube_id": "L9ePHyT1fZM",
        }
    )

    save_json(json_data, speech_json_file)
    print(f"Summary and buzzwords saved to: {speech_json_file}")


if __name__ == "__main__":
    for speech_txt_file in glob(os.path.join(FOLDER, "*.txt")):
        process_speech_file(speech_txt_file)
