import psycopg2
import logging

class DBtolls:
    logging.basicConfig(level = logging.INFO, 
                        filename = "py_log.log",
                        filemode = "w",
                        format = "%(asctime)s %(levelname)s %(message)s",
                        encoding = 'utf-8')

    def __init__(self, database, password):
         self.database = database
         self.password = password

    def createtables(self):
        logging.info('FUNCTION createtables has been activated')
        with psycopg2.connect(database = self.database, user = 'postgres', password = self.password) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                CREATE TABLE IF NOT EXISTS Clients(
                                    id SERIAL PRIMARY KEY, 
                                    name VARCHAR(40) NOT NULL,
                                    lastname VARCHAR(40) NOT NULL,
                                    email text UNIQUE NOT NULL 
                                    );""")
                cur.execute("""
                CREATE TABLE IF NOT EXISTS Telephone_numbers(
                                    id SERIAL PRIMARY KEY, 
                                    number text UNIQUE NOT NULL,
                                    id_of_client int4 NOT NULL REFERENCES Clients(id)
                                    );""")
                conn.commit()

    def add_client(self, name, lastname, email):
        logging.info('FUNCTION add_client has been activated')
        with psycopg2.connect(database = self.database, user = 'postgres', password = self.password) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                INSERT INTO Clients(name, lastname, email) 
                VALUES(%s, %s, %s);
                """, (name, lastname, email))
                conn.commit()

    def add_number(self, search_email, search_name, search_lastname, number):
        logging.info('FUNCTION add_number has been activated')
        with psycopg2.connect(database = self.database, user = 'postgres', password = self.password) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                INSERT INTO Telephone_numbers(number, id_of_client)
                VALUES(%s, (SELECT id FROM Clients
                WHERE name=%s and lastname=%s and email=%s));
                """, (number, search_name, search_lastname, search_email))
                conn.commit()

    def dropdb(self):
        logging.warning('FUNCTION dropdb has been activated')
        with psycopg2.connect(database = self.database, user = 'postgres', password = self.password) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                DROP TABLE Telephone_numbers;
                """)
                cur.execute("""
                DROP TABLE Clients;
                """)
                conn.commit()

    def change_info(self, changed_name, changed_lastname, changed_email, id, change_number):
        logging.info('FUNCTION change_info has been activated')
        with psycopg2.connect(database = self.database, user = 'postgres', password = self.password) as conn:
            with conn.cursor() as cur: 
                cur.execute("""
                UPDATE Clients SET name=%s,  lastname=%s, email=%s
                WHERE id=%s RETURNING id;
                """, (changed_name, changed_lastname, changed_email, id))
                print(cur.fetchall())
                if change_number != None:
                    cur.execute("""
                    UPDATE Telephone_numbers SET number=%s
                    WHERE id_of_client=%s;
                    """, (change_number, id))
                conn.commit()

    def delete_num(self, name, lastname, email):
        logging.info('FUNCTION delete_num has been activated')
        with psycopg2.connect(database = self.database, user = 'postgres', password = self.password) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                DELETE FROM Telephone_numbers
                WHERE id_of_client=(SELECT id FROM Clients
                WHERE name=%s and lastname=%s and email=%s);
                """, (name, lastname, email))
                conn.commit()

    def delete_client(self, name, lastname, email):
        logging.info('FUNCTION delete_client has been activated')
        with psycopg2.connect(database = self.database, user = 'postgres', password = self.password) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                DELETE FROM Telephone_numbers
                WHERE id_of_client=(SELECT id FROM Clients
                WHERE name=%s and lastname=%s and email=%s);
                """, (name, lastname, email)) 
                cur.execute("""
                DELETE FROM Clients
                WHERE name=%s and lastname=%s and email=%s;
                """, (name, lastname, email))
                conn.commit()
            
    def search_client(self, name, lastname=None, email=None):
        logging.info('FUNCTION search_client has been activated')
        with psycopg2.connect(database = self.database, user = 'postgres', password = self.password) as conn:
            with conn.cursor() as cur: # Этот курсор возвращает информацию, если в дальнейшей проверке условия if условие ложно 
                cur.execute("""
                SELECT id, name, lastname, email FROM Clients
                WHERE name=%s;
                """, (name,))
                for element in cur.fetchall():
                    info_cur = element
            with conn.cursor() as cur: # Этот курсор берет информацию о длине списка кортежей, чтобы таким образом понять, было ли возвращено более 1 строчки, то есть более одного пользователя
                cur.execute("""
                SELECT id, name, lastname, email FROM Clients
                WHERE name=%s;
                """, (name,))
                curlen = len(cur.fetchall())
            if curlen > 1:
                with conn.cursor() as curs: # Этот курсор возвращает информацию, если в дальнейшей проверке условия if условие ложно
                    curs.execute("""
                    SELECT id, name, lastname, email FROM Clients
                    WHERE name=%s and lastname=%s;
                    """, (name, lastname))
                    for element in curs.fetchall():
                        info_curs = element
                with conn.cursor() as curs: # Этот курсор берет информацию о длине списка кортежей, чтобы таким образом понять, было ли возвращено более 1 строчки, то есть более одного пользователя
                    curs.execute("""
                    SELECT id, name, lastname, email FROM Clients
                    WHERE name=%s and lastname=%s;
                    """, (name, lastname))
                    curlen_1 = len(curs.fetchall())
                if curlen_1 > 1:
                    with conn.cursor() as cursor: # Этот курсор возвращает информацию, если в дальнейшей проверке условия if условие ложно
                        cursor.execute("""
                        SELECT id, name, lastname, email FROM Clients
                        WHERE name=%s and lastname=%s and email=%s;
                        """, (name, lastname, email))
                        for element in cursor.fetchall():
                            info_cursor = element
                        return info_cursor
                else:
                    return info_curs
            else:
                return info_cur

    def _search_by_number(self, id):
        logging.info('FUNCTION search_by_number has been activated')
        with psycopg2.connect(database = self.database, user = 'postgres', password = self.password) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                SELECT number FROM Telephone_numbers
                WHERE id_of_client=%s;
                """, (id,))
                info = cur.fetchall()
            try:
                check = info[0]
                new_turple = ()
                for element in info:
                    new_turple = new_turple + element
                return new_turple
            except:
                logging.warning('DBTOOL. No registered numbers')
                return 'У клиента нет зарегистированных номеров'
    
