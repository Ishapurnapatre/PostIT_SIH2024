# database.py
import sqlite3

class DatabaseManager:
    def __init__(self, db_path='letters.db'):
        self.connection = sqlite3.connect(db_path)
        self.create_table()
    
    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS letters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT,
            receiver TEXT,
            address TEXT,
            pin TEXT
        )
        '''
        self.connection.execute(query)
        self.connection.commit()
    
    def insert_letter(self, sender, receiver, address, pin):
        query = 'INSERT INTO letters (sender, receiver, address, pin) VALUES (?, ?, ?, ?)'
        self.connection.execute(query, (sender, receiver, address, pin))
        self.connection.commit()
    
    def get_all_letters(self):
        cursor = self.connection.execute('SELECT * FROM letters')
        return cursor.fetchall()
    
    def close(self):
        self.connection.close()
