from datetime import datetime

import pytest

from project import create_app
from project import db
from project import init_db
from project.data_point.data_point import DataPoint
from project.news.news import News


@pytest.fixture
def app():
    app = create_app(
        {"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"})

    with app.app_context():
        init_db()

        db.session.add_all(
            (
                News(
                    title="News Title 1",
                    content="News Content 1",
                    statement_date="01.01.2020",
                    created=datetime(2021, 3, 12)
                ), News(
                    title="News Title 2",
                    content="News Content 2",
                    statement_date="01.02.2020",
                    created=datetime(2021, 3, 12)
                ),
                DataPoint(
                    total=21, sentiment=1.4, point_date="01.01.2020", created=datetime(2020, 1, 1)),
                DataPoint(
                    total=42, sentiment=0.5, point_date="01.02.2020", created=datetime(2020, 2, 1))

            )
        )
        db.session.commit()

    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
