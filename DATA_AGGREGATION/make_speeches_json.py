import json
import os
from unidecode import unidecode
import sys
import argparse
import ast

def parse_args():
    parser = argparse.ArgumentParser(description="Aggregate speeches, buzzwords and summary")
    parser.add_argument(
        'info_json_path',
        type=str,
        help="Path to the info_json containing speaker information"
    )
    parser.add_argument(
        "--speeches_directory",
        type=str,
        help="Directory where the speech JSON files are located",
        default="speeches",
    )
    parser.add_argument(
        "--output_file",
        type=str,
        help="Path to the output file to write the combine information",
        default="speeches_summary_buzzwords.json",
    )
    return parser.parse_args()


def extract_buzzword_list(buzzword_string):

    cleaned_string = buzzword_string.split("```")[1]
    print("CLEANED", cleaned_string)
    buzzwords_list_string = ""
    if "politische_forderungen" in cleaned_string:
        buzzwords_list_string = cleaned_string.split("politische_forderungen = ")[1]
    if "schlagworte_forderungen" in cleaned_string:
        buzzwords_list_string = cleaned_string.split("schlagworte_forderungen = ")[1]
    if "political_demands" in cleaned_string:
        buzzwords_list_string = cleaned_string.split("political_demands = ")[1]
    if "keywords_and_demands" in cleaned_string:
        buzzwords_list_string = cleaned_string.split("keywords_and_demands = ")[1]
    if "forderungen" in cleaned_string:
        buzzwords_list_string = cleaned_string.split("forderungen = ")[1]

    buzzwords_list = ast.literal_eval(buzzwords_list_string)
    print(buzzwords_list)

    return buzzwords_list


def main():

    args = parse_args()

    try: 
        with open(args.info_json_path, 'r', encoding='utf-8') as f:
            info_json = json.load(f)
    except FileNotFoundError:
        print(f"Error: The file {args.info_json_path} was not found.")
        sys.exit(1)

    speeches_dir = args.speeches_directory
    output_file = args.output_file


    for person in info_json:
        speech_filename = unidecode(person["name"]).strip().lower().replace(" ", "_") + ".json"
        speech_filepath = os.path.join(speeches_dir, speech_filename)
        
        if os.path.exists(speech_filepath):
            with open(speech_filepath, 'r', encoding='utf-8') as speech_file:
                speech_data = json.load(speech_file)
            
            buzzwords_list = extract_buzzword_list(speech_data.get("buzzword", ""))
            person["text"] = speech_data.get("text", "")
            person["buzzwords"] = buzzwords_list
            person["summary"] = speech_data.get("summary", "")
        
        else:
            print(f"Warning: Speech file for {person['name']} not found at {speech_filepath}")

    try:
        with open(output_file, 'w', encoding='utf-8') as output_file:
            json.dump(info_json, output_file, indent=4)
        print(f"Updated JSON file written to '{output_file}'")
    except Exception as e:
        print(f"Error: Could not write to putput file '{output_file}'. {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
