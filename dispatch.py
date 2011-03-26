# Device Infomation registration pages.
# -*- coding: utf-8 -*-

import os
from models import DeviceInfo
from models import UserInfo

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

import twitter
import mono
import finder

class TopPage(webapp.RequestHandler):
    def get(self):

        user = users.get_current_user()

        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            "user" : user,
            "url" : url,
            "url_linktext" : url_linktext
            }
        path = os.path.join(os.path.dirname(__file__), 'template/index.html')
        self.response.out.write(template.render(path, template_values))


application = webapp.WSGIApplication([
#        ('/twitter', twitter.RegistTwitter),
#        ('/list', mono.ListDevice),
#        ('/regist', mono.RegistDevice),
#        ('/show', mono.ShowDevice),
#        ('/edit', mono.EditDevice),
#        ('/delete', mono.DeleteDevice),
#       ('/finder', finder.FindDevice),
#        ('/notify', finder.NotifyOwner),
#        ('/thanks', finder.Thanks),
        ('/', TopPage),
        ], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
