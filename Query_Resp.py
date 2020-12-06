from mysql.connector import cursor

class Query_Resp:
    def __init__(self,cursor, queryStr:str):
        
        cursor.execute(queryStr)
        self.field_names = [i[0] for i in cursor.description]
        self.resp = cursor.fetchall()