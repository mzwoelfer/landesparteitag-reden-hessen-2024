# Grüne Hessen Landesparteitag 2024 SpeechAnalyzer
Get speeches of Landesparteitag of teh GRÜNE Hessen 2024.


## Prerequisites
Create a Python3 Virtual Environment.
Requiremetns:
- python3
- python3-pip
- python3-venv

```SHELL
python3 -m venv Env
source Env/bin/activate
pip install -r requirements.txt
```

## How to run?
1. Create `speeches_1.md`. Get timestamps for speeches from YouTUbe video
2. `python3 getSpeechesInfo.py speeches_1.md`
3. `python3 cut_speeches.py speeches_1_info.json landesparteitag.mp4`
4. `python3 transcribeSpeeches.py speeches_1_info.json`
5. includeYouTubeID.py
6. summarizeSpeeches.py


Analysis could be:
- Counted words
- Most similar words being used
- Automatic topic and sentiment analysis

Want a frontend to put YouTube link, select your range of time for the video, get the text for that area.

1. Basic Webpage with list of places ons list and links to speeches (only text)
2. Include timestamps in speech
3. Embedd Video on YouTube starting at that timestamp
4. Word-Count overview
5. Summary Word-Count with sentiment (renewable energies, wind and solar, etc. are one group!)



## ToDos
- Simplyfy the process from cutting the videos to having the speeches, texts and summary in one script
- Rework Datastructure to contain database_key, name, youtube_link, summary, text, buzzwords as python list, begin- end- Speech and Question timestamps, language, segments, questions -- ALL directly readable in webapp. No shenanigans!


## Steps
- Download youtube video
- Write Python script to
    iterate timestamps
    cut audio into clips
    push to whisper
    get text
    save text
- Save text
- get text from video/audio (per timestamp)
- split into indiviudal speeches
- include "text", "name", speaker_id" in the JSON file
