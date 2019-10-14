# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from validationService.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_validate_get(self):
        """Test case for validate_get

        
        """
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '//validate',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
