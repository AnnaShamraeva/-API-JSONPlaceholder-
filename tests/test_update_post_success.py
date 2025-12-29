import pytest
import requests
from url import UrlAndEndpoint 


class TestUpdatePostSuccess:
    def test_update_post_success(self):      
        payload = {"id": 1, "title": "foo updated", "body": "bar updated", "userId": 1}
        resp = requests.put(UrlAndEndpoint.UPDATING_POST, json=payload)

        assert resp.status_code == 200
        data = resp.json()
        assert data["id"] == payload["id"]
        assert data["title"] == payload["title"]
        assert data["body"] == payload["body"]
        assert data["userId"] == payload["userId"]