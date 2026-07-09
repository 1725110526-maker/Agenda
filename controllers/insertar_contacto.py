import web
import sqlite3

render = web.template.render("views", base="layout")

class InsertarContacto:

    def inserteContacto(self, contacto: dict):
        conexion = None
        try:
            conexion = sqlite3.connect("sql/agenda.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()

            nombre = contacto["nombre"]
            primer_apellido = contacto["primer_apellido"]
            segundo_apellido = contacto["segundo_apellido"]
            email = contacto["email"]
            telefono = contacto["telefono"]
            
            query = """
                INSERT INTO contactos
                (nombre, primer_apellido, segundo_apellido, email, telefono)
                VALUES (?, ?, ?, ?, ?)
            """

        
            datos = (
                nombre,
                primer_apellido,
                segundo_apellido,
                email,
                telefono
            )
            
            cursor.execute(query, datos)
            conexion.commit()
            return True
        except sqlite3.Error as error:
            print(f"ERROR 104: {error.args}")
            return False
        finally:
            if conexion:
                conexion.close()

    def GET(self):
        return render.inserte_contacto()
    
    def POST(self):
        formulario = web.input()
        
        contacto = {
            "nombre": formulario['nombre'],
            "primer_apellido": formulario['primer_apellido'],
            "segundo_apellido": formulario['segundo_apellido'],
            "email": formulario['email'],
            "telefono": formulario['telefono']
        }
        
        resultado = self.inserteContacto(contacto)
        web.ctx.status
        
        if resultado:
            raise web.seeother('/lista_contactos')
        else:
            return resultado
        


