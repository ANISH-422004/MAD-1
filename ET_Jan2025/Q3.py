from jinja2 import Template


newlist = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']


this_template = """
    {%- for item in data -%} // FOR LOOP iterating over newlist
        {% if item|length<6 %}
            {{ item }} 
        {%- endif -%}
    {%- endfor -%}
"""
out = Template(this_template)


print(out.render(data=newlist))

"""Clear label

"Search for a word" explains the purpose of the input field.

Helpful placeholder

"Type a word to search" reinforces what kind of input is expected.

Additional explanation via aria-describedby

Screen readers announce:
“Enter a word to find relevant results.”

This makes the instruction clearer, especially for assistive technology users.

Meaningful button text

"Start Search" clearly indicates the action.

Because the instructions, purpose, and expected input are easy to understand for all users, this example demonstrates the Understandable accessibility principle.

Why not the other options?

❌ Perceivable → focuses on making content visible/audible (contrast, alt text, captions).

❌ Operable → focuses on keyboard access, focus order, clickable controls.

❌ Robust → focuses on compatibility with assistive technologies and future browsers."""