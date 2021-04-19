from flask.json import jsonify
from project.news.news import News
from flask import Blueprint

from flask import request

from project import db


bp = Blueprint("news", __name__)


def get_news(id):
    news = News.query.get_or_404(
        id, f"News id {id} doesn't exist.")

    return news


@bp.route("/news", methods=["POST"])
def create_news_entry():
    title = request.form["title"]
    content = request.form["content"]
    statement_date = request.form["statement_date"]

    error = None

    if not title:
        error = "Title is required."

    if not content:
        error = "Content is required."

    if not statement_date:
        error = "Statement Date is required."

    if error is not None:
        return error

    db.session.add(News(title=title, content=content,
                        statement_date=statement_date))
    db.session.commit()
    return jsonify(success=True)


@bp.route("/news", methods=["GET"])
def get_all_news():
    all_news = News.query.all()
    value = [{'title': news.title, 'content': news.content, 'statement_date': news.statement_date}
             for news in all_news]
    return jsonify(value)


@bp.route("/news/update/<int:id>", methods=["PUT"])
def update(id):
    news = get_news(id)

    title = request.form["title"]
    content = request.form["content"]
    statement_date = request.form["statement_date"]

    error = None

    if not title:
        error = "Title is required."

    if not content:
        error = "Content is required."

    if not statement_date:
        error = "Statement Date is required."

    if error is not None:
        return error

    news.title = title
    news.content = content
    news.statement_date = statement_date
    db.session.commit()

    return jsonify(success=True)


@bp.route("/news/delete/<int:id>", methods=("POST",))
def delete(id):
    news = get_news(id)
    db.session.delete(news)
    db.session.commit()

    return jsonify(success=True)
