#!/usr/bin/env python
import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates") #template_dir: In welchem Ordner ist mein Template. Fuer OS schau demo.py
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False) #aus welchem Ordner hole ich mir die templates/Formulare von der Webseite


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None): #parameter sind platzhalter
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params)) #Render schaut ob es Platzhalter gibt in der html datei. Gibt es welche ersetzt er diese mit den definierten Parametern



class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
