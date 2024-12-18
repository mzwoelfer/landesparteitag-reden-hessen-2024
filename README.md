# Grüne Hessen Landesparteitag 2024 SpeechAnalyzer
Get speeches of Landesparteitag of the GRÜNE Hessen 2024.

- DATA_AGGREGATION: Get speeches from livestream. + Summary, buzzwords and transcript
- WEBPAGE: Display speeches on a webpage


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
Download the YouTube Audio/Video in MP4 or MP3 format!

1. Create `speeches_timestamps.md`. Get timestamps for speeches from YouTUbe video
2. `python3 create_speeches_info.py speeches_timestamps.md`
3. `python3 cut_speeches.py speeches_timestamps_info.json landesparteitag.mp4`
4. `python3 transcribeSpeeches.py speeches_timestamps_info.json`
5. includeYouTubeID.py
6. summarizeSpeeches.py

