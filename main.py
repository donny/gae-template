import config
import os
import sys

# Force sys.path to have our own directory first, so we can import from it.
sys.path.insert(0, config.APP_ROOT_DIR)
sys.path.insert(1, os.path.join(config.APP_ROOT_DIR, 'externals'))

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from handlers import error, home

def main():
	application = webapp.WSGIApplication([
											('/', home.HomeHandler),
											# If we make it this far then the page
											# we are looking for does not exist.
											('/.*', error.Error404Handler),
											], debug=True)
	run_wsgi_app(application)

if __name__ == '__main__':
	main()