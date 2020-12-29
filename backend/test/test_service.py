import unittest
from unittest.mock import patch

from service.service import (add_request, get_common_description_count,
                             get_page_requests)

from app import app


class ServiceTest(unittest.TestCase):
    @patch('service.service.Pagination')
    def test_get_page_requests(self, mock_pagination):
        mock_pagination.paginate.return_value = {
            "data": [
                {
                    "client": "client a",
                    "date": "2021-12-29 00:00:00",
                    "description": "asd",
                    "name": "asd",
                    "priority": 1,
                    "productarea": "Assessments"
                }
            ],
            "pagination": {
                "currentPage": "/api/featurerequest?page=1&size=5",
                "hasNext": False,
                "hasPrev": False,
                "pages": 1,
                "size": 5,
                "totalElements": 1
            }
        }

        assert get_page_requests(page=0)

    @patch('service.service.FeatureRequest')
    @patch('service.service.db')
    def test_add_request(self, mock_feature_req, mock_db):
        old_data = [{"client": "client a", "date": "2021-12-29 00:00:00", "description": "asd", "name": "asd", "priority": 1, "productarea": "Assessments"},
                    {"client": "client b", "date": "2021-12-29 00:00:00", "description": "asdf", "name": "asd", "priority": 1, "productarea": "Assessments"}]
        new_data = {"client": "clienta", "date": "2021-12-2900:00:00",
                    "description": "asd", "name": "asd", "priority": 1, "productarea": "Assessments"}
        mock_db.return_value()
        mock_feature_req.return_value(old_data)
        add_request(new_data['name'], new_data['description'], new_data['client'],
                    new_data['date'], new_data['priority'], new_data['productarea'])

    def test_get_common_description_count(self):
        common_descriptions = get_common_description_count(
            ['Hello earth', 'What is your name'], 'Hello world')
        assert common_descriptions == 1
