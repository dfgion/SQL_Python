from dbtool import DBtolls
import psycopg2
import logging

DBTool = DBtolls(database = '', password = '')

def client():
    print('Введите /exit, чтобы выйти из режима добавления')
    name = input('Введите имя клиента:\n')
    if name == '/exit':
        logging.info('FUNCTION. Progress reset')
        return ''
    logging.info('FUNCTION. Progress.. 25%')
    lastname = input('Введите фамилию клиента:\n')
    if lastname == '/exit':
        logging.info('FUNCTION. Progress reset')
        return ''
    logging.info('FUNCTION. Progress.. 50%')
    email = input('Введите email клиента:\n')
    if email == '/exit':
        logging.info('FUNCTION. Progress reset')
        return ''
    logging.info('FUNCTION. Progress.. 75%')
    if name and lastname and email:
        DBTool.add_client(name=name, lastname=lastname, email=email)
        logging.info('FUNCTION. Progress.. 100%')
        logging.info('MAIN. Tables have been created')
    else:
        print('Некорректно введено имя, фамилия или email')
        logging.error('FUNCTION. Progress reset')

def number():
    print('Введите /exit, чтобы выйти из режима добавления')
    search_name = input('Введите имя клиента:\n')
    if search_name == '/exit':
        logging.info('FUNCTION. Progress reset')
        return ''
    logging.info('FUNCTION. Progress.. 20%')
    search_lastname = input('Введите фамилию клиента:\n')
    if search_lastname == '/exit':
        logging.info('FUNCTION. Progress reset')
        return ''
    logging.info('FUNCTION. Progress.. 40%')
    search_email = input('Введите email клиента:\n')
    if search_email == '/exit':
        return ''
    logging.info('FUNCTION. Progress.. 60%')
    number = input('Введите телефонный номер клиента:\n')
    if number == '/exit':
        logging.info('FUNCTION. Progress reset')
        return ''
    logging.info('FUNCTION. Progress.. 80%')
    if search_name and search_lastname and search_email and number:
        DBTool.add_number(search_name=search_name, search_lastname=search_lastname, search_email=search_email, number=number)
        logging.info('FUNCTION. Progress.. 100%')
    else:
        logging.error('FUNCTION. Progress reset')
        print('Некорректно введено имя, фамилия, email или номер телефона')

def changeInfo():
    print('Введите /exit, чтобы выйти из режима изменения')
    name = input('Введите имя, на которое хотите изменить, либо введите текущее:\n')
    if name == '/exit':
        logging.info('FUNCTION. Progress reset')
        return ''
    logging.info('FUNCTION. Progress.. 12,5%')
    lastname = input('Введите фамилию, на которую хотите изменить, либо введите текущую:\n')
    if lastname == '/exit':
        logging.info('FUNCTION. Progress reset')
        return ''
    logging.info('FUNCTION. Progress.. 25%')
    email = input('Введите email, на который хотите изменить, либо введите текущий:\n') 
    if email == '/exit':
        logging.info('FUNCTION. Progress reset')
        return ''
    logging.info('FUNCTION. Progress.. 37,5%')
    id = input('Введите id пользователя:\n') 
    if id == '/exit':
        logging.info('FUNCTION. Progress reset')
        return ''
    logging.info('FUNCTION. Progress.. 50%')
    help = input('Хотите ли изменить телефон клиента? Да/Нет \n')
    if help == 'Да':
        number = input('Введите номер, на который хотите изменить, либо введите текущий:\n')
        DBTool.change_info(changed_name=name, changed_lastname=lastname, changed_email=email, change_number=number, id=id)
        logging.info('FUNCTION. Progress.. 100%')
    elif help == 'Нет':
        DBTool.change_info(changed_name=name, changed_lastname=lastname, changed_email=email, change_number=None, id=id)
        logging.info('FUNCTION. Progress.. 100%')
    elif help == '/exit':
        logging.info('FUNCTION. Progress reset')
        return ''
    else:
        logging.error('FUNCTION. Progress reset')
        print("Некорректный ответ")

def delNumber():
    print('Введите /exit, чтобы выйти из режима удаления')
    name = input('Введите имя клиента:\n')
    if name == '/exit':
        logging.info('FUNCTION. Progress reset')
        return ''
    logging.info('FUNCTION. Progress.. 25%')
    lastname = input('Введите фамилию клиента:\n')
    if lastname == '/exit':
        logging.info('FUNCTION. Progress reset')
        return ''
    logging.info('FUNCTION. Progress.. 50%')
    email = input('Введите email клиента:\n')
    if email == '/exit':
        logging.info('FUNCTION. Progress reset')
        return ''
    logging.info('FUNCTION. Progress.. 75%')
    if name and lastname and email:
        DBTool.delete_num(name=name, lastname=lastname, email=email)
        logging.info('FUNCTION. Progress.. 100%')
    else:
        logging.error('FUNCTION. Progress reset')
        print('Некорректно введено имя, фамилия или email')

