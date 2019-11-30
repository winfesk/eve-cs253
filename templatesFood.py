import webapp2
from jinja2 import Template

class MainPage(webapp2.RequestHandler):
    def get(self):
        foods = self.request.get("food", allow_multiple = True)
        name = self.request.get("name")
        self.response.write(Template(template).render(foods = foods, name = name))

template = """
{%if name %}
    <h1>List of {{name}}</h1>
{% else %}
    <h1>List</h1>
{% endif %}
<form>
    <input name="food">
    {% if foods %}
        {% for food in foods %}
            <li>{{food}}</li>
        {% endfor %}
    {% endif %}
    <button>click</button>
</form>
"""

app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
