import sqlite3
from sqlite3 import Error
from tkinter.messagebox import NO

def create_connection(path='default_test_db.sqlite'):
    conn = None

    try:
        conn = sqlite3.connect(path)
        print('Connection to sqlite3 DB succesful')
    except Error as e:
        print(f'The error "{e}" occurred')
    
    return conn

def main():
    create_connection()

if __name__ == '__main__':
    main()