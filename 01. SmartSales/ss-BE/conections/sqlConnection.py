import psycopg2
from .schemasSQL import schemas
from config import SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DATABASE

class SQLDB():
    def __init__(self):

        self.conection = psycopg2.connect(
            host = SQL_HOST,
            user = SQL_USER,
            password = SQL_PASSWORD,
            database = SQL_DATABASE
        )

        self.cursor = self.conection.cursor()

    def getDatabase(self, tableName:str, columns:str="*"):
        self.cursor.execute(f"SELECT {columns} FROM {tableName}")
        data = self.cursor.fetchall()
        response = [i for i in data]
        self.close()

        return response

    def getOne(self, tableName:str, filterColumn:str, filterValue:str, columns:str="*"):
        self.cursor.execute(f"SELECT {columns} FROM {tableName} WHERE {filterColumn} = '{filterValue}'")
        data = self.cursor.fetchone()
        response = data
        self.close()

        return response

    def putOne(self, tableName:str, data:dict):
        query = schemas[tableName]
        self.cursor.execute(query, data)
        self.close()

        return data

    def deleteOne(self, tableName:str, columnFilter:str, columnValue:str):
        self.cursor.execute(f"DELETE FROM {tableName} WHERE {columnFilter} = {columnValue}")
        self.close()

    def close(self):
        self.conection.commit()
        self.conection.close()
