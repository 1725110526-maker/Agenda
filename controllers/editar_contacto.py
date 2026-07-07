import web
import sqlite3

render = web.template.render('views', base='layout')

class EditarContacto:
    
    def actualizarContacto(self, contacto:dict):
        try:
            conexion = sqlite3.connect("sql/agenda.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()

            id_contacto = contacto['id_contacto']
            nombre=contacto['nombre']
            primer_apellido=contacto['primer_apellido']
            segundo_apellido=contacto['segundo_apellido']
            email=contacto['email']
            telefono=contacto['telefono']

            query = """UPDATE contactos
                SET nombre = ?,
                primer_apellido = ?,
                segundo_apellido = ?,
                email = ?,
                telefono = ?
                WHERE id_contacto = ?
                """
            
            cursor.excute(query,(nombre,primer_apellido,segundo_apellido,email,telefono,id_contacto))
            conexion.commit()
            return True
        
        except sqlite3.Error as error:
            print(f"ERROR 104:¨{error.args}")
            return False
        except Exception as error:
            print(f"ERROR 105:{error.args}")
            return False
        
    def GET (self, id_contacto:int):
        print(f"ID_CONTACTO: {id_contacto}")
        contacto = self.actualizarContacto(id_contacto)
        return render.editar_contacto(contacto)

    def POST(self, id_contacto: int):
        formulario = web.input()
        contacto = {
            "id_contacto":formulario['id_contacto'],
            "nombre":formulario['nombre'],
            "primer_apellido":formulario['primer_apellido'],
            "segundo_apellido":formulario['segundo_apellido'],
            "email":formulario['email'],
            "telefono":formulario['telefono'],
        }
        return (contacto)

