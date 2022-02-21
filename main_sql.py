import os
import psycopg2

from dotenv import load_dotenv
from psycopg2 import Error


load_dotenv()


try:
    connection = psycopg2.connect(user=os.getenv('USER'),
                                  password=os.getenv('PASWORD'),
                                  host="127.0.0.1",
                                  port="5432",
                                  database=os.getenv('NAME_DB'))

    cursor = connection.cursor()
    create_table_query = '''create table images(id int, image bytea);'''
    record_table_file = '''insert into images values (1, pg_read_binary_file('/path/to/image.jpg')::bytea);'''
    # Выполнение команды: это создает новую таблицу
    cursor.execute(create_table_query)
    cursor.execute(record_table_file)
    connection.commit()

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
