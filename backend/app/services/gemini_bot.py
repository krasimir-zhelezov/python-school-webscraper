import google.generativeai as genai
import os

class GeminiBot:
    
    def __init__(self):
        API_KEY = os.environ.get('GEMINI_API_KEY')
        
        genai.configure(api_key=API_KEY)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        
    def process_data(self, data: str) -> str:
        prompt = """I will send you raw data extracted from a school website. Your task is to process it and format it in Bulgarian.
        Correct grammatical and spelling errors, organize the information clearly and professionally (you can use lists, subheadings, or tables).
        The information is for educational purposes — do not embellish it, do not advertise it, or add new elements. 
        If there are examples in the text, treat them as examples, not as background information.
        Do not add an introduction, title, explanation, or commentary. Start directly with the revised text: \n
        """
        
        return self.model.generate_content(prompt + data).text