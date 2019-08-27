import webapp2

class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
        self.response.write('Plese wait for a while...we are just goating this site')

app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
], debug=True)
