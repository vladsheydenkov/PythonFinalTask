"""
This module provides templates for html converter
"""


from jinja2 import Template


feed = Template('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{title}}</title>
</head>
<body>
<h1>
    {{title}}
</h1>
    {% for item in news %}
    {{item}}
    {% endfor %}
</body>
</html>
''')

feed_item = Template('''
<div>
    <h2>{{title}}</h2>
    <div>
        <div>
            <h5>{{date}}</h5>
            <p>
            {% for content in content %}
                {{content}}
            {% endfor %}
            </p><br>
            <b>Link: </b><a href="{{link}}">{{link}}</a><br>
            <b>Links:</b><br>
            {% for link in links %}
                <a href="{{link}}">{{link}}</a><br>
            {% endfor %}
            <b>Images:</b><br>
            {% for img in img %}
                <img src={{img['src']}} alt={{img['alt']}}><br>
            {% endfor %}
            <br>
        </div>
    </div>
</div>
''')
