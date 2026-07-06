import web
import sqlite3

render = web.template.render('views', base='layout')

class BorrarContacto:
    
    def POST(self, id_contacto: int):
        exito = False
        try:
            conexion = sqlite3.connect("sql/agenda.db")
            cursor = conexion.cursor()
            query = "DELETE FROM contactos WHERE id_contacto = ?"
            cursor.execute(query, (id_contacto,))
            
            conexion.commit()
            conexion.close()
            exito = True
            
        except sqlite3.Error as error:
            print(f"ERROR 106: {error.args}")
            return "Error al intentar eliminar el contacto."
        except Exception as error:
            print(f"ERROR 107: {error.args}")
            return "Ocurrió un error inesperado al eliminar."
        if exito:
            raise web.seeother('/')