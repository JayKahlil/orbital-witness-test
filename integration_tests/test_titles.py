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


def test_get_title():
    response = client.get("/api/titles/4")
    assert response.status_code == 200
    assert response.json() == {
        "id": "4",
        "title_number": "ZULV94",
        "title_class": "Freehold",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean convallis lectus velit, ac mollis lorem fringilla ac. In consequat molestie dui, et pellentesque nisl convallis at. Curabitur dictum lacinia justo, pulvinar pharetra purus rutrum eu. Curabitur euismod dignissim turpis, vitae tincidunt leo condimentum non. Donec id dui in libero feugiat aliquet nec eu nulla. Proin eu enim dictum, viverra lacus vitae, porta arcu. Nam ullamcorper, odio in volutpat fermentum, odio lectus gravida nunc, eget imperdiet nibh nisi at elit. Suspendisse dapibu"
    }
