# SQL & PostgreSQL Interactive Course

A Streamlit learning app organized into 8 sessions based on `SQL_PostgreSQL_Detailed_Study_Guide.pdf`.

## Features
- Eight structured sessions with learning objectives
- Explanations and PostgreSQL-oriented SQL examples
- Hands-on prompts with revealable suggested answers
- Session-level knowledge checks with explanations
- Flashcards
- Final assessment with score feedback
- Session completion tracking for the current browser session
- Download button for the original PDF when included

## Run locally

Python 3.10 or newer is recommended.

```bash
python -m venv .venv
```

Windows:
```powershell
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Install dependencies and run:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud
1. Create a GitHub repository.
2. Upload `app.py`, `requirements.txt`, `README.md`, and the original PDF.
3. Open https://share.streamlit.io/ and sign in with GitHub.
4. Choose the repository, branch, and `app.py` as the main file.
5. Deploy and share the generated app URL.

## Notes
- This version is an interactive learning platform, not a full SQL execution engine.
- For actual PostgreSQL query execution, use an online PostgreSQL playground linked from the Resources page.
- Progress is stored in Streamlit session state and is not a persistent learner profile. A production course can add a database-backed progress store, authentication, and instructor analytics.
- Course content is based on the uploaded study guide; activities and assessment questions are learning aids.
