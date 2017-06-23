#!/usr/bin/env python
import os
import jinja2
import webapp2
import json
from google.appengine.api import urlfetch

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


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
        data = open("./storage/people.json", "r").read()
        json_data = json.loads(data)

        params = {"people_list": json_data}

        self.render_template("hello.html", params)


class WeatherHandler(BaseHandler):
    def get(self):
        API_KEY = "cbec83a956006eaa27214ce58f138fc1"
        CITY = "London,uk"
        UNITS = "metric"
        baseurl = "http://api.openweathermap.org/data/2.5/weather"
        queryurl = "?q={city}&units={units}&appid={appid}".format(city=CITY,units = UNITS,appid=API_KEY)
        url = baseurl+queryurl

        result = urlfetch.fetch(url)

        weather_info = json.loads(result.content)

        params = {"weather_info": weather_info}

        self.render_template("weather.html", params)

class CityWeatherHandler(BaseHandler):
    def get(self, city):
        API_KEY = "cbec83a956006eaa27214ce58f138fc1"
        CITY = city
        UNITS = "metric"
        baseurl = "http://api.openweathermap.org/data/2.5/weather"
        queryurl = "?q={city}&units={units}&appid={appid}".format(city=CITY,units = UNITS,appid=API_KEY)
        url = baseurl+queryurl

        result = urlfetch.fetch(url)

        weather_info = json.loads(result.content)

        params = {"weather_info": weather_info}

        self.render_template("weather.html", params)


class CityLuckyWeatherHandler(BaseHandler):
    def get(self, city,time,luck):
        API_KEY = "cbec83a956006eaa27214ce58f138fc1"
        CITY = city
        UNITS = "metric"
        baseurl = "http://api.openweathermap.org/data/2.5/weather"
        queryurl = "?q={city}&units={units}&appid={appid}".format(city=CITY,units = UNITS,appid=API_KEY)
        url = baseurl+queryurl

        result = urlfetch.fetch(url)

        weather_info = json.loads(result.content)

        weather_info["name"] = time
        weather_info["main"]["temp"] = luck
        params = {"weather_info": weather_info}

        self.render_template("weather.html", params)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/weather', WeatherHandler),
    webapp2.Route('/weather/<city:([^/]+)?>', CityWeatherHandler),
    webapp2.Route('/weather/<city:([^/]+)?>/<time:([^/]+)?>/<luck:([^/]+)?>', CityLuckyWeatherHandler),

    # [([^/]+)?] matches everything that is not
], debug=True)