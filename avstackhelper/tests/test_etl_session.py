"""Module for testing etl.sesion."""
from mock import patch, MagicMock

from avstackhelper.etl.session import postgresql_connect, postgresql_fetch_data


def test_postgres_connect_fail():
    conn = postgresql_connect({})
    assert conn == None


def test_postgres_connect_ok(mocker):
    metadata = {
        "host": "db_postgres",
        "database": "dbstack",
        "user": "user",
        "password": "xxxxxx"
    }
    p2_conn = patch('avstackhelper.etl.session.connect').start()
    p2_conn.return_value = "CONNECT"
    conn = postgresql_connect(metadata)
    assert conn == "CONNECT"


def test_postgresql_fetch_data_no_data():
    conn = MagicMock()
    conn.cursor = MagicMock()
    conn.cursor.return_value = Exception
    tupple = postgresql_fetch_data(conn, "Select * FROM A")
    assert len(tupple) == 0


class ConnMock:
    def __init__(self, data):
        self.data = data

    def cursor(self):
        return self

    def execute(self, *args):
        return True

    def fetchall(self):
        return self.data

    def close(self):
        return True


def test_postgresql_fetch_data_ok():
    conn = ConnMock([1] * 10)
    tupple = postgresql_fetch_data(conn, "Select * FROM A")
    assert len(tupple) == 10


# TODO Require more advances test