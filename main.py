import webapp2

form="""
    <form action="http://www.google.com/search">
        <input name="q" /> <input type="submit" />
    </form>
"""


class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)

app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
], debug=True)
