# InsightCV

---

## __Description:__
**InsightCV** is a simple, clean resume analyzer that helps users analyze their Resume and compare it against a Job Description.

It's built using `streamlit` and uses libraries like `pandas`, `PDFPlumber`, `spaCy`, `textstat`, etc., to extract and evaluate resumes based on readability, formatting, skills, and more.

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
After downloading, navigate to the project folder in the terminal/cmd and install required libraries.
```
pip install -r requirements.txt
```
### Usage
To launch the program, run `InsightCV.py` using streamlit.
```
streamlit run InsightCV.py
```
The program will automatically launch on the browser with **InsightCV** web app on localhost.

![Home screen](https://i.postimg.cc/wxPXCQG1/Screenshot-24.png)

### Navigating through the App

#### Homepage

On the home page of **InsightCV**, it will prompt to upload a resume. Upload the resume in PDF format (Use the converter to convert any file into PDF, if the resume is not available in PDF format).

Then the user can select from the 2 options available:
1. `Analyse`
2. `Compare with JD`
 And click `start` to continue.

#### Analyse
`Analyse` function detects and displays skills found in the user's resume.
Also, provides a Resume score (out of 100) based on:
    - Skills match
    - Action verbs
    - Readability
    - Formatting
    - Filename structure
    - Resume length

![analyse](https://i.postimg.cc/W4FF6BsS/Screenshot-25.png)

The user can also see the Detailed breakdown by clicking the `View Detailed Score Breakdown` button.

#### Compare with JD
The program will prompt to upload or paste the Job Description. After uploading, click `Continue` to start.

`Compare with JD` function detects key skills required from the JD and compares them with the user's resume.

![Compare screen](https://i.postimg.cc/gkzxBXYx/Screenshot-26.png)

It also outputs a Match score and highlights missing skills in the user's resume.

The user can also see unmatched skills by clicking the `View in Detail` button.

![Compare Output](https://i.postimg.cc/DyxSVvZB/Screenshot-27.png)

## __author__
Made with 🤍 by [Manav](https://www.linkedin.com/in/manav-kumarr)
