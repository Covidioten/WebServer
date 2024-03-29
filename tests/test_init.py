from project import create_app


def test_config():
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


def test_db_url_environ(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "sqlite:///environ")
    app = create_app()
    assert app.config["SQLALCHEMY_DATABASE_URI"] == "sqlite:///environ"


def test_init_db_command(runner, monkeypatch):
    class Recorder:
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr("project.init_db", fake_init_db)
    result = runner.invoke(args=["init-db"])
    assert "Initialized" in result.output
    assert Recorder.called
