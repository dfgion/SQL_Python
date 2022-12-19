import logging
from functions_main import *

def main():
    while True:
        HELP = """
        /createdb - Создает структуру БД(Таблицы)
        /client - Добавить нового клиета
        /number - Добавить телефон для существующего клиента
        /changeInfo - Позволяет изменить данные о клиенте
        /delNumber - Удаляет номер для определнного клиента
        /delClient - Удаляет информацию о клиенте
        /searchClient - Позволяет найти клиента по данным
        /delTables - Удаление всех существующих таблиц
        /exit - Завершение работы
        """
        command = input('Введите команду:\n')
        if command == '/help':
            print(HELP)
        elif command == '/createdb':
            logging.info('MAIN. Create tables...')
            DBTool.createtables()
        elif command == '/client':
            logging.info('MAIN. Adding new client information')
            client()
        elif command == '/number':
            number()
        elif command == '/changeInfo':
            changeInfo()
        elif command == '/delNumber':
            delNumber()
        elif command == '/delClient':
            delClient()
        elif command == '/delTables':
            logging.warning('MAIN. TABLES HAVE BEEN DROPPED')
            DBTool.dropdb()
        elif command == '/searchClient':
            searchClient()
        elif command == '/exit':
            return 'Завершение работы'
        else:
            print('/help - Получить справку по командам')
        
if __name__ == "__main__":
    logging.basicConfig(level = logging.INFO, 
                        filename = "py_log.log",
                        filemode = "w",
                        format = "%(asctime)s %(levelname)s %(message)s",
                        encoding = 'utf-8')
    main()
        



