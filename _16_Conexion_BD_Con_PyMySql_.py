import pymysql

class DataBase:
    def __init__(self): # -> None:
        self.connection = pymysql.connect(host = 'localhost',
                                          user='root',
                                          password ='root',
                                          db='world' 
                                          )
        self.cursor = self.connection.cursor()
    
#print("La conexion se ha establecido")

    
dataBase = DataBase()