from jinja2 import Template

template_str ="""
{% set gifts = [
    {'name': 'Teddy Bear', 'price': 250, 'rating': 4.2},
    {'name': 'Coffee Mug', 'price': 150, 'rating': 4.5},
    {'name': 'Keychain', 'price': 100, 'rating': 3.9},
    {'name': 'Notebook', 'price': 180, 'rating': 4.7},
    {'name': 'Wall Clock', 'price': 300, 'rating': 4.0}
    ] %}

<ul>
{% for gift in gifts if gift.price < 200 and gift.rating > 4 %}
    <li>{{ gift.name }} - {{ gift.price }} - {{ gift.rating }}</li>
{% endfor %}
</ul>"""

template = Template(template_str)
rendered_str = template.render()
print(rendered_str)