'''
 ● Partial Link Text
'''


from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam Chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximizam fereastra
chrome.maximize_window()

# navigare catre un url
chrome.get('https://formy-project.herokuapp.com/')

# selector by Partial Link Text
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Enab').click()


sleep(3)
chrome.quit()