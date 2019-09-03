import webapp2

form="""
    <form method="post">
         What is your birthday?
         <br>
         <label> Month
            <input type="text" name="month">
         </label>
         <label> Day
            <input type="text" name="day">
         </label>
         <label> Year
            <input type="text" name="year">
         </label>
        <input name="q" /> <input type="submit" />
    </form>
"""


class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)

app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
], debug=True)
