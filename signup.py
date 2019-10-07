import webapp2
import re

template = """
    <!DOCTYPE html>
    <html lang="en">
        <head>
          <meta charset="UTF-8">
          <title>Beautiful title</title>
          <style>
            label {
                text-align: right;
            }
            .grid {
                display: grid;
                grid-template-columns: 107px auto;
                grid-gap: 5px;
            }
          </style>
        </head>
        <body>
          <h1>Sign Up</h1>
          <form method="POST">
            <div class="grid">
                <label for="username">Username</label>
                <div>
                    <input
                        id="username"
                        type="text"
                        placeholder="username"
                        name="username"
                        value="%(username)s"
                    > %(username_error)s
                </div>


                <label for="password">Password</label>
                <div>
                    <input
                        id="password"
                        type="password"
                        placeholder="password"
                        name="password"
                    > %(password_error)s
                </div>

                <label for="verify">Verify password</label>
                <div>
                    <input
                        id="verify"
                        type="password"
                        placeholder="verify password"
                        name="verify"
                    > %(pass_verify_error)s
                </div>

                <label for="email">Email (optional)</label>
                <div>
                    <input
                        id="email"
                        type="text"
                        placeholder="you@mail.com"
                        name="email"
                        value="%(email)s"
                    > %(email_error)s
                </div>
            </div>
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

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

def valid_username(username):
    return USER_RE.match(username)

def valid_password(password):
    return PASSWORD_RE.match(password)

def valid_repeat_pass(password, repeated_pass):
    return repeated_pass == password

def valid_email(email):
    if email == "":
        return True
    return EMAIL_RE.match(email)


class Main(webapp2.RequestHandler):
    def get(self):
        self.response.write(template % {"username": "",
                                        "email": "",
                                        "username_error": "",
                                        "password_error": "",
                                        "pass_verify_error": "",
                                        "email_error": "" })

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        repeated_pass = self.request.get('verify')
        email = self.request.get('email')
        if valid_username(username) and valid_password(password) and valid_repeat_pass(password, repeated_pass) and valid_email(email):
            self.redirect("/signup/welcome?username=" + username)
        else:
            usernameError = "" if valid_username(username) else "<span style='color: red'>bad name</span>"
            passwordError = "" if valid_password(password) else "<span style='color: red'>bad password</span>"
            pverifyError = "" if valid_repeat_pass(password, repeated_pass) else "<span style='color: red'>bad repeated password</span>"
            emailError = "" if valid_email(email) else "<span style='color: red'>bad email</span>"
            # self.response.write("Here we go again, " + username)
            self.response.write(template % {"username": escape_html(username),
                                            "email": escape_html(email),
                                            "username_error": usernameError,
                                            "password_error": passwordError,
                                            "pass_verify_error": pverifyError,
                                            "email_error": emailError })

class Welcome(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        self.response.write("Welcome, " + username + "!")

route1 = ('/signup', Main)
route2 = ('/signup/welcome', Welcome)

# app = webapp2.WSGIApplication([
#     ('/', Main),
#     ('/welcome', Welcome)
# ], debug=True)
