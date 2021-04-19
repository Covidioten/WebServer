import os

from flask import Blueprint
from flask import json
from flask import jsonify

from project.data_point.data_point import DataPoint


from flask import request

from project import db

bp = Blueprint("data_point", __name__)


@bp.route("/data-point", methods=["POST"])
def create_data_point():
    total = request.form["total"]
    sentiment = request.form["sentiment"]
    point_date = request.form["point_date"]

    error = None

    if not total:
        error = "Total is required."
    if not sentiment:
        error = "Sentiment is required."
    if not point_date:
        error = "Point Date is required"

    if error is not None:
        return error

    db.session.add(DataPoint(total=total, sentiment=float(sentiment),
                             point_date=point_date))
    db.session.commit()

    return jsonify(success=True)


@bp.route("/data-point", methods=["GET"])
def get_all_data_points():
    data_points = DataPoint.query.all()
    value = [{'x': data_point.point_date, 'y': data_point.sentiment}
             for data_point in data_points]
    return jsonify(value)


def get_data_point(id):
    data_point = DataPoint.query.get_or_404(
        id, f"DataPoint id {id} doesn't exist.")

    return data_point


@bp.route("/data-point/update/<int:id>", methods=["PUT"])
def update(id):
    data_point = get_data_point(id)

    total = request.form["total"]
    sentiment = request.form["sentiment"]
    point_date = request.form["point_date"]

    error = None

    if not total:
        error = "Total is required."

    if not sentiment:
        error = "Sentiment is required"

    if not point_date:
        error = "Point Date is required"

    if error is not None:
        return error

    data_point.total = total
    data_point.sentiment = sentiment
    data_point.point_date = point_date
    db.session.commit()

    return jsonify(success=True)


@bp.route("/data-point/delete/<int:id>", methods=("POST",))
def delete(id):
    data_point = get_data_point(id)
    db.session.delete(data_point)
    db.session.commit()

    return jsonify(success=True)


@ bp.route("/data-point/from-file", methods=["GET"])
def create_data_points_from_file():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/data", "test.json")
    return parse_data_point_json_file(json_url)


def parse_data_point_json_file(path):
    with open(path) as json_file:
        formatted_json = json.loads(json_file.read())
        for tree in formatted_json.items():
            for day in tree[1]:
                for entry in day.items():
                    if DataPoint.query.filter_by(point_date=entry[1]['date']).first() is None:
                        db.session.add(DataPoint(total=entry[1]['total'], sentiment=float(
                            entry[1]['sentiment']), point_date=entry[1]['date']))
                        db.session.commit()
    return "200"
