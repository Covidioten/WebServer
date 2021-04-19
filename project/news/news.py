from project import db
from flask import url_for


class News(db.Model):
    __tablename__ = "news"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    statement_date = db.Column(db.String, nullable=False)
    created = db.Column(
        db.DateTime, nullable=False, server_default=db.func.current_timestamp()
    )

    @property
    def update_url(self):
        return url_for("news.update", id=self.id)

    @property
    def delete_url(self):
        return url_for("news.delete", id=self.id)
