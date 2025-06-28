import streamlit as st
from streamlit_tags import st_tags
import pdfplumber
import pandas as pd
import re
import spacy
import textstat
nlp = spacy.load('en_core_web_sm')

#open skills.csv in read mode with pandas
skills_df = pd.read_csv("skills.csv", header=None, names=["skill"])
skills_list = skills_df["skill"].str.lower().tolist()

#open action_verbs.csv in read mode with pandas
verbs_df = pd.read_csv("action_verbs.csv", header=None, names=["verbs"])
verbs_list = verbs_df["verbs"].str.lower().tolist()

#extracting the user's name from the resume file using spacy
def user_name(file):
    file = nlp(file)
    for ent in file.ents:
        if ent.label_ == "PERSON":
            return ent.text.strip().title()

#function to extract text from pdf files using pdfplumber
def extract_text(file):
    text = ""
    try:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() if page.extract_text() else ""
    except Exception as e:
        st.error(f"Some error occured while extracting pdf: {e}") 
    return text

#function to extract skills (keywords) from the extracted text
def extract_skills(text):
    found = []
    text_low = text.lower()
    for skill in skills_list:
        if re.search(rf"\b{re.escape(skill)}\b", text_low):
            found.append(skill)
    return list(set(found))

#function to extract action verbs from extracted text
def action_verbs(text):
    found = []
    text_low = text.lower()
    for verbs in verbs_list:
        if re.search(rf"\b{re.escape(verbs)}\b",text_low):
            found.append(verbs)
    return list(set(found))

#function to check formatting of the user's resume and score them
def formatting(text, pages):
    score = 10
    if pages > 2:
        score -= 3
    if text.count("-") + text.count("•") + text.count("●") < 5:
        score -= 3
    if re.search(r"\b[A-Z]{6,}\b", text):
        score -= 1.5
    return max(score, 1)

#function to check filename format of the user's resume using regex and score them
def filename(filename):
    name = filename.lower()
    if "resume" not in name:
        return 0
    elif re.search(r"^(final|draft|new|copy)", name):
        return 3
    elif re.search(r"[^a-z0-9_.-]", name):
        return 5
    elif re.search(r"[a-z]+[-_][a-z]+.*resume", name):
        return 10
    else:
        return 7

#function to check readablilty of the user's resume using textstat and score them
def readability(text):
    score = textstat.flesch_reading_ease(text)
    if score >= 90:
        return 15
    elif score >= 70:
        return 12
    elif score >= 60:
        return 9
    elif score >= 30:
        return 7
    else:
        return 3

def main():
    #printing the program name, logo and credits using streamlit  
    st.markdown(
        """
        <div style='display: flex; justify-content: space-between; align-items: center;'>
            <div style='display: flex; align-items: center;'>
                <h2 style='margin-bottom: 0;'>InsightCV</h2>
            </div>
            <span style='font-size: 0.9em;'>
                Made with 🤍 by <a href='https://www.linkedin.com/in/manav-kumarr' target='_blank'>Manav</a>
            </span>
        </div>
        <hr style='margin-top:0.5em; margin-bottom:1em;'/>
        """,
        unsafe_allow_html=True
    )

    #printing the header
    st.header("Welcome to InsightCV!")

    #asking for resume file input
    resumefile = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
    st.caption("Not a PDF File? [Convert Here](https://www.ilovepdf.com/word_to_pdf)")
    if resumefile: 
        st.success(f"Uploaded Resume {resumefile.name}")

    #asking to seelect the option for what function the user want to use
    mode = st.selectbox("Choose what to do you want to do: ", ["Analyse", "Compare with JD"])
    if "start_clicked" not in st.session_state:
        st.session_state.start_clicked = False
    if st.button("start"):
        st.session_state.start_clicked = True

    #strating the process
    if st.session_state.start_clicked and resumefile:
        with st.spinner("Extracting the Resume..."):
            extracted_resume = extract_text(resumefile)
        name = user_name(extracted_resume)
        extracted_skills = extract_skills(extracted_resume)
        verbs = action_verbs(extracted_resume)

        with pdfplumber.open(resumefile) as pdf:
            pages = len(pdf.pages)

        #counting pdf length and scoring 
        if pages== 1:
            length_score = 10
        elif pages == 2:
            length_score = 8
        else:
            length_score = 5

        #calling all the scoring functions used in final Resume score
        readablilty_score = readability(extracted_resume) 
        formatting_score = formatting(extracted_resume, pages)
        filename_score = filename(resumefile.name) 
        verbs_score = min(len(verbs), 20) 
        skills_score = min(len(extracted_skills), 30) 
        
        resume_score = readablilty_score + verbs_score + skills_score + formatting_score + filename_score + length_score
        # Distribution for resume score:
            #skills present = 30%
            #action verbs present = 20%
            #formatting = 15%
            #readablilty = 15%
            #filename format = 10%
            #length of pdf = 10%
        
        #if user select analyse mode
        if mode == "Analyse":
            st.header("Resume Analysis")
            st.subheader(f"Hello :green[{name}!]")
            st_tags(extracted_skills, '', "Skills Detected in your resume:", '', -1, None)
            st.metric("Your Resume score is", f"{resume_score} / 100")
            with st.expander("View Detailed Score Breakdown"):
                st.write(f"🧠 Skills score: {skills_score}/30")
                st.write(f"🚀 Action verbs score: {verbs_score}/20")
                st.write(f"📖 Readability score: {readablilty_score}/15")
                st.write(f"🧩 Formatting score: {formatting_score}/15")
                st.write(f"📌 Filename score: {filename_score}/10")
                st.write(f"📄 Resume length score: {length_score}/10")
            if st.button(":blue[▸ Get AI resume suggestions]", type="tertiary"):
                st.write("Feature coming soon")
        #if user select Compare mode
        elif mode == "Compare with JD":
            st.header("Compare with Job Description")
            st.subheader(f"Hello :green[{name}!]")
            st.subheader("Upload or Paste Job Description")
            jd_file = st.file_uploader("Upload JD (PDF)", type=["pdf"])
            jd_text = st.text_area("or Paste the Job Description below")
            jd_start= st.button(":blue[▸Continue]", type="tertiary")
            if jd_start:
                if not jd_file and not jd_text:
                    st.warning("Please Upload or paste a valid Job Description")
                else:
                    if jd_file:
                        extracted_jd = extract_text(jd_file)
                    elif jd_text:
                        extracted_jd = jd_text
                    jd_skills = extract_skills(extracted_jd)
                    matched_skills = []
                    missing_skills = []
                    match_score = 0
                    for skill in extracted_skills:
                        if skill in jd_skills:
                            matched_skills.append(skill)
                    for skill in jd_skills:
                        if skill not in extracted_skills:
                            missing_skills.append(skill)
                    if jd_skills:
                        ratio = len(matched_skills)/len(jd_skills)
                        match_score = round(ratio*100)
                    else:
                        match_score= 0
                        st.write(f"skills matched: {len(matched_skills)}/{len(jd_skills)}")
                    st.metric("Match score", f"{match_score}%")
                    with st.expander("View in Detail"):
                        if missing_skills:
                            st.markdown("**Missing skills in Resume:**")
                            st.write(",".join(missing_skills))
                        else: 
                            st.markdown("All the skills required are present in resume")

if __name__ == "__main__":
    main()
