import web

urls = (
    '/', 'controllers.index.Index',
    '/lista_contacto','controllers.lista_contacto.ListaContactos',
    '/ver.contacto/(.*)','controllers.ver.contacto.VerContacto'
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()