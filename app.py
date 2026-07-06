import web

urls = (
    '/', 'controllers.index.Index',
    '/lista_contactos','controllers.lista_contacto.ListaContactos',
    '/ver.contacto/(.*)','controllers.ver.contacto.VerContacto',
    '/modificar_contacto/(.*)','controllers.modificar_contacto.ModificarContacto',

)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
