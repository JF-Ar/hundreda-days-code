from time import sleep
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager



class LinkedinBot():

    def iniciar(self):
        LinkedinBot.navegador_config()
        LinkedinBot.login()
        LinkedinBot.find_busca()
        LinkedinBot.filtros()
        LinkedinBot.enviar_solicitacao()


    def navegador_config(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())


    def login(self, username, password):
        driver = self.driver
        driver.get('https://linkedin.com/')
        campouser = driver.find_element_by_xpath('//input[@name="session_key"]')
        campouser.click()
        sleep(1)
        campouser.send_keys(username)
        camposenha = driver.find_element_by_xpath('//input[@name="session_password"]')
        camposenha.click()
        sleep(1)
        camposenha.send_keys(password)
        botao_entrar = driver.find_element_by_class_name('sign-in-form__submit-button').click()
        sleep(4)

    def find_busca(self, profissao):
        driver = self.driver
        sleep(4)
        campo_pesquisar = driver.find_element_by_xpath('//input[@placeholder="Pesquisar"]')
        campo_pesquisar.clear()
        sleep(2)
        campo_pesquisar.send_keys(profissao + Keys.ENTER)
        sleep(4)

##Caso queira mais filtros, basta colocar na função futuramente
#numero de conexões por exemplo
    def filtros(self):
        driver = self.driver
        all_filtros = driver.find_element_by_xpath('//button[@aria-label="Todos os filtros"]')
        all_filtros.click()
        
    def filtro_pessoas(self):
            driver = self.driver
            sleep(2)
            filtropessoas = driver.find_element_by_xpath('//button[@aria-label="Pessoas"]')
            filtropessoas.click()

#maior chance de conexão, boa feature para depois do GUI

    def filtro_grau_conexao(self):
        driver = self.driver
        terceiro_grau = driver.find_element_by_xpath('//input[@value="O"]')
        terceiro_grau.clik()

    def filtro_segundo_grau(self):
        driver = self.driver
        segundo_grau = driver.find_element_by_xpath('//input[@value="S"]')
        segundo_grau.click()

    def filtro_cidade(self):
        driver = self.driver
        mg = driver.find_element_by_id("advanced-filter-geoUrn-100358611")
        mg.click()

    def resultado(self):
        driver = self.driver
        exibir_resultados = driver.find_element_by_xpath('//button[@aria-label="Aplicar filtros atuais para exibir resultados"]')
        

    @staticmethod
    def digitando_como_pessoa(texto, campo_mensagem):
        for letra in texto:
            campo_mensagem.send_keys(letra)
            sleep(random.randint(1,5)/30)



    def enviar_solicitacao(self, mensagem):
        driver = self.driver
        #definindo a mensagem
        #mensagem = ( """Opa! Meu nome é Josué Junio e estou começando na nossa área e acho que esse conexão pode ser útil para ambos!\nEu me apaixonei pela programação e gostaria de fazer mais conexões.\nDe qualquer maneira, eu gostei do seu perfil e gostaria de manter contato. \n Um abraço!""")
        for i in range(0, 5):
                driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                sleep(2)
                tds_pags_buttons = driver.find_elements_by_tag_name('button')
                botao_conectar = [btn for btn in tds_pags_buttons if btn.text == "Conectar"]
                try:
                    for btn in botao_conectar:
                        driver.execute_script("arguments[0].click();", btn)
                        sleep(2)
                        adcionar_nota = driver.find_element_by_xpath('//button[@aria-label="Adicionar nota"]')
                        driver.execute_script("arguments[0].click();", adcionar_nota)
                        sleep(2)
                        nota = driver.find_element_by_xpath('//*[@id="custom-message"]')
                        LinkedinBot.digitando_como_pessoa(mensagem, nota)
                        sleep(1)
                        enviar = driver.find_element_by_xpath('//button[@aria-label="Enviar agora"]')
                        driver.execute_script("arguments[0].click();", enviar)
                        print('Indo para a proxima conexão')
                        sleep(2)
                
                    prox_pag = driver.find_element_by_xpath('//button[@aria-label="Avançar"]').click()
                    sleep(3)
                    print('proxima pagina')
                except Exception as e:
                    print(e)

##Popup de aviso semanal aria-label="Entendi"
