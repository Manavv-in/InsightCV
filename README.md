# __InsightCV__
#### Video Demo:  <URL HERE>

---

## __Description:__
**InsightCV** is a simple, clean resume analyzer that helps user to analyse their Resume and compare it against a Job Description.

It's built using `streamlit` and uses libraries like `pandas`, `PDFPlumber`, `spaCy`, `textstat`, etc. to extract and evaluate resumes based on readability, formatting, skills, and more.

---

### __Libraries Used__
- `pdfplumber` – for extracting text from uploaded PDF resumes and job descriptions.
- `pandas` – for reading skill and action verb lists.
- `spaCy` – for extracting named entities like name.
- `textstat` – for calculating readability scores.
- `re` – for pattern matching using regex.
- `streamlit` – for building the interactive web app UI.

## __How to use InsightCV?__

### Download
Clone the Repository or Download Zip:
```
git clone https://github.com/
``` 
### Installation
After downloading, Navigate to the project folder in terminal/cmd and install required libraries.
```
pip install -r requirements.txt
```
### Usage
To launch the program, run `project.py` using streamlit.
```
streamlit run project.py
```
the program will automatically launch on the browser with **InsightCV** web app on localhost.

![Home screen](<Screenshot (24).png>)

### Navigating through the App

#### Homepage

On the home page of **InsightCV**, It will prompt to upload resume. Upload the resume in PDF format (Use the converter to convert any file into PDF, if resume not available in PDF format).

Then user can select from 2 options available:
1. `Analyse`
2. `Compare with JD`
 and click `start` to Continue.

#### Analyse
`Analyse` function detects and displays skills found in user's resume.
Also, Provides a Resume score (out of 100) based on:
    - Skills match
    - Action verbs
    - Readability
    - Formatting
    - Filename structure
    - Resume length

![analyse](<Screenshot (25).png>)

User can also see the Detailed breakdown by clicking the `View Detailed Score Breakdown` button.

#### Compare with JD
The program will prompt to upload or paste Job Description. After Uploading click `Continue` to start.

`Compare with JD` function detects key skills required from the JD and compares them with user's resume.

![Compare screen](<Screenshot (26).png>)

It also Outputs a Match score and Highlights missing skills in user's resume.

User can also see unmatched skills by clicking the `View in Detail` button.

![Compare Output](<Screenshot (27).png>)

## __author__
Made with 🤍 by [Manav](www.linkedin.com/in/manav-kumarr)