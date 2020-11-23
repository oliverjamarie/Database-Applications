import mysql.connector as connector
import json

class Connection:
    def __init__(self, db_name='Project', user_index = 0, userName= '', psswrd = ''):
        credentials = {}
        with open ('Credentials.json') as f:
            credentials = json.load(f)
        
        if userName == '' and psswrd == '':
            userName = credentials['users'][user_index]['name']
            psswrd = credentials['users'][user_index]['password']

        print('Connecting to \t', userName)
        self.db = connector.connect(
            host = "localhost",
            user = userName,
            password = psswrd,
            database = db_name
        )

        self.cursor = self.db.cursor()