
import json 
from Connection import Connection

class User:
    def __init__(self):
        self.__setup_variables()
    def __setup_variables(self):
        self.host:str
        self.user:str
        self.select_priv:bool 
        self.insert_priv:bool 
        self.update_priv:bool
        self.delete_priv:bool
        self.create_priv:bool
        self.drop_priv:bool 
        self.reload_priv:bool 
        self.shutdown_priv:bool 
        self.process_priv:bool 
        self.file_priv:bool
        self.grant_priv:bool
        self.references_priv:bool
        self.index_priv:bool
        self.alter_priv:bool
        self.show_db_priv:bool
        self.super_priv:bool
        self.create_tmp_table_priv:bool
        self.lock_tables_priv:bool
        self.execute_priv:bool
        self.repl_slave_priv:bool 
        self.create_view_priv:bool
        self.show_view_priv:bool
        self.create_routine_priv:bool
        self.alter_routine_priv:bool
        self.create_user_priv:bool
        self.event_priv:bool
        self.trigger_priv:bool
        self.create_tablespace_priv:bool


def getCredentials():
    credentials = {}
    with open ('Credentials.json') as f:
        credentials = json.load(f)
        return credentials


user = User()
data = getCredentials()
views = []
tables = []
connect = Connection()
mydb = connect.db
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

    getUsers()

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