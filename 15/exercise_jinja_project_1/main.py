#!/usr/bin/env python
import os
import jinja2
import webapp2

import random

template_dir = os.path.join(os.path.dirname(__file__), "templates")
template_project_dir = os.path.join(template_dir, "projects")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader([template_dir, template_project_dir]), autoescape=False)

Visitor = "Z"

class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")


#  Exercise 1: write a Handler, and an HTML page which links to a new page random.html

class Randomhandler(BaseHandler):
    def get(self):
        return self.render_template("random.html")

#  Exercise 2: each time this page is opened, pass a random number which should be displayed on the page

class Rand2Handler(BaseHandler):
    def get(self):
        num = random.randint(1,50)
        p88x = {"numbers": num}
        return self.render_template("random2.html", params=p88x)

class VisitHandler(BaseHandler):
        def get(self):
            global Visitor
            if Visitor is not int:
                Visitor = 0
            else:
                Visitor += 1
            p99x = {"Visitor": Visitor}
            return self.render_template("VisitorCounter.html", params=p99x)


#  Exercise 3: create a folder in template, call it 'projects'.


#Exercise4 : Make a Visit Counter


#  Now integrate a page within the projects folder into your website


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/random', Randomhandler),
    webapp2.Route('/random2', Rand2Handler),
    webapp2.Route('/visit', VisitHandler),
], debug=True)
