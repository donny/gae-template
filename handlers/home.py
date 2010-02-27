from google.appengine.ext import webapp

import view

class HomeHandler(webapp.RequestHandler):

	def get(self):
		page = view.Page()
		page.render(self, 'templates/home/index.html', {})
