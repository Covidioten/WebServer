from sqlite3.dbapi2 import connect
from flask import Blueprint
from flask import flash
from flask import g

from flask import request

from werkzeug.exceptions import abort

from project.db import get_db

import datetime

bp = Blueprint("news", __name__)


@bp.route("/news", methods=["POST"])
def create_news_entry():
    """Create a new data point."""
    title = request.form["title"]
    content = request.form["content"]
    if not title:
        error = "Title is required."
    if not content:
        error = "Content is required."

    if error is not None:
        flash(error)
    else:
        db = get_db()
        db.execute("INSERT INTO news (title, content) VALUES (?, ?)",
                   (title, content))
        db.commit()
        return db.cursor().fetchone()[0]


@bp.route("/news", methods=["GET"])
def get_all_news():
    """Get all data points"""
    db = get_db()
    data_points = db.execute(
        "SELECT id, title, content, created, creator_id FROM news ORDER BY created DESC").fetchall()
    return data_points


@bp.route("/news/range/<string:from>/<string:to>", methods=["GET"])
def get_news_in_range(date_from: datetime, date_to: datetime):
    """Get all data points"""
    db = get_db()
    data_points = db.execute(
        "SELECT id, title, content, created, creator_id FROM data_point WHERE created BETWEEN CONVERT(datetime, %s) AND CONVERT(datetime, %s) ORDER BY created DESC", (date_from, date_to)).fetchall()
    return data_points
