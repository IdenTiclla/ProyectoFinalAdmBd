import pyodbc

server = "Servidor.SC.LOCAL"
database = "master"
username = "sa"
password = "Passw0rd"

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

class Ejecutar(object):
    def create_dbs(self,nombre):
        cursor = cnxn.cursor()
        cursor.execute('CREATE DATABASE {0}'.format(nombre))
        cnxn.commit()
        return True


