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

