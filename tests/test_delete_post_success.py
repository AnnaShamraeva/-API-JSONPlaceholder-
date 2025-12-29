import pytest
import requests
from url import UrlAndEndpoint 
from data import Message


class TestDeletePost:
    def test_delete_post_success(self):
        resp = requests.delete(UrlAndEndpoint.DELETE_POST)
        
        assert resp.status_code in (200, 202, 204)
        assert Message.DELETE_POST == resp.text


 