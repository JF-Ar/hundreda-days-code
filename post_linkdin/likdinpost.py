from time import sleep
import random

import pyautogui

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager


PUBLICACAO_TEXT = ("""Fala pessoal! Eu estou curtindo o meu desafio de #100DaysOfCode !\n
Tenho aproveitado e aprendido muito! Fiz vários bots para testar algumas habilidades e bibliotecas.\n
Se você quiser acompanhar e ver estas coisas funcionando, tenho publicado no meu instagram (link)\n
E você também pode encontrar o código no meu GitHub! Inclusive, essa publicação foi feita por um bot em python!
Bom, meu atual e grande desafio está sendo juntar a interface que criei com PySimpleGUI e o bot Python que fiz para o Linkedin que te permite fazer algumas conexções!

Uma coisa que aprendi com isso tudo é que você não pode desistir nunca! A dor do aprendizado é uma delicia.\n
Se esforce e encontre pessoas que possam te apoiar e continue estudando, se cercando de pessoas experientes. 

Um abraço guys! #Python #Developer #bots #Code""")


class LinkedinPost:

    def __init__(self, username, password):
            self.username = username
            self.password = password

    def navegador_config(self):
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
        sleep(4)

    @staticmethod
    def digitando_como_pessoa(texto, campo_mensagem):
        for letra in texto:
            campo_mensagem.send_keys(letra)
            sleep(random.randint(1,5)/30)

    def publicacao(self):
        driver = self.driver
        button_foto = driver.find_element_by_xpath('//button[@aria-label="Adicionar foto"]')
        button_foto.click()
        sleep(4)
        botpost.encontrarimgagem()


    def encontrarimgagem(self):
        fotprint = 'print.png'
        fotopublicar = pyautogui.locateCenterOnScreen(fotprint)
        pyautogui.moveTo(fotopublicar, duration=0.5)
        sleep(1)
        pyautogui.click()
        sleep(3)

    def publicar(self):
        driver = self.driver 
        button_concluido = driver.find_element_by_class_name('editor-container')
        button_concluido.click()
        sleep(2)
        campo_publicacao = driver.find_element_by_xpath('//div[@data-placeholder="No que você está pensando?"]')
        botpost.digitando_como_pessoa(PUBLICACAO_TEXT,campo_publicacao)
        sleep(1)
        button_publicar = driver.find_element_by_xpath('//button[@aria-label="Salvar esta publicação"]')
        button_publicar.click()

    def curtir(self):
        driver = self.driver
        pass
        
   

botpost = LinkedinPost('','')
botpost.navegador_config()
botpost.login()
botpost.publicacao()
botpost.publicar()