def delClient():
    print('Введите /exit, чтобы выйти из режима удаления')
    name = input('Введите имя клиента:\n')
    if name == '/exit':
        logging.info('FUNCTION. Progress reset')
        return ''
    logging.info('FUNCTION. Progress.. 25%')
    lastname = input('Введите фамилию клиента:\n')
    if lastname == '/exit':
        logging.info('FUNCTION. Progress reset')
        return ''
    logging.info('FUNCTION. Progress.. 50%')
    email = input('Введите email клиента:\n')
    if email == '/exit':
        logging.info('FUNCTION. Progress reset')
        return ''
    logging.info('FUNCTION. Progress.. 75%')
    if name and lastname and email:
        DBTool.delete_client(name=name, lastname=lastname, email=email)
        logging.info('FUNCTION. Progress.. 100%')
    else:
        logging.error('FUNCTION. Progress reset')
        print('Некорректно введено имя, фамилия или email')
        
def searchClient():
    with psycopg2.connect(database = 'Inf_ab_Clients', user = 'postgres', password = 'jjUUhy23') as conn:
        print('Введите /exit, чтобы выйти из режима поиска')
        name = input('Введите имя клиента:\n')
        if name == '/exit':
                logging.info('FUNCTION. Progress reset')
                return ''
        logging.info('FUNCTION. Progress.. 25%')
        with conn.cursor() as cur:
            cur.execute("""
            SELECT id FROM Clients
            WHERE name=%s;
            """, (name,))
            if len(cur.fetchall()) > 1:
                print('Клиентов с таким именем несколько, добавьте фамилию')
                lastname = input('Введите фамилию клиента:\n')
                if lastname == '/exit':
                    logging.info('FUNCTION. Progress reset')
                    return ''
                logging.info('FUNCTION. Progress.. 50%')
                cur.execute("""
                SELECT id FROM Clients
                WHERE name=%s and lastname=%s;
                """, (name, lastname))
                if len(cur.fetchall()) > 1:
                    print('Клиентов с таким именем и фамилией несколько, добавьте email')
                    email = input('Введите email клиента:\n')
                    if email == '/exit':
                        logging.info('FUNCTION. Progress reset')
                        return ''
                    logging.info('FUNCTION. Progress.. 75%')
                    info = [x for x in DBTool.search_client(name=name, lastname=lastname, email=email)]
                    print(f'id : {info[0]}')
                    print(f'Имя : {info[1]}')
                    print(f'Фамилия : {info[2]}')
                    print(f'Email : {info[3]}')
                    info_number = DBTool._search_by_number(info[0])
                    if info_number == 'У клиента нет зарегистированных номеров':
                        logging.info('FUNCTION. Progress.. 100%')
                        print(f'{info_number}')
                    else:
                        print(f'У клиента {len(info_number)} номер(а):')
                        for element in [x for x in info_number]:
                            print(element)
                        logging.info('FUNCTION. Progress.. 100%')
                else:
                    info = [x for x in DBTool.search_client(name=name, lastname=lastname)]
                    print(info)
                    print(f'id : {info[0]}')
                    print(f'Имя : {info[1]}')
                    print(f'Фамилия : {info[2]}')
                    print(f'Email : {info[3]}')
                    info_number = DBTool._search_by_number(info[0])
                    if info_number == 'У клиента нет зарегистированных номеров':
                        print(f'{info_number}')
                        logging.info('FUNCTION. Progress.. 100%')
                    else:
                        print(f'У клиента {len(info_number)} номер(а):')
                        for element in [x for x in info_number]:
                            print(element)
                        logging.info('FUNCTION. Progress.. 100%')
            else:
                info = [x for x in DBTool.search_client(name=name)]
                print(f'id : {info[0]}')
                print(f'Имя : {info[1]}')
                print(f'Фамилия : {info[2]}')
                print(f'Email : {info[3]}')
                info_number = DBTool._search_by_number(info[0])
                if info_number == 'У клиента нет зарегистированных номеров':
                    print(f'{info_number}')
                    logging.info('FUNCTION. Progress.. 100%')
                else:
                    print(f'У клиента {len(info_number)} номер(а):')
                    for element in [x for x in info_number]:
                        print(element)
                    logging.info('FUNCTION. Progress.. 100%')