import jinja2

template = """
<ol>
{% for x in range(1, n + 1) %}
    {% if x % 3 == 0 and x % 5 == 0 %}
        <li>FizzBuzz</li>
    {% elif x % 3 == 0 %}
        <li>Fizz</li>
    {% elif x % 5 == 0  %}
        <li>Buzz</li>
    {% else %}
        <li>{{x}}</li>
    {% endif %}
{% endfor %}
</ol>
"""

# compiled = jinja2.Template(template)
# formatted = compiled.render(n=10)
#
# print formatted

print jinja2.Template(template).render(n=10)
