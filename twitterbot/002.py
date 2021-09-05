from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class BotTwitter():

    def __init__(self, username, password, link):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        self.link = link


    def login(self):
        driver = self.driver
        driver.get('https://twitter.com/login')
        sleep(5)
        campo_user = driver.find_element_by_xpath('//input[@name="session[username_or_email]"]')
        campo_user.click()
        sleep(0.5)
        campo_user.clear()
        campo_user.send_keys(self.username)
        campo_password = driver.find_element_by_xpath('//input[@name="session[password]"]')
        campo_password.click()
        sleep(0.5)
        campo_password.clear()
        campo_password.send_keys(self.password)
        sleep(0.5)
        login_butt = driver.find_element_by_xpath('//div[@data-testid="LoginForm_Login_Button"]')
        login_butt.click()
        sleep(6)


    def tweet(self):
        driver = self.driver
        campo_msg = driver.find_element_by_xpath('//div[@class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]')
        campo_msg.click()
        sleep(0.5)
        campo_msg.clear()
        sleep(1)
        campo_msg.send_keys(f'E lá vamos nós.... #100DaysOfCode #HundredDaysOfCode 004/100 {self.link}')
        sleep(2)
        tweet_button = driver.find_element_by_xpath('//div[@data-testid="tweetButtonInline"]')
        tweet_button.click()




botj = BotTwitter('@username', 'senha')
botj.login()
botj.tweet()