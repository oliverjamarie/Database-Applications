import mysql.connector as connector
import json

from mysql.connector import cursor

class Connection:
    def __init__(self, db_name='Project', user_index = 0, userName= '', psswrd = ''):
        credentials = {}
        self.name = userName

        with open ('Credentials.json') as f:
            credentials = json.load(f)
        
        if userName == '' and psswrd == '':
            self.name = credentials['users'][user_index]['name']
            psswrd = credentials['users'][user_index]['password']

        print('Connecting to \t', self.name)

        self.db = connector.connect(
            host = "localhost",
            user = self.name,
            password = psswrd,
            database = db_name
        )

        self.cursor = self.db.cursor()

        self.tables = []
        self.views = []

        self.cursor.execute("show tables")
        for x in self.cursor:
            if '_View' in x[0]:
                self.views.append(x[0])
            else:
                self.tables.append(x[0])

    def execute(self, queryMsg:str = ''):
        self.cursor.execute(queryMsg)
        
        return self.cursor.fetchall()