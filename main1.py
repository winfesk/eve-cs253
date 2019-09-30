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

class Main(webapp2.RequestHandler):
    def get(self):
        self.response.write(template % { "textarea": "" })

    def post(self):
        # writeToFile('database.txt', "13:38: Slava: I'm a pro, too :(")
        self.response.write(template % { "textarea": rot13(self.request.get("text")) })
        # newHtml = """<!DOCTYPE html>
        # <html lang="en">
        #     <head>
        #       <meta charset="UTF-8">
        #       <title>Beautiful title</title>
        #     </head>
        #     <body>
        #
        #     </body>
        # </html>
        # """
        # self.response.write(newHtml)


app = webapp2.WSGIApplication([
    ('/', Main)
], debug=True)
