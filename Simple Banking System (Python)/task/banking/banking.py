# Importando bibliotecas
import random
import sqlite3

# Creando la base de datos
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()

# Creando la tabla
cur.execute('CREATE TABLE IF NOT EXISTS card (id INTEGER, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);')
conn.commit()

# Función para el menú
def menu():
    print('1. Create an account')
    print('2. Log into account')
    print('0. Exit')
    return input('>')

# Función para crear una cuenta
def create_account():
    id = random.randint(100000000, 999999999)
    card_number = '400000' + str(id)
    card_number += str(luhn_algorithm(card_number))
    pin = random.randint(1000, 9999)
    cur.execute('INSERT INTO card (id, number, pin) VALUES (?, ?, ?);', (id, card_number, pin))
    conn.commit()
    print('Your card has been created')
    print('Your card number:')
    print(card_number)
    print('Your card PIN:')
    print(pin)

# Función para el algoritmo de Luhn
def luhn_algorithm(card_number):
    card_number = [int(x) for x in card_number]
    for i in range(0, len(card_number), 2):
        card_number[i] *= 2
        if card_number[i] > 9:
            card_number[i] -= 9
    return (10 - sum(card_number) % 10) % 10

# Función para iniciar sesión
def log_in():
    print('Enter your card number:')
    card_number = input('>')
    print('Enter your PIN:')
    pin = input('>')
    cur.execute('SELECT number, pin FROM card WHERE number = ? AND pin = ?;', (card_number, pin))
    if cur.fetchone() is None:
        print('Wrong card number or PIN!')
    else:
        print('You have successfully logged in!')
        logged_in_menu(card_number)

# Función para el menú de sesión iniciada
def logged_in_menu(card_number):
    while True:
        print('1. Balance')
        print('2. Add income')
        print('3. Do transfer')
        print('4. Close account')
        print('5. Log out')
        print('0. Exit')
        option = input('>')
        if option == '1':
            cur.execute('SELECT balance FROM card WHERE number = ?;', (card_number,))
            print('Balance:', cur.fetchone()[0])
        elif option == '2':
            print('Enter income:')
            income = int(input('>'))
            cur.execute('UPDATE card SET balance = balance + ? WHERE number = ?;', (income, card_number))
            conn.commit()
            print('Income was added!')
        elif option == '3':
            print('Transfer')
            print('Enter card number:')
            transfer_card_number = input('>')
            if transfer_card_number == card_number:
                print("You can't transfer money to the same account!")
            elif luhn_algorithm(transfer_card_number[:-1]) != int(transfer_card_number[-1]):
                print('Probably you made a mistake in the card number. Please try again!')
            else:
                cur.execute('SELECT number FROM card WHERE number = ?;', (transfer_card_number,))
                if cur.fetchone() is None:
                    print('Such a card does not exist.')
                else:
                    print('Enter how much money you want to transfer:')
                    transfer_amount = int(input('>'))
                    cur.execute('SELECT balance FROM card WHERE number = ?;', (card_number,))
                    if transfer_amount > cur.fetchone()[0]:
                        print('Not enough money!')
                    else:
                        cur.execute('UPDATE card SET balance = balance - ? WHERE number = ?;', (transfer_amount, card_number))
                        cur.execute('UPDATE card SET balance = balance + ? WHERE number = ?;', (transfer_amount, transfer_card_number))
                        conn.commit()
                        print('Success!')
        elif option == '4':
            cur.execute('DELETE FROM card WHERE number = ?;', (card_number,))
            conn.commit()
            print('The account has been closed!')
            break
        elif option == '5':
            print('You have successfully logged out!')
            break
        elif option == '0':
            print('Bye!')
            exit()

# Función principal
while True:
    choice = menu()
    if choice == '1':
        create_account()
    elif choice == '2':
        log_in()
    elif choice == '0':
        print('Bye!')
        exit()

# Cerrando la base de datos
conn.close()


