import mysql.connector as connector
import json 




def getCredentials():
    credentials = {}
    with open ('Credentials.json') as f:
        credentials = json.load(f)
        return credentials



def connectToDB(user_index = 0, db_name = 'Project'):

    global data
    
    db = connector.connect(
        host = "localhost",
        user = data['users'][user_index]['name'],
        password = data['users'][user_index]['password'],
        database = db_name
    )

    return db   

data = getCredentials()
views = []
tables = []
mydb = connectToDB()
cursor = mydb.cursor()

def dispTables():
    global tables

    for table in tables:
        print (tables)

def dispTable(tableName:str):
    try:
        table = tables.index(tableName)
    except:
        print('Table not found')
        return

    cmd = 'select * from ' + tables[table]
    cursor.execute(cmd)

    result = cursor.fetchall()

    for i in result:
        print(i)
    

def dispViews():
    global views

    for view in views:
        print (view)

def dispView(viewName:str):
    try:
        view = views.index(viewName)
    except:
        print ('View not found')
        return

    cmd = 'select * from ' + views[view]
    cursor.execute(cmd)

    result = cursor.fetchall()

    for i in result:
        print(i)

def init():
    global cursor

    cursor.execute("show tables")

    for x in cursor:
        if '_View' in x[0]:
            views.append(x[0])
        else:
            tables.append(x[0])

def main():
    init()

    dispViews()
    dispView('Location_Building_View')

def getUsers():
    users = []

    cmd = 'select * from mysql.user;'
    cursor.execute(cmd)

    result = cursor.fetchall()

    for i in result:
        print(i[1])
        users.append(i[1])

    return users
            

main()