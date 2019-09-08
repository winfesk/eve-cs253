import webapp2

form="""
    <form method="post">
         What is your birthday?
         <br>
         <label> Month
            <input type="text" placeholder="december" name="month">
         </label>
         <label> Day
            <input type="text" placeholder="19" name="day">
         </label>
         <label> Year
            <input type="text" placeholder="1999" name="year">
         </label>
         <div style="color: red">%(error)s</div>
         <br>
         <br>
         <input type="submit" />
    </form>
"""
months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

def valid_month(month):
    if len(month) < 1:
        return None
    month = lowerCases(month)
    if month in months:
        return month
    return None

def lowerCases(month):
    result = month[0].upper()
    i = 0
    for letter in month:
        if i != 0:
            result = result + letter.lower()
        i = 1
    return result

def valid_day(day):
    if day.isdigit():
        if int(day) >= 1 and int(day) <= 31:
            return int(day)
    return None

def valid_year(year):
    if year.isdigit():
        if int(year) >= 1900 and int(year) <= 2020:
            return int(year)
    return None


class HelloWebapp2(webapp2.RequestHandler):
    def write_form(self, error=""):
        self.response.write(form % {"error": error})

    def get(self):
        self.write_form()

    def post(self):
        user_month = valid_month(self.request.get('month'))
        user_day = valid_day(self.request.get('day'))
        user_year = valid_year(self.request.get('year'))

        if not (user_month and user_day and user_year):
            self.write_form("That doesn't look valid to me, friend.")
        else:
            self.response.write("Thanks! That's a totally valid day!")

app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
], debug=True)
