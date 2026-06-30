import web

urls = (
    '/', 'controllers.index.Index',
    '/lista.contactos','controllers.lista_contactos.ListaContactos'
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()