from datos.db import Ejecutar

db = Ejecutar()


class NewDb(object):
    def __init__(self,Nombre):
        self.Nombre = Nombre
    def create_db(self):
        res = db.create_dbs(self.Nombre)
        if res:
            return True
        else:
            return False

