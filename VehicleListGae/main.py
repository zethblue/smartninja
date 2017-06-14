#!/usr/bin/env python
import os
import jinja2
import webapp2
import models

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        vehicles = models.Vehicles.query().fetch()
        params = {"vehicles":vehicles}
        return self.render_template("hello.html", params=params)
    def post(self):
        brand = self.request.get("brand")
        model = self.request.get("model")
        price = self.request.get("price")
        vehicle = models.Vehicles(brand=brand,
                                  model=model,
                                  price=price,
                                  ps="100")
        vehicle.put()
        vehicles = models.Vehicles.query().fetch()
        params = {"vehicles":vehicles}
        return self.render_template("hello.html", params=params)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
