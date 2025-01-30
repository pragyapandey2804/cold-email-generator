# Cold Email Generator

This project helps generate cold emails for job applications based on job descriptions scraped from career pages. The generator uses a combination of LangChain and Groq for extracting job data and composing personalized emails.

## Features

- Scrapes job postings from the provided URLs.
- Extracts relevant job information such as the role, skills, experience, and description.
- Generates personalized cold emails based on the job information and the user's portfolio.

## Requirements

- Python 3.x
- Streamlit
- LangChain
- Groq API
- Pandas
- ChromaDB
- dotenv

## Setup

1) Clone the repository:
```bash
git clone https://github.com/pragyapandey2804/cold-email-generator.git
cd cold-email-generator
```

2) Create a .env file to store sensitive information such as your API key for Groq:
```bash
GROQ_API_KEY=your-api-key-here
```

3) Run the Streamlit app:
```bash
streamlit run main.py
```

4) Open the app in your browser and start using the cold email generator.

## How it Works

- Input: Provide the URL of a job listing.
- Processing: The app scrapes the job details from the URL and extracts the key information.
- Email Generation: The app uses your portfolio (stored in a CSV file) to match skills and create a cold email.
- Output: The generated cold email is displayed on the app








