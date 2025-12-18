from jinja2 import Template


sub = "MAD2"

t = """
        {% if sub == 'MAD1' %}
            Mobile Application Development
        {% elif sub == 'DSA' %} 
            Data Structures and Algorithms
        {% else %}
            Some other subject
        {% endif %}
        
"""

template = Template(t)

print(template.render(sub=sub))

