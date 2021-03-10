from flask import Blueprint
from flask import flash
from flask import g

from flask import request

from werkzeug.exceptions import abort

from project.auth import login_required
from project.db import get_db

import datetime

bp = Blueprint("data_point", __name__)


@bp.route("/data-point", methods=("POST"))
@login_required
def create_data_point():
    """Create a new data point."""
    total = request.form["total"]
    sentiment = request.form["sentiment"]
    point_date = request.form["date"]
    if not total:
        error = "Total is required."
    if not sentiment:
        error = "Sentiment is required."
    if not point_date:
        error = "Point Date is required"
    if error is not None:
        flash(error)
    else:
        db = get_db()
        db.execute("INSERT INTO data_point (total, sentiment, point_date, creator_id) VALUES (?, ?, ?, ?)",
                   (total, sentiment, point_date, g.user["id"]))
        db.commit()
        return db.cursor().fetchone()[0]


@bp.route("/data-point", methods=("GET"))
def get_all_data_points():
    """Get all data points"""
    db = get_db()
    data_points = db.execute(
        "SELECT id, total, sentiment, point_date, created, creator_id FROM data_point ORDER BY created DESC").fetchall()
    return data_points


@bp.route("/data-point/range/<datetime:from>/<datetime:to>", methods=("GET"))
def get_data_points_in_range(from: datetime, to: datetime):
    """Get all data points"""
    db = get_db()
    data_points = db.execute(
        "SELECT id, total, sentiment, point_date, created, creator_id FROM data_point WHERE created BETWEEN CONVERT(datetime, %s) AND CONVERT(datetime, %s) ORDER BY created DESC", (from, to)).fetchall()
    return data_points


@bp.route("/data-point/from-file", methods=("GET"))
def create_data_points_from_file():
    """Create a new data point from file"""


def parse_data_point_json_file():
    """Parse a data point json file"""
