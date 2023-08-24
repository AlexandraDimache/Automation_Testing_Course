# XPATH
# XPATH

'''
Este adresa elementului, prin care putem gasi
selector by xpath - in f de textul partial - luam textul de pe el cu proprietatea text
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
chrome.get('https://formy-project.herokuapp.com/form')

# selector by XPATH
chrome.find_element(By.XPATH, '//input[@id="first-name"]').send_keys('A')

# selector by XPATH - toate elementele care respecta regula
chrome.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('L')
# * inseamna un inlocuitor pentru toate elementele care respecta regula


# selector by XPATH - navigare in jos - trecem prin fiecare element
chrome.find_element(By.XPATH, '//div/div/input[@id="first-name"]').send_keys('E')


# selector by Xpath - navigare in jos - skip tags - cautam oriunde sub forma de input care sa respecte regula
chrome.find_element(By.XPATH, '//form//input[@id="first-name"]').send_keys('X')
# // = orice mostenitor, / = primul mostenitor


# selector by XPATH - selectare element din lista - index incepe de la 1
chrome.find_element(By.XPATH, '(//input[@class="form-control"])[2]').send_keys('A')


'''
div - parinte 
input - copil care contine textul 'last name'
sleep(3)
'''


sleep(3)
chrome.quit()