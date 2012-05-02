import webapp2

import rest_api
import file_manager

app = webapp2.WSGIApplication([('/api.*', rest_api.Rest), ('/prepare_upload', file_manager.Prepare), ('/file_upload', file_manager.Upload), ('/file_download/([^/]+)', file_manager.Download)], debug=True)