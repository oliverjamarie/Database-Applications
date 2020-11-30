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
        self.privilegeTypes = self.getPrivilegeTypes() 

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

        filter = 'GRANT USAGE ON *.* TO `{}`@`localhost`'.format(self.name)
        print (filter)
        if (filter in resultSTR):
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

    def getPrivilegeTypes(self):
        if self.db.user == 'root':
            return ['User has all privilege types']
        
        cmd = 'SHOW GRANTS FOR \'{}\'@\'localhost\''.format(self.name)
        result = self.execute(cmd)
        
        resultSTR = ''
        for i in result: 
            for j in i:
                resultSTR += j
        
        if('GRANT ALL PRIVILEGES ON `{}`.* TO `{}`@`localhost`'.format(self.db.database, self.db.user) in resultSTR):
            print ('FULL PRIVILIGES')
            return ['User has all priviliges types']

        print (resultSTR)
        list1 = resultSTR.split('GRANT')

        print(list1[2])
        list2 = list1[2].split('ON')

        print(list2[0])
        return list2[0].split(',')

    def getGrants(self):
        cmd = 'SHOW GRANTS FOR \'{}\'@\'localhost\''.format(self.name)

        return self.execute(cmd) 


        


        