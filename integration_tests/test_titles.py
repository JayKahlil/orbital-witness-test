from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_list_titles():
    response = client.get("/api/titles/?_page=1&_limit=2")
    assert response.status_code == 200
    assert response.json() == {
        "titles": [
            {
                "id": "0",
                "title_number": "MYBKZ10625",
                "title_class": "Freehold",
            },
            {
                "id": "1",
                "title_number": "GP51",
                "title_class": "Leasehold",
            }
        ],
        "page": 1,
        "page_size": 2,
        "total_titles": 1000
    }
