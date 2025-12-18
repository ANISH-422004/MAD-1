from jinja2 import Template

subjects  =  [
    "MAD1", "DSA", "CN", "OS", "DBMS"
]

t = """
    {% for sub in subjects -%}
        {% if "A" in sub -%}
            <h1>{{ sub }}</h1>
        {% else -%}
            <p>{{ sub }}</p>
        {% endif -%}
    {% endfor %}
    
"""

temp = Template(t)
op = temp.render(subjects=subjects)
print(op)
