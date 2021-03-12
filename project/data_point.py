import os

from flask import Blueprint
from flask import flash
from flask import g
from flask import json
from flask import jsonify

from flask import request

from werkzeug.exceptions import abort

from project.db import get_db

import datetime

bp = Blueprint("data_point", __name__)


@bp.route("/data-point", methods=["POST"])
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
        db.execute("INSERT INTO data_point (total, sentiment, point_date) VALUES (?, ?, ?)",
                   (total, sentiment, point_date))
        db.commit()
        return db.cursor().fetchone()[0]


@bp.route("/data-point", methods=["GET"])
def get_all_data_points():
    """Get all data points"""
    db = get_db()
    data_points_as_rows = db.execute(
        "SELECT point_date, sentiment FROM data_point ORDER BY point_date ASC").fetchall()
    data_points = [{'x': data_point[0], 'y':data_point[1]}
                   for data_point in data_points_as_rows]
    return jsonify(data_points)


@bp.route("/data-point/range/<string:date_from>/<string:date_to>", methods=["GET"])
def get_data_points_in_range(date_from: datetime, date_to: datetime):
    """Get all data points"""
    db = get_db()
    data_points = db.execute(
        "SELECT id, total, sentiment, point_date, created FROM data_point WHERE created BETWEEN CONVERT(datetime, %s) AND CONVERT(datetime, %s) ORDER BY created DESC", (date_from, date_to)).fetchall()
    return data_points


@bp.route("/data-point/from-file", methods=["GET"])
def create_data_points_from_file():
    """Create a new data point from file"""
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/data", "test.json")
    return parse_data_point_json_file(open(json_url))


def parse_data_point_json_file(raw_json: json):
    """Parse a data point json file"""
    db = get_db()
    formatted_json = json.loads(raw_json)
    for tree in formatted_json.items():
        for day in tree[1]:
            for entry in day.items():
                db.execute("INSERT INTO data_point (total, sentiment, point_date) VALUES (?, ?, ?)",
                           (entry[1]['total'], entry[1]['sentiment'], entry[1]['date']))
                db.commit()
    return "200"
