from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui


class InstaBot():

    def __init__(self, username, password, hastag):
        mobile_emulation = mobile_emulation = {

    "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },

    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.chrome_options)
        self.username = username
        self.password = password
        self.hastag = hastag

    def login (self):
        driver = self.driver
        driver.get('https://instagram.com/')
        sleep(2)
    #pagina de login anterior ao login comum
        entrar = driver.find_element_by_xpath('//button[text()="Entrar"]').click()
        sleep(4)
        camp_user = driver.find_element_by_xpath('//input[@name="username"]')
        camp_user.click()
        sleep(0.5)
        camp_user.send_keys(self.username)
        sleep(0.4)
        camp_password = driver.find_element_by_xpath('//input[@name="password"]')
        camp_password.click()
        sleep(0.3)
        camp_password.send_keys(self.password)
        submit = driver.find_element_by_xpath('//button[@type="submit"]')
        submit.click()
        sleep(5)

    def fist_popup(self):
        driver = self.driver
    #colocando no metodo try, caso precise da função em outro momento
        try:
            notnow = driver.find_element_by_xpath('//button[text()="Agora não"]')
            notnow.click()
            sleep(8)
        except:
            print('Tentando outro metodo')
            notnow = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/button')
            notnow.click()
            sleep(8)
    
    def second_popup(self):
        driver = self.driver
        try:
            cancel = driver.find_element_by_xpath('//button[text()="Cancelar"]')
            cancel.click()
            sleep(3)
        except:
            print('Tentando de outro modo')
            cancel = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
            cancel.click()
            sleep(3)

    ###Aqui a função para publicar no feed. (não foi um grande desafio)
    '''def post_feed(self, legenda):
        driver = self.driver
        button_post = driver.find_element_by_xpath('//div[@data-testid="new-post-button"]')
        button_post.click()
        foto = pyautogui.moveTo(x = 502, y = 325) #local da foto no PC tive problemas com o pyautogui
        sleep(1)
        pyautogui.click(foto)
        sleep(1)
        pyautogui.press('enter')
        sleep(4)
        button_avancar = driver.find_element_by_xpath('//button[text()="Avançar"]')
        button_avancar.click()
        sleep(2)
        box_text = driver.find_element_by_xpath('//textarea[@aria-label="Escreva uma legenda..."]')
        box_text.click()
        sleep(0.5)
        pyautogui.write(self.hastag + legenda, interval=0.22)
        sleep(3)
        compartilhar = driver.find_element_by_xpath('//button[text()="Compartilhar"]')
        compartilhar.click()'''

    
    def girar_cell(self):  #quando chegamos selecionamos a foto, o instagram pede pra girar o telefone (??)
        driver = self.driver
        pyautogui.press('f12')
        sleep(3)
        pyautogui.hotkey('command', 'shift', 'm')
        sleep(3)
        #após 'girar' o telefone aparecem popups
        try:
            notnow = driver.find_element_by_xpath('//button[text()="Agora não"]')
            notnow.click()
            sleep(2)
        except:
            print('Tentando outro metodo')
            notnow = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/button')
            notnow.click()
            sleep(2)

    def publicar_story(self):
        jbot.girar_cell()

        driver = self.driver
        icon_story = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav[1]/div/div/header/div/div[1]/button')
        icon_story.click()
    #Agora inserimos o pyautogui para interagir com o MacOs
        sleep(4)
        foto = pyautogui.moveTo(x = 492, y = 305)
        sleep(1)
        pyautogui.click(foto)
        pyautogui.press('enter')
        sleep(2)
    #agora sim publicar + legenda
        pyautogui.moveTo(x = 735, y = 159)
        sleep(1)
        pyautogui.click()
        sleep(3)
        text = pyautogui.moveTo(x = 509, y = 240)
        sleep(1)
        pyautogui.click(text)
        pyautogui.write(self.hastag, interval=0.22)
        sleep(1)
        concluir = pyautogui.moveTo(x = 509, y = 240)
        sleep(1)
        pyautogui.click(concluir)
        sleep(2)
        publicar = pyautogui.moveTo(x = 268, y = 822)
        pyautogui.click(publicar)


jbot = InstaBot('username', '124senha!', '#100DaysOfCode')
jbot.login()
jbot.fist_popup()
jbot.second_popup()
jbot.publicar_story()
#jbot.post_feed('Pelo menos eu consigo publicar no feed! #python #codebot') 