from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
import os

class Shout(db.Model):
    name = db.StringProperty(required=True)
    date = db.DateTimeProperty(auto_now_add=True)


class MainPage(webapp.RequestHandler):
    def get(self):
        shouts = db.GqlQuery('SELECT * FROM Shout ' 
                               'ORDER BY name')
        self.response.out.write(template.render('index.html', {'shouts': shouts}))
    def post(self):
        shout = Shout(name=self.request.get('name'))
        shout.put()
        self.redirect("/")
        

application = webapp.WSGIApplication(
                [('/', MainPage)],debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
