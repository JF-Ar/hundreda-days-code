from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class LinkedinBot():
    
    def __init__(self, username, password, profissao):
        self.username = username
        self.password = password
        self.profissao = profissao
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        driver = self.driver
        driver.get('https://linkedin.com/')
        campouser = driver.find_element_by_xpath('//input[@name="session_key"]')
        campouser.click()
        sleep(1)
        campouser.send_keys(self.username)
        camposenha = driver.find_element_by_xpath('//input[@name="session_password"]')
        camposenha.click()
        sleep(1)
        camposenha.send_keys(self.password)
        botao_entrar = driver.find_element_by_class_name('sign-in-form__submit-button').click()
        

        

bot = LinkedinBot('ablueablue','ablue2e3', 'ablueprof')



        