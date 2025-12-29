import pytest
import requests
from url import UrlAndEndpoint 


class TestCreatePostSucces:
    def test_create_post_success(self):
        payload = {"title": "foo", "body": "bar", "userId": 1}
        resp = requests.post(UrlAndEndpoint.CREATE_POST, json=payload)
        assert resp.status_code == 201
        data = resp.json()
        assert isinstance(data, dict)
        assert "id" in data
        assert data["title"] == payload["title"]
        assert data["body"] == payload["body"]
        assert data["userId"] == payload["userId"]
        assert isinstance(data["id"], int)

        