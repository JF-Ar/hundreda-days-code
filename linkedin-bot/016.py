from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager


class LinkedinBot():

    def texto(self):
        self.mensagem = ( """Opa! Meu nome é Josué Junio e estou começando
        na nossa área e acho que esse conecção pode ser útil para ambos!
        Eu me apaixonei pela programação e gostaria de fazer mais contatos.
        De qualquer maneira, eu gostei do seu perfil e gostaria de manter contato.
        Um abraço! """)

    
    def __init__(self, username, password, profissao):
        opts = Options()
        opts.add_argument('--headless')
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
        sleep(4)

    def find_busca(self):
        driver = self.driver
        sleep(4)
        campo_pesquisar = driver.find_element_by_xpath('//input[@placeholder="Pesquisar"]')
        campo_pesquisar.clear()
        sleep(2)
        campo_pesquisar.send_keys(self.profissao + Keys.ENTER)
        sleep(4)
##Caso queira mais filtros, basta trocar na função futuramente
#numero de conexões por exemplo
    def filtros(self):
        driver = self.driver
        filtropessoas = driver.find_element_by_xpath('//button[@aria-label="Pessoas"]')
        filtropessoas.click()
        sleep(3)


    def enviar_solicitacao(self):
        driver = self.driver
        #encontrando a tag mãe
        #pessoas = driver.find_elements_by_xpath('//*[@id="main"]/div/div/div[2]/ul/li')
        buttons = driver.find_elements_by_xpath('//*[@id="main"]/div/div/div[2]/ul/li/div/div/div[3]/div/button')
        #print(len(pessoas))  
        print(len(buttons)) #testando o numero de botões encontrados

bot = LinkedinBot('bla bla bla@seuemail.com','1234secreto', 'criador de bots')
bot.login()
bot.find_busca()
bot.filtros()
bot.enviar_solicitacao()


        