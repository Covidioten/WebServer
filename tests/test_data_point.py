from project.data_point.data_point import DataPoint


def test_create(client, app):
    with app.app_context():
        assert DataPoint.query.count() == 2

    assert client.get("/data-point").status_code == 200
    response = client.post("/data-point", data={"total": "25", "sentiment": 4.2,
                                                "point_date": "01.05.2020"})

    with app.app_context():
        assert DataPoint.query.count() == 3


def test_update(client, app):
    with app.app_context():
        assert DataPoint.query.get(1).total == 21
        assert DataPoint.query.get(1).sentiment == 1.4
        assert DataPoint.query.get(1).point_date == "01.01.2020"

    response = client.put("/data-point/update/1", data={
        "total": "12", "sentiment": "0.2", "point_date": "01.03.2020"})

    with app.app_context():
        assert DataPoint.query.get(1).total == 12
        assert DataPoint.query.get(1).sentiment == 0.2
        assert DataPoint.query.get(1).point_date == "01.03.2020"
        assert response.status_code == 200


def test_delete(client, app):
    response = client.post("/data-point/delete/1")

    with app.app_context():
        assert response.status_code == 200
        assert DataPoint.query.get(1) is None


def test_delete_404(client, app):
    response = client.post("/data-point/delete/404")

    with app.app_context():
        assert response.status_code == 404
