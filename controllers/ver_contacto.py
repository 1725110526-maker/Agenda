import web
import sqlite3

render = web.template.render('views', base='layout')

class VerContacto:

    def buscarContactos(self, id_contacto: int):
        try:
            conexion = sqlite3.connect("sql/agenda.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            
            query = "SELECT * FROM contactos WHERE id_contacto = ?"
            cursor.execute(query, (id_contacto,))
            resultado = cursor.fetchone()

            conexion.close()
            if resultado:
                contacto = {
                    "id_contacto": resultado[0],
                    "nombre": resultado[1],
                    "primer_apellido": resultado[2],
                    "segundo_apellido": resultado[3],
                    "email": resultado[4],
                    "telefono": resultado[5]
                }
                print(contacto)
                return contacto
            
            return None
            
        except sqlite3.Error as error:
            print(f"ERROR 102: {error.args}")
            return None
        except Exception as error:
            print(f"ERROR 103: {error.args}")
            return None
    
    def GET(self, id_contacto: int):
        print(f"ID_CONTACTO: {id_contacto}")
        
        contacto = self.buscarContactos(id_contacto)
        
        if contacto is None:
            return "Error: Contacto no encontrado."
            
        return render.ver_contacto(contacto=contacto)