import web

render = web.template.render('views', base='layout')

class Contactos:
    def GET(self):
        return render.contactos()