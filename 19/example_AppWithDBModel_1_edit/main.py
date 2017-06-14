#!/usr/bin/env python
import os
import jinja2
import webapp2
from models import Message

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
        messages = Message.query().fetch()
        params = {"messages": messages}
        return self.render_template("hello.html", params=params)

    def post(self):
        result_text = self.request.get("some_text")
        result_name = self.request.get("some_name")
        result_another_text = self.request.get("another_text")

        msg = Message(message_text=result_text,name=result_name,another_text=result_another_text)
        msg.put()

        messages = Message.query().fetch()
        params = {"messages": messages}
        return self.render_template("hello.html", params=params)


class MessageDetailsHandler(BaseHandler):
    def get(self, message_id):
        message = Message.get_by_id(int(message_id))
        params = {"message": message}
        return self.render_template("message_detail.html", params=params)


class EditMessageHandler(BaseHandler):
    def get(self, message_id):
        message = Message.get_by_id(int(message_id))
        params = {"message": message}
        return self.render_template("message_edit.html", params=params)

    def post(self, message_id):
        new_text = self.request.get("some_text")
        new_name = self.request.get("some_name")
        another_text =self.request.get("another_text")
        message = Message.get_by_id(int(message_id))
        message.message_text = new_text
        message.name = new_name
        message.another_text = another_text
        message.put()
        return self.redirect_to("msg-list")


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="msg-list"),
    webapp2.Route('/message/<message_id:\d+>', MessageDetailsHandler),
    webapp2.Route('/message/<message_id:\d+>/edit', EditMessageHandler),
], debug=True)