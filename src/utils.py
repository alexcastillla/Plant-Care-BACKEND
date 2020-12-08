from flask import jsonify, url_for, request
from functools import wraps
import jwt


class APIException(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

def generate_sitemap(app):
    links = ['/admin/']
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            if "/admin/" not in url:
                links.append(url)

    links_html = "".join(["<li><a href='" + y + "'>" + y + "</a></li>" for y in links])
    return """
        <div style="text-align: center;">
        <img style="max-height: 120px" src='https://i.ibb.co/pJV64n2/Frame-1.png' />
        <h1>Welcomes to your API also connected with Raspberry Pi4!</h1>
        <p>API HOST: <script>document.write('<input style="padding: 5px; width: 300px" type="text" value="'+window.location.href+'" />');</script></p>
        <p>This API is ready to use for <a href="https://github.com/alexcastillla/Plant-Care-FP-RaspberryPi4-4Geeks-BACKEND/blob/main/README.md" target="_blank">Plant Care</a></p>
        <p>A final project for 4Geeks Academy Madrid elaborated by Alexander & Aurelian</p>
        <p>and with all support from Jimena & Juan ❤</p>
        <p>Remember to specify an endpoint: </p>
        <ul style="text-align: left;">"""+links_html+"</ul></div>"


