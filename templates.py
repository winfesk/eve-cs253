import webapp2

form_html = """
    <!DOCTYPE html>
        <html lang="en">
          <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <meta http-equiv="X-UA-Compatible" content="ie=edge" />
            <title>FOOD</title>
          </head>
          <body>
            <form>
              <h2>Add a food</h2>
              <input type="text" name="food" />
              <input type="hidden" name="food" value="eggs" /> <button>Add</button>
            </form>
          </body>
        </html>
"""

hidden_html = """
    <input type="hidden" name="food" value="%s">
"""
shopping_list_html = """
    <br><br>
    <h2>Shopping List</h2>
    <ul>
    %s
    </ul>
"""

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.write(*a, **kw)

class MainPage(Handler):
    def ger(self):
        self.write(form_html)

app = webapp2.WSGIApplication([('/', MainPage),
                            ],
                             debug = True)

route = ('/food', MainPage)
