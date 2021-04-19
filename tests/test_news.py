import datetime
from project.news.news import News


def test_create(client, app):
    with app.app_context():
        assert News.query.count() == 2

    assert client.get("/news").status_code == 200
    response = client.post("/news", data={"title": "Title", "content": "Content",
                                          "statement_date": "01.05.2020"})
    print(response.data)

    with app.app_context():
        assert News.query.count() == 3


def test_update(client, app):
    with app.app_context():
        assert News.query.get(1).title == "News Title 1"
        assert News.query.get(1).content == "News Content 1"
        assert News.query.get(1).statement_date == "01.01.2020"

    response = client.put("news/update/1", data={
        "title": "New Title 25", "content": "New content 25", "statement_date": "01.04.2020"})

    with app.app_context():
        assert response.status_code == 200
        assert News.query.get(1).title == "New Title 25"
        assert News.query.get(1).content == "New content 25"
        assert News.query.get(1).statement_date == "01.04.2020"


def test_delete(client, app):
    response = client.post("/news/delete/1")

    with app.app_context():
        assert response.status_code == 200
        assert News.query.get(1) is None


def test_delete_404(client, app):
    response = client.post("/news/delete/404")

    with app.app_context():
        assert response.status_code == 404
