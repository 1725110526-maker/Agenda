import web
import sqlite3

render = web.template.render("views", base="layout")


class BorrarContacto:

    def eliminarContacto(self, contacto: dict) -> bool:
        try:
            conexion = sqlite3.connect("sql/agenda.sqlite")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()

            id_contacto = contacto["id_contacto"]
            query = """DELETE FROM contacto
                        WHERE id_contacto = ?
                """
            cursor.execute(query,(id_contacto,))
            conexion.commit()
            return True
        except sqlite3.Error as error:
            print(f"ERROR 104: {error.args}")
            return False
        except Exception as error:
            print(f"ERROR 105: {error.args}")
            return False

    def buscarContacto(self, id_contacto: int):
        try:
            conexion = sqlite3.connect("sql/agenda.sqlite")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM contacto WHERE id_contacto = ?"
            cursor.execute(query, (id_contacto,))
            resultado = cursor.fetchone()

            contacto = {
                "id_contacto": resultado[0],
                "nombre": resultado[1],
                "primer_apellido": resultado[2],
                "segundo_apellido": resultado[3],
                "email": resultado[4],
                "telefono": resultado[5],
            }
            conexion.close()
            print(contacto)
            return contacto
        except sqlite3.Error as error:
            print(f"ERROR 102: {error.args}")
            return []
        except Exception as error:
            print(f"ERROR 103: {error.args}")
            return []

    def GET(self, id_contacto: int):
        print(f"ID_CONTACTO: {id_contacto}")
        contacto = self.buscarContacto(id_contacto)
        return render.borrar_contacto(contacto)
    
    def POST(self,id_contacto: int):
        formulario = web.input()
        contacto = {
            "id_contacto":formulario['id_contacto'],
            "nombre":formulario['nombre'],
            "primer_apellido":formulario['primer_apellido'],
            "segundo_apellido":formulario['segundo_apellido'],
            "email":formulario['email'],
            "telefono":formulario['telefono']
        }
        resultado = self.eliminarContacto(contacto)
        web.ctx.status = '303 See Other'
        web.header('Location', '/lista_contactos')
        return ''
        #raise web.seeother('/lista_contactos')