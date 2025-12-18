from flask import Blueprint ,render_template, request, redirect, url_for
from .db import db
from .models import Post

post_bp = Blueprint("post_bp", __name__)


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