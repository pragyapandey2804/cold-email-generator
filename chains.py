import os 
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

os.getenv("GROQ_API_KEY")

class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            temperature = 0,
            groq_api_key = os.getenv("GROQ_API_KEY"),
            model_name = "llama-3.3-70b-versatile"
        )

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ###SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ###INSTRUCTION:
            The scraped text if fro, the career's page website.
            Your job is to extract the job postings and return them in a JSON format containing 
            following keys : 'role', 'experience','skills' and 'description.
            Only return the valid JSON.
            ###VALID JSON (NO PREAMBLE):

            """
        )    
        chain_extract = prompt_extract | self.llm 
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)  ###type = json
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_email(self, job, links):
        prompt_email = PromptTemplate.from_template(
           """
           ###JOB DESCRIPTION:
           {job_description}
           ###INSTRUCTION:
           You are Pragya a student of robotics and automation engineering.
           You have great interest in robotics, AI and computer vision.
           YOU have done many projecrts and posted them on github.
           Your job is to write cold emails to the bussiness regarding the job mentioned aboved fulfilling their needs.
           Also add the most relevant ones from the following links to showcase the project experience :{link_list}
           Remember you are Pragya a student of robotics and automation.
           Do not provide a preamble
           ##EMAIL (NO PREAMBLE):

           """
        )

        chain_email = prompt_email | self.llm 
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content  ##type = str
        

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))