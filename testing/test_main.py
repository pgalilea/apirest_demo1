from os.path import dirname, realpath, expanduser

from fastapi.testclient import TestClient

from sys import path; path.append( dirname(dirname(realpath(expanduser(__file__)))))
from app.main import app

client = TestClient(app)

def test_read_item():
    response = client.get('/patentes/AAAA000')
    assert response.status_code == 200

