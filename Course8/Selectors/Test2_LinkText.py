'''
 ● Link Text
'''

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam Chrome
s = Service(ChromeDriverManager().install()) #stocam serviciul de Chrome, printr-o variabila definita pentru a deschide acel chrome
chrome = webdriver.Chrome(service=s)

# maximizam fereastra
chrome.maximize_window()

# navigare catre un url
chrome.get('https://formy-project.herokuapp.com/')

# selector by Link Text
chrome.find_element(By.LINK_TEXT, 'Autocomplete').click()


sleep(3)
chrome.quit()



