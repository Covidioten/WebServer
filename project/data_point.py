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
        "SELECT point_date, total, sentiment FROM data_point ORDER BY created DESC").fetchall()
    data_points = [{'point_date': data_point[0], 'sentiment':data_point[1],
                    'total':data_point[2]} for data_point in data_points_as_rows]
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
    return parse_data_point_json_file("""{"root":[{"2020-01-04":{"total":"22","sentiment":"0.025","date":"2020-01-04","data":{"1213457533781848064":{"13:49:55":"0.0"},"1213457554757636097":{"13:50:00":"0.0"},"1213457588328767489":{"13:50:08":"0.0"},"1213457617672179712":{"13:50:15":"0.0"},"1213457638635245568":{"13:50:20":"0.0"},"1213457647023861760":{"13:50:22":"0.0"},"1213457680574173184":{"13:50:30":"0.0"},"1213457743497089026":{"13:50:45":"0.7"},"1213457777043087361":{"13:50:53":"0.0"},"1213457777047298049":{"13:50:53":"0.0"},"1213457789647020032":{"13:50:56":"0.0"},"1213457819002953729":{"13:51:03":"0.0"},"1213457831564840961":{"13:51:06":"0.0"},"1213457848363028480":{"13:51:10":"0.0"},"1213457877727432705":{"13:51:17":"0.0"},"1213457886094995456":{"13:51:19":"0.0"},"1213457928033914881":{"13:51:29":"0.2333333333333333"},"1213457932228145152":{"13:51:30":"0.0"},"1213457944806928384":{"13:51:33":"0.0"},"1213457995167916032":{"13:51:45":"0.0"},"1213458024528072706":{"13:51:52":"0.0"},"1213458129381462016":{"13:52:17":"0.025"}}}},{"2020-01-05":{"total":"22","sentiment":"0.025","date":"2020-01-05","data":{"1213457533781848064":{"13:49:55":"0.0"},"1213457554757636097":{"13:50:00":"0.0"},"1213457588328767489":{"13:50:08":"0.0"},"1213457617672179712":{"13:50:15":"0.0"},"1213457638635245568":{"13:50:20":"0.0"},"1213457647023861760":{"13:50:22":"0.0"},"1213457680574173184":{"13:50:30":"0.0"},"1213457743497089026":{"13:50:45":"0.7"},"1213457777043087361":{"13:50:53":"0.0"},"1213457777047298049":{"13:50:53":"0.0"},"1213457789647020032":{"13:50:56":"0.0"},"1213457819002953729":{"13:51:03":"0.0"},"1213457831564840961":{"13:51:06":"0.0"},"1213457848363028480":{"13:51:10":"0.0"},"1213457877727432705":{"13:51:17":"0.0"},"1213457886094995456":{"13:51:19":"0.0"},"1213457928033914881":{"13:51:29":"0.2333333333333333"},"1213457932228145152":{"13:51:30":"0.0"},"1213457944806928384":{"13:51:33":"0.0"},"1213457995167916032":{"13:51:45":"0.0"},"1213458024528072706":{"13:51:52":"0.0"},"1213458129381462016":{"13:52:17":"0.025"}}}}]}""")


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
