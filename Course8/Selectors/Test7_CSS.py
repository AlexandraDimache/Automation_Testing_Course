# ● CSS

''''
● CSS
# = identificator pentru ID
. = identificator pentru clasa
[] = identificator pentru atribut = valoare
* = marcator pentru placeholder valoare partiala
'''

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam Chrome
s = Service(ChromeDriverManager().install())
#stocam serviciul de Chrome, printr-o variabila definita pentru a deschide acel chrome
chrome = webdriver.Chrome(service=s)

# maximizam fereastra
chrome.maximize_window()

# navigare catre un url
chrome.get('https://formy-project.herokuapp.com/form')


# selector by Class, ia prima optiune, este ok doar daca avem clasa unica
chrome.find_element(By.CLASS_NAME, 'form-control').send_keys('Test')


# gasim mai multe si le punem in lista
chrome.find_elements(By.CLASS_NAME, 'form-control')[1].send_keys('Test1')

'''
div - parinte 
input - copil care contine textul 'last name'
sleep(3)
'''

sleep(3)
chrome.quit()
