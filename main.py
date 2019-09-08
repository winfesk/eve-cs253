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
         <br>
         <input type="submit" />
    </form>
"""

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
    def get(self):
        self.response.write(form)

    def post(self):
        user_month = valid_month(self.request.get('month'))
        user_day = valid_day(self.request.get('day'))
        user_year = valid_year(self.request.get('year'))

        if not (user_month and user_day and user_year):
            self.response.out.write(form)
        else:
            self.response.write("Thanks! That's a totally valid day!")

app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
], debug=True)
