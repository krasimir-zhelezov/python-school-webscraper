from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

class WebScraper:
    
    def __init__(self):
        self.timeout_time = 5
        
        self.driver = webdriver.Chrome()
    
    def search_for_bulgarian(self, query):
        self.driver.get(f'https://kaksepishe.com/?s={query}&type=title')
        
        try: 
            links = [link.get_attribute('href') for link in self.__find_elements('//article//header//h2//a')]
            self.__extract_article(links[0])
        except TimeoutException:
            self.__extract_article()
        
        # # search_input.send_keys(query)
        
        # self.driver.execute_script(f"arguments[0].value='{query}';", search_input)
        
    def __extract_article(self, url: str=None):
        if (url):
            self.driver.get(f'{url}')
        
        text = ' '.join([p.text for p in self.__find_elements('//main//article//div//p')])
            
        print(text)
        
        return text
        
        
    def __find_element(self, xpath: str) -> WebElement:
        elements = WebDriverWait(self.driver, self.timeout_time).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        
    def __find_elements(self, xpath: str) -> List[WebElement]:
        elements = WebDriverWait(self.driver, self.timeout_time).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath))
        )
        
        return elements
        
    def __click_element(self, element: WebElement):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)
        