import ast
import unittest

import fibonappi


class FibonappiTestCase(unittest.TestCase):
    def setUp(self):
        fibonappi.app.config['TESTING'] = True
        self.app = fibonappi.app.test_client()

    def tearDown(self):
        pass

    def test_negative_input(self):
        response = self.app.get('/fibonacci/-1')
        assert '400' in response.status

    def test_fibonacci_response_0(self):
        response = self.app.get('/fibonacci/0')
        assert '200' in response.status
        assert 'application/json' in response.content_type
        assert [] == ast.literal_eval(response.data)

    def test_fibonacci_response_1(self):
        response = self.app.get('/fibonacci/1')
        assert '200' in response.status
        assert 'application/json' in response.content_type
        assert [0] == ast.literal_eval(response.data)

    def test_fibonacci_response_3(self):
        response = self.app.get('/fibonacci/3')
        assert '200' in response.status
        assert 'application/json' in response.content_type
        assert [0, 1, 1] == ast.literal_eval(response.data)

    def test_fibonacci_response_5(self):
        response = self.app.get('/fibonacci/5')
        assert '200' in response.status
        assert 'application/json' in response.content_type
        assert [0, 1, 1, 2, 3] == ast.literal_eval(response.data)

    def test_fibonacci_response_5_not_in(self):
        response = self.app.get('/fibonacci/5')
        assert '200' in response.status
        assert 'application/json' in response.content_type
        assert [0, 1, 1, 2, 3, 5] != ast.literal_eval(response.data)


if __name__ == '__main__':
    unittest.main()
