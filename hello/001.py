import pyttsx3
from os import system, name

def limparterminal ():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def menu ():
    print('=-'*20)
    print('''    HELLO ITS ME!
    KS KS KS KKS
    DIGAMOS QUE EU SEJA O CEREBRO E VOCÊ O PINK. 
    DAI VOCÊ DIZ, "O QUE VAMOS FAZER HOJE?"''')
    print('=-'*20)


def fala ():
    robo = pyttsx3.init()
    voices = robo.getProperty('voices')
    robo.setProperty('voice', voices[22].id)
    rate = robo.getProperty('rate')
    robo.setProperty('rate', rate-10)
    robo.say('HELLO ITS ME! KS KS KS KKS DIGAMOS QUE EU SEJA O CEREBRO E VOCÊ O PINK. DAí VOCÊ DIZ, "O QUE VAMOS FAZER HOJE?"')
    robo.runAndWait()
    input('Se você é o PINK da ENTER aí')
    text = open('/Users/mac/Documents/HundredDaysCode/o que vamos fazer hoje.txt', 'r', encoding= "utf-8")
    arquivo = text.read()
    robo = pyttsx3.init()
    robo.say(arquivo)
    robo.runAndWait()


limparterminal()
menu()
fala()