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
        
    def search_for_math(self, query):
        self.driver.get(f'https://www.matematika.bg/search.html?q={query}')
        
        link = self.__find_element('//div[contains(@class, \'gsc-expansionArea\')]//div//div//div//div//a').get_attribute('href')
        
        self.driver.get(link)        
        
        cta_accept_button = self.__find_element('//button[contains(@class, \'fc-button fc-cta-consent fc-primary-button\')]')
        self.__click_element(cta_accept_button)
        
        self.__extract_math_article()
        
    def __extract_math_article(self):
        text = self.__concat_p_tags(self.__find_elements('//article//p'))
        
        print(text)
        
        return text
        
        
    def __extract_article(self, url: str=None):
        if (url):
            self.driver.get(f'{url}')
        
        text = self.__concat_p_tags(self.__find_elements('//main//article//div//p'))
        
        return text
    
    def __concat_p_tags(self, p_tags: List[WebElement]) -> str:
        return ' '.join([p.text for p in p_tags])
        
        
    def __find_element(self, xpath: str) -> WebElement:
        element = WebDriverWait(self.driver, self.timeout_time).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        
        return element
        
    def __find_elements(self, xpath: str) -> List[WebElement]:
        elements = WebDriverWait(self.driver, self.timeout_time).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath))
        )
        
        return elements
        
    def __click_element(self, element: WebElement):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)
        