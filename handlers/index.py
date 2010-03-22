from google.appengine.ext import webapp

import view

class IndexHandler(webapp.RequestHandler):

	def get(self):
		page = view.Page()
		page.render(self, 'templates/page/index.html', {})
