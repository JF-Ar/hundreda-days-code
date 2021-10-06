import PySimpleGUI as sg

from lkdinbot import LinkedinBot as bck




sg.theme('DarkGrey11')
layout = [
    [sg.Text('')],
    [sg.Text('Bem vindo!\n Coloque seu e-mail, senha\n digite a mensagem de convite e vamos começar.', font= 'Arial 14 italic')],
    [sg.Text('')],
    [sg.Text('Email', font='Arial 12 bold'), sg.InputText(key='-USERNAME-', font='Courier 13')],
    [sg.Text('Senha', font='Arial 12 bold'), sg.InputText(key='-PASSWORD-', password_char="*")],
    [sg.Text('Digite a profissão', font='Arial 12 bold'), sg.InputText(key='-PROFISSAO-', font='Courier 13')],
    [sg.Text('')],
    [sg.Text('DIGITE UMA MENSAGEM:',font='Courier 13 underline')],
    [sg.Text('', size=(6,0)), sg.Multiline(size=(30,12),key='-MENSAGEM-', font='Courier 11'), sg.Button('COMEÇAR', button_color=('#00804b'),font='Arial 12 bold')],
    [sg.Text('')],
    [sg.Text('OUTPUT', font='Courier 13 underline')],
    [sg.Output(size=(35,20), font='Courier 13'), sg.Button('SAIR', button_color=('red'), font='Arial 12 bold'),sg.Text('')]

]
window = sg.Window('linkedin Bot App', layout, size=(400, 670), element_justification='center')    



while True:             
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'SAIR'):
        sg.popup('GoodBay!', font='Arial')
        break

    if event == 'COMEÇAR':
            if values['-USERNAME-'].strip() == '':
                print('Email ou senha invalidos.')
            elif values['-PASSWORD-'].strip() == '':
                print('Email ou senha invalidos')
            elif values['-PROFISSAO-'].strip() == '':
                print('Digite uma profissão para a busca.')
            
            else:
                print('Ok, Vamos começar!')
                print('Aqui, você verá o resultado\nde suas conexções.')
                print('Tente não utilizar o\nnavegador em execução!')
                print('=-'*10)
                bck()
                bck.navegador_config(bck)
                bck.login(bck, values['-USERNAME-'], values['-PASSWORD-'])
                bck.find_busca(bck, values['-PROFISSAO-'])
                bck.filtro_pessoas(bck)
                bck.enviar_solicitacao(bck, values['-MENSAGEM-'])
            



                    
window.close()
