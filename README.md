<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,50:F59E0B,100:EF4444&height=160&section=header&text=Random%20Headline%20Generator&fontSize=36&fontColor=ffffff&animation=fadeIn&fontAlignY=36&desc=Beginner-friendly%20Python%20CLI%20project%20for%20random%20text%20generation&descSize=14&descAlignY=56" alt="Random Headline Generator banner" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Type-CLI%20Application-F59E0B?style=for-the-badge" alt="CLI Application" />
  <img src="https://img.shields.io/badge/Dependencies-Standard%20Library-22C55E?style=for-the-badge" alt="Standard Library" />
  <img src="https://img.shields.io/badge/License-MIT-7C3AED?style=for-the-badge" alt="MIT License" />
</p>

---

## Overview

Random Headline Generator is a Python command-line application that creates playful fake headlines from predefined subjects, actions, places, and symbols.

The project is built as a beginner practice app for randomization, functions, dictionaries, loops, input validation, and file handling.

---

## Features

| Feature | Detail |
|---|---|
| Category menu | Lets the user choose from multiple headline categories |
| Random generation | Combines random subjects, actions, places, and symbols |
| Save option | Saves selected headlines to `headlines.txt` |
| Timestamp support | Adds save time for each stored headline |
| Input validation | Handles invalid category and yes/no inputs |
| No external packages | Uses only Python standard library modules |

---

## Project Structure

```text
Random-Fake-Headline-Generator/
|-- main.py
|-- requirements.txt
|-- LICENSE
|-- .gitignore
`-- README.md
```

`headlines.txt` is created automatically when a headline is saved.

---

## How To Run

```bash
git clone https://github.com/bilal-dev-0x/Random-Fake-Headline-Generator.git
cd Random-Fake-Headline-Generator
python main.py
```

Optional dependency check:

```bash
pip install -r requirements.txt
```

The requirements file is included for standard project structure, but no third-party package is needed.

---

## Example Output

```text
Random News Headline Generator
Choose a category:
1. Funny News
2. Political News
3. Celebrity News
4. Animal News
Enter your choice (1-4): 1

Generated headline:
A smart refrigerator is teaching maths to aliens in a haunted classroom

Do you want to save this headline? (yes/no): yes
Headline saved successfully!
```

---

## Concepts Practiced

- `random.choice()`
- Lists and dictionaries
- Functions
- `while` loops
- Input validation
- File handling
- Timestamp formatting with `time`

---

## Future Improvements

- Add more categories.
- Add custom user-created words.
- Add export to CSV.
- Convert the CLI app into a small web app.
- Add tests for headline generation.

---

<p align="center">
  <b>A fun Python text generator built to practice clean CLI flow and beginner project structure.</b>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:EF4444,50:F59E0B,100:111827&height=90&section=footer" alt="Footer wave" />
</p>
