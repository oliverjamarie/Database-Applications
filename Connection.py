import mysql.connector as connector
import json
import re
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

        self.privileges = self.getPrivileges()

    # returns a list for the result
    def execute(self, queryMsg:str = ''):
        self.cursor.execute(queryMsg)
        
        return self.cursor.fetchall()

    def getPrivileges(self):
        cmd = 'SHOW GRANTS FOR \'{}\'@\'localhost\''.format(self.name)
        result = self.execute(cmd)
        
        resultSTR = ''
        for i in result: 
            resultSTR += i[0]

        print (resultSTR)
        #print(type('ON `{}.*'.format(self.db.database)))

        if ('ON `{}`.*'.format(self.db.database) in resultSTR):
            print('Access to all tables')
            return ['User has access to all tables']
        
        if (self.db.user == 'root'):
            return ['User has root access']
        
        # Regular expression to extract the permissions 
        # \`[a-z|A-Z]+\`\.\`[a-z|A-Z|_]+\`


        parse = re.findall('\`[a-z|A-Z]+\`\.\`[a-z|A-Z|_]+\`', resultSTR)

        perms = []

        for i in parse:
            li = i.split('.')
            perms.append(li[1][1:-1]) #string slicing to remeove the quotation marks

            

        return perms


        


        