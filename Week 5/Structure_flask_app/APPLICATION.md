# 📦 Application Documentation

Auto-generated application overview.

## 📁 Project Structure

├── Structure_flask_app/
│   ├── app.py
│   ├── reoprt.py
│   ├── requirments.txt
│   ├── application/
│   │   ├── config.py
│   │   ├── controllers.py
│   │   ├── db.py
│   │   ├── models.py
│   │   ├── __init__.py
│   ├── instance/
│   │   ├── mydb.db
│   ├── static/
│   ├── templates/
│   │   ├── add_post.html
│   │   ├── index.html

---

## 📄 File Contents

### `app.py`

```python
from application import create_app

app = create_app()


if __name__ == "__main__":
    app.run(debug=True)

```

### `reoprt.py`

```python
import os

OUTPUT_FILE = "APPLICATION.md"

# folders to ignore
IGNORE_DIRS = {
    ".env", "__pycache__", ".git", ".vscode",
    "node_modules", ".idea"
}

# files to ignore
IGNORE_FILES = {
    OUTPUT_FILE
}

def get_language_hint(filename):
    ext = os.path.splitext(filename)[1]
    return {
        ".py": "python",
        ".html": "html",
        ".css": "css",
        ".js": "javascript",
        ".json": "json",
        ".md": "markdown",
        ".txt": "text",
        ".sql": "sql",
        ".yml": "yaml",
        ".yaml": "yaml"
    }.get(ext, "")

def write_tree(root, md):
    md.write("## 📁 Project Structure\n\n")
    for root_dir, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        level = root_dir.replace(root, "").count(os.sep)
        indent = "│   " * level
        md.write(f"{indent}├── {os.path.basename(root_dir)}/\n")
        for file in files:
            if file not in IGNORE_FILES:
                md.write(f"{indent}│   ├── {file}\n")
    md.write("\n---\n\n")

def write_files(root, md):
    md.write("## 📄 File Contents\n\n")
    for root_dir, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for file in files:
            if file in IGNORE_FILES:
                continue

            path = os.path.join(root_dir, file)
            rel_path = os.path.relpath(path, root)

            md.write(f"### `{rel_path}`\n\n")

            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception as e:
                content = f"⚠️ Could not read file: {e}"

            lang = get_language_hint(file)
            md.write(f"```{lang}\n{content}\n```\n\n")

def main():
    root = os.getcwd()
    with open(OUTPUT_FILE, "w", encoding="utf-8") as md:
        md.write("# 📦 Application Documentation\n\n")
        md.write("Auto-generated application overview.\n\n")
        write_tree(root, md)
        write_files(root, md)

    print(f"✅ {OUTPUT_FILE} generated successfully.")

if __name__ == "__main__":
    main()

```

### `requirments.txt`

```text
flask
flask_sqlalchemy
```

### `application\config.py`

```python


class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///mydb.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

```

### `application\controllers.py`

```python
from flask import render_template, request, redirect, url_for
from .database import db
from .models import Post

post_bp = Blueprint("post_bp", __name__)

@app.route("/")
def home():
    return "Hello Flask"



@post_bp.route("/")
def index():
    posts = Post.query.all()
    return render_template("index.html", posts=posts)

@post_bp.route("/add", methods=["GET", "POST"])
def add_post():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")

        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for("post_bp.index"))

    return render_template("add_post.html")
```

### `application\db.py`

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

```

### `application\models.py`

```python
from .db import db

class Post(db.Model):
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Post {self.title}>"

```

### `application\__init__.py`

```python
from flask import Flask
from .db import db

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"

    db.init_app(app)

    from . import models
    from .controllers import post_bp

    app.register_blueprint(post_bp)

    with app.app_context():
        db.create_all()

    return app

```

### `instance\mydb.db`

```
⚠️ Could not read file: 'utf-8' codec can't decode byte 0x8b in position 99: invalid start byte
```

### `templates\add_post.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    <h1>Add a New Post</h1>
    <form action="/add_post" method="post">
        <label for="title">Title:</label><br>
        <input type="text" id="title" name="title" required><br><br>
        <label for="content">Content:</label><br>
        <textarea id="content" name="content" rows="4" cols="50" required></textarea><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

### `templates\index.html`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <h1>Hello world</h1>
    {% for post in posts %} 
    <div >
      <h2>{{post.title}}</h2>
      <p>{{post.content}}</p>
    </div>
    {% endfor %}
  </body>
</html>

```

