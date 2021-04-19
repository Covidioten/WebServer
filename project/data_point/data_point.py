from project import db
from flask import url_for


class DataPoint(db.Model):
    __tablename__ = 'data_point'
    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Integer, nullable=False)
    sentiment = db.Column(db.Float, nullable=False)
    point_date = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, nullable=False,
                        server_default=db.func.current_timestamp())

    @property
    def update_url(self):
        return url_for("data_point.update", id=self.id)

    @property
    def delete_url(self):
        return url_for("data_point.delete", id=self.id)
