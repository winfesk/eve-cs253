import webapp2

template = """<!DOCTYPE html>
<html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Beautiful title</title>
    </head>
    <body>
      <form method="POST">
        <textarea name="text">%(textarea)s</textarea>
        <button>Submit</button>
      </form>
    </body>
</html>
"""

def escape_html(s):
    for (i, o) in (("&", "&amp;"),
                    (">", "&gt;"),
                    ("<", "&lt;"),
                    ('"', "&quot;")):
        s = s.replace(i, o)
    return s

def rot13(str):
    new_str = ""
    for element in str:
        if ord(element) >= 65 and ord(element) <= 90:
            if ord(element) + 13 > 90:
                element = chr(65 - (91 - (ord(element) + 13)))
            else:
                element = chr(ord(element) + 13)
        else:
            if ord(element) >= 97 and ord(element) <= 122:
                if ord(element) + 13 > 122:
                    element = chr(97 - (123 - (ord(element) + 13)))
                else:
                    element = chr(ord(element) + 13)
        new_str = new_str + element
    return new_str

class Rot13(webapp2.RequestHandler):
    def get(self):
        self.response.write(template % { "textarea": "" })

    def post(self):
        # writeToFile('database.txt', "13:38: Slava: I'm a pro, too :(")
        self.response.write(template % { "textarea": escape_html(rot13(self.request.get("text"))) })

route = ('/rot13', Rot13)
# app = webapp2.WSGIApplication([
#     ('/', Main)
# ], debug=True)
