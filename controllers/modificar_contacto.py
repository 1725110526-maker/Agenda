import web
import sqlite3

render = web.template.render('views', base='layout')

class ModificarContacto:

    def buscarContacto(self, id_contacto: int):
        try:
            conexion = sqlite3.connect("sql/agenda.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            
            query = "SELECT * FROM contactos WHERE id_contacto = ?"
            cursor.execute(query, (id_contacto,))
            resultado = cursor.fetchone()
            conexion.close()
            
            if resultado:
                return dict(resultado)
            return None
            
        except sqlite3.Error as error:
            print(f"ERROR 102: {error.args}")
            return None
        except Exception as error:
            print(f"ERROR 103: {error.args}")
            return None

    def GET(self, id_contacto: int):
        contacto = self.buscarContacto(id_contacto)
        
        if contacto is None:
            return "Error: El contacto no existe."
            
        return render.modificar(contacto)

    def POST(self, id_contacto: int):
        datos_formulario = web.input()
        
        nombre = datos_formulario.get('nombre')
        primer_apellido = datos_formulario.get('primer_apellido')
        segundo_apellido = datos_formulario.get('segundo_apellido')
        email = datos_formulario.get('email')
        telefono = datos_formulario.get('telefono')

        try:
            conexion = sqlite3.connect("sql/agenda.db")
            cursor = conexion.cursor()
            
            query = """
                UPDATE contactos 
                SET nombre = ?, primer_apellido = ?, segundo_apellido = ?, email = ?, telefono = ? 
                WHERE id_contacto = ?
            """
            cursor.execute(query, (nombre, primer_apellido, segundo_apellido, email, telefono, id_contacto))
            conexion.commit()
            conexion.close()
            
            raise web.seeother('/') 
            
        except sqlite3.Error as error:
            print(f"ERROR 104: {error.args}")
            return "Error al intentar actualizar el contacto en la base de datos."
        except Exception as error:
            print(f"ERROR 105: {error.args}")
            return "Ocurrió un error inesperado al procesar la actualización."
