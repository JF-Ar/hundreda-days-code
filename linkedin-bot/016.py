from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
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


    def find_busca(self):
        driver = self.driver
        campo_pesquisar = driver.find_element_by_xpath('//input[@placeholder="Pesquisar"]')
        campo_pesquisar.clear()
        sleep(2)
        campo_pesquisar.send_keys(self.profissao + Keys.ENTER)
        sleep(2)
##Caso queira mais filtros, basta trocar na função futuramente
#numero de conexões por exemplo
    def filtros(self):
        driver = self.driver
        filtropessoas = driver.find_element_by_xpath('//button[@aria-label="Pessoas"]')
        filtropessoas.click()
        sleep(2)

    def enviar_solicitacao(self):
        driver = self.driver
        conectar_buttons = driver.find_elements_by_class_name('entity-result__actions entity-result__divider')
    

        

bot = LinkedinBot('ablue@balue','senha ablue', 'criador de bots kkks')
bot.login()
bot.find_busca()
bot.filtros


        