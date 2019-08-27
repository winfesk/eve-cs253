import webapp2

form="""
    <form action="/testform">
        <input name="q" /> <input type="submit" />
    </form>
"""


class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)

class TestHandler(webapp2.RequestHandler):
    def get(self):
        q = self.request.get("q")
        self.response.write(q)

app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
], debug=True)
