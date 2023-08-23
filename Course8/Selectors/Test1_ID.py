'''
We delve into the different types of selectors: ID, Link Text, Partial Link Text, Name, Tag, Class name, CSS, Xpath.
 ● ID
• In terminal, instalam pip install webdriver-manager si pip install selenium
• Deschidem Chrome
• Navigam catre url dorit ( https://formy-project.herokuapp.com/form )
• Click dreapta pe elementul ce dorim sa il inspectam
• Selectati optiunea ‘Inspect’
• Veti gasi partea de html a unui website
• Structura e urmatoarea:
  tag sau webelement (ex: <input>)
  atribut=”valoare” (ex: type=”text” id=”first-name”)
• Copiem ID al elementului dorit (ex: ‘first-name’)
'''

# avem nevoie sa importam cateva librarii gratuite care sa ne ajute sa controlam chrome

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install()) #stocam serviciul de Chrome, printr-o variabila definita pentru a deschide acel chrome
chrome = webdriver.Chrome(service=s) # initializam din nou o variabila, in care vom stoca acel serviciu de chrome
# instantiem serviciul de chorme prin cei in paranteze


# maximizam fereastra
chrome.maximize_window()

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form')

# selector by ID
first_name = chrome.find_element(By.ID, 'first-name')
first_name.send_keys('Alexandra')


sleep(3)
chrome.quit() # inchide browser-ul