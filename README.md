# CharacterAnalysis
## Description
This program analyzes a text file to identify all character names mentioned in the text and counts how many times each one appears. It also detects dialogue by iterating through the file and applying simple speech-pattern rules. Using English grammar cues, the program infers which character is speaking in each line of dialogue. For every character who speaks, the program extracts a “catchphrase” by determining the most frequently used word in their speech, excluding pronouns, articles, and prepositions.
## Features
* Detects names listed inside of a text file
* Detects the occurance of names in a text file
* Identifies dialogue using English grammar structure
* Attributes dialogue to characters
* Determines the most frequent word spoken by a character
## Tech Stack
**Python - File Parsing - Text Analysis - Data Analysis**
## Installation
1. Install Python: https://www.python.org/downloads
2. Download spaCy Python Library
```
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm
```
3. Clone Repo
```
git clone https://github.com/ThereaultL/CharacterAnalysis.git
```
4. Navigate to Project Directory
```
cd CharacterAnalysis
```
## Running
```
python src/CharacterAnalyzer.py <input_filepath> <output_filepath>
```
- Replace ```<input_filepath>``` with your chosen text file
- Replace ```<output_filepath>``` with your chosen output file
- Output file will store the character analysis summary
  - Characters names
  - Occurances of characters in text
  - Characters Catchphrase
## License
MIT
