import web

urls = (
    '/', 'controllers.index.Index',
    '/lista_contacto','controllers.lista_contacto.ListaContacto',
    '/ver.contacto','controllers.ver.contacto.VerContacto',
    '/modificar_contacto','controllers.modificar_contacto.ModificarContacto',

)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
