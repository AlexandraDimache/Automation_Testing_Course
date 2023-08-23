# ● Tag

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

# selector by Tag - ia primul tag, este in regula doar daca este tag unic
chrome.find_element(By.TAG_NAME, 'input').send_keys('Test')

sleep(3)

# daca avem mai multe tag-uri, le stocam intr-o variabila de tip input
input_list = chrome.find_elements(By.TAG_NAME, 'input')
# am definit o lista care sa stocheze toate elementele de pe site identificabile prin tag-ul de input
input_list[1].send_keys('Test1')
# de fiecare data cand avem de gasit mai multe tag-uri se pot adauga in input_list
print(len(input_list))

sleep(3)
chrome.quit()