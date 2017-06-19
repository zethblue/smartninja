#!/usr/bin/env python
import os
import jinja2
import webapp2
import datetime
import random

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
        return self.render_template("hello.html")

class FakebookHandler(BaseHandler):
    def get(self):
        return self.render_template("fakebook.html")

class LotteryHandler(BaseHandler):
    def get(self):

        lottery = sorted(random.sample(range(1, 50), 8))
        params = {"lottery": lottery}
        return self.render_template("lottery.html", params=params)

class CurrentTimeHandler(BaseHandler):
    def get(self):
        time = datetime.datetime.now()

        params = {"time": time}

        return self.render_template("time.html", params=params)

class GuessNumberHandler(BaseHandler):
    def get(self):
        return self.render_template("guess.html")

class CalculatorHandler(BaseHandler):
    def get(self):
        return self.render_template("calc.html")
    def post(self):

        a = self.request.get("var1")
        b = self.request.get("var2")
        c = self.request.get("var3")

        if c == "A":
            sol = float(a) + float(b)
        elif c == "B":
            sol = float(a) * float(b)
        else:
            sol = "Please enter correct Data"
        solution = {"solution": sol}
        return self.render_template("calc.html", params=solution)

        #todo LengthUnitConvertHandler

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/fakebook', FakebookHandler),
    webapp2.Route('/lottery', LotteryHandler),
    webapp2.Route('/time', CurrentTimeHandler),
    webapp2.Route('/guess', GuessNumberHandler),
    webapp2.Route('/calc', CalculatorHandler)
], debug=True)


