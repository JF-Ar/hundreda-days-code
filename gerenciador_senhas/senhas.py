import sqlite3

MASTER_SENHA = '123456'

senha = input('Insira a senha master: ')
if senha != MASTER_SENHA:
    print('Senha inválida. Paramos por aqui...')
    exit()

conn = sqlite3.connect('senhas.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULl
);
''')

def menu():
    print('=-'*18)
    print('* I:  Insira uma nova senha')
    print('* L:  Lista de serviços salvos ')
    print('* R:  Recuperar senha uma nova senha')
    print('* S:  Sair')
    print('=-'*18)

def recupera_senha(service):
    cursor.execute(f'''
    SELECT username, password FROM users
    WHERE service = '{service}'
    ''')

    if cursor.rowcount == 0:
        print('Serviço não cadasrtado (use "I" para verificar os serviços).')
    else:
        for user in cursor.fetchall():
            print(user)


def inserir_servicos(service, username, password):
    cursor.execute(f'''
    INSERT INTO users (service, username, password)
    VALUES ('{service}', '{username}', '{password}')
    ''')
    conn.commit()

def mostrar_servicos():
    cursor.execute('''
    SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)


while True:
    menu()
    opcao = input('Escolha uma das opções: ')
    if opcao not in ['I' , 'L', 'R', 'S']:
        print('')
        print('Escolha uma opção valida do menu.')
        continue
    if opcao == 'S':
        break

    if opcao == 'I':
        service = input('Qual o nome do serviço? ')
        username = input('Qual o nome de usuario? ')
        password = input('Qual a senha? ')
        inserir_servicos(service, username, password)

    if opcao == 'L':
        mostrar_servicos()

    if opcao == 'R':
        service = input('De qual serviço gostaria de recuperar a senha? ')
        recupera_senha(service)

conn.close()
