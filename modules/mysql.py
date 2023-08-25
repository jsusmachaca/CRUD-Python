from pymysql import connect, DataError
from dotenv import load_dotenv
from os import getenv
import pymysql

load_dotenv()

def connection() -> bool:
    try:
        con = connect(
            host=getenv('DB_HOST'),
            user=getenv('DB_USER'),
            passwd=getenv('DB_PASSWORD'),
            db=getenv('DB_DATABASE')
        )

        return con
    except ConnectionRefusedError:
        return False
    except pymysql.err.OperationalError:
        return False

def insert_data(con, nombre: str, apellido: str, num: int) -> bool:
    try:
        with con.cursor() as cur:
            cur.execute(f'INSERT INTO Personas(nombre, apellido, numero) VALUES ("{nombre}", "{apellido}", "{num}");')
            con.commit()
        return True
    except DataError:
        return False

def show_all(con) -> tuple:
    with con.cursor() as cur:
        cur.execute('SELECT * FROM Personas')
        data = cur.fetchall()
    return data

def delete_data(con, id: int) -> None:
    with con.cursor() as cur:
        cur.execute(f'DELETE FROM Personas WHERE id={id};')
        con.commit()

def update_data(con, id: int, nombre: str, ape: str, numero: int) -> bool:
    try:
        with con.cursor() as cur:
            cur.execute(f'UPDATE Personas SET nombre="{nombre}", apellido="{ape}", numero={numero} WHERE id={id};')
            con.commit()
        return True
    except DataError:
        return False
    except pymysql.err.OperationalError:
        return False
    except pymysql.err.ProgrammingError:
        return False
