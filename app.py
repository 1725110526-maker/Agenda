import web
import sqlite3

urls = (
    '/', 'controlles.index.Index',
    '/lista_contactos','controllers.lista_contactos.Lista_Contactos',
)
app = web.application(urls, globals())

class listacontactos:
    def conectar(self):
        try:
            conexion=sqlite3.connect("../sql/agenda.db")
            conexion.row_factory = sqlite3.Row
        except  Exception as error;
            print (f"Error 100:{error.args}")
            return None
        
class listacontactos:

    def GET(self):
        print(self.)
    



if __name__ == "__main__":
    app.run()