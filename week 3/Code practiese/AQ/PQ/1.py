'''
What is Jinja2?

Jinja2 is a templating engine for Python.

It lets you combine data (variables, objects) with a template (HTML, text, etc.) to generate a final output.

Mostly used in Flask/Django web apps to render dynamic HTML pages.

'''

from jinja2 import Template


#step 1 - variables  : These are the Python variables you want to pass into the template.
name = "anish"
palce = "IITM"
profession = "student"

#step 2 - template : This is your template string.

# {{ variable_name }} is Jinja2 syntax for inserting values.
# Inside {{ ... }} → Jinja2 replaces with the actual variable passed later.


temp = "My name is {{ name }}. I study in {{ place }}. I am a {{ profession }}."

#step 3 - create template object : 
# Creates a Template object from your string.
# Now Jinja2 knows where to substitute variables.

made_template = Template(temp)

#step 4 - render the template
output = made_template.render(name=name, place=palce, profession=profession)

print(output)