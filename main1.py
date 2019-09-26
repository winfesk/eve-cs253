import webapp2

class Main(webapp2.RequestHandler):
    def get(self):
        self.response.write("Slava!!!!!!!\n")


app = webapp2.WSGIApplication([
    ('/', Main)
], debug=True)
