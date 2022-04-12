import unittest
import random as rd
from unittest.mock import Mock, call
from faker import Faker
from HTMLParser import parse_html
from contextlib import contextmanager


class TestHTMLParser(unittest.TestCase):
    def setUp(self):
        self.open_tag_callback_mock = Mock()
        self.data_callback_mock = Mock()
        self.close_tag_callback_mock = Mock()
        rd.seed()
        Faker.seed(0)
        self.fake = Faker()
        print("Set up")

    def tearDown(self):
        print("Tear down")

    @contextmanager
    def assertNotRaises(self, exc_type):
        try:
            yield None
        except():
            raise self.failureException('{} raised'.format(exc_type.__name__))

    def test_parser_html_no_raises(self):
        with self.assertNotRaises(TypeError):
            parse_html("", self.open_tag_callback_mock, self.data_callback_mock, self.close_tag_callback_mock)
            parse_html("", None,  self.data_callback_mock, self.close_tag_callback_mock)
            parse_html("", self.open_tag_callback_mock, None, self.close_tag_callback_mock)
            parse_html("", self.open_tag_callback_mock,  self.data_callback_mock, None)
            parse_html("", None, None, None)
            html_str = '?' * rd.randint(1, 10) + ' ' * rd.randint(1, 10) + '<' + '?' * rd.randint(1, 10) + '>'
            html_str += ' ' * rd.randint(1, 10) + '?' * rd.randint(1, 10) + ' ' * rd.randint(1, 10)
            html_str += '</' + '?' * rd.randint(1, 10) + '>'
            html_str = self.fake.bothify(text=html_str)
            parse_html(html_str, None,  self.data_callback_mock, self.close_tag_callback_mock)
            parse_html(html_str, self.open_tag_callback_mock, None, self.close_tag_callback_mock)
            parse_html(html_str, self.open_tag_callback_mock,  self.data_callback_mock, None)
            parse_html(html_str, None, None, None)

    def test_parser_html(self):
        parse_html("", self.open_tag_callback_mock, self.data_callback_mock, self.close_tag_callback_mock)
        self.assertEqual(self.open_tag_callback_mock.call_count, 0)
        self.assertEqual(self.data_callback_mock.call_count, 0)
        self.assertEqual(self.close_tag_callback_mock.call_count, 0)

        html_str = self.fake.bothify(text='?' * rd.randint(1, 1000))
        parse_html(html_str, self.open_tag_callback_mock, self.data_callback_mock, self.close_tag_callback_mock)
        self.assertEqual(self.open_tag_callback_mock.call_count, 0)
        self.assertEqual(self.data_callback_mock.call_count, 1)
        self.assertEqual(self.close_tag_callback_mock.call_count, 0)
        self.data_callback_mock.assert_called_once_with(html_str)

        html_str = self.fake.bothify(text='      '+'?' * rd.randint(1, 10))
        parse_html(html_str, self.open_tag_callback_mock, self.data_callback_mock, self.close_tag_callback_mock)
        self.assertEqual(self.open_tag_callback_mock.call_count, 0)
        self.assertEqual(self.data_callback_mock.call_count, 2)
        self.assertEqual(self.close_tag_callback_mock.call_count, 0)
        self.data_callback_mock.assert_called_with(html_str)

        html_str = self.fake.bothify(text='?' * rd.randint(1, 10) + '     ')
        parse_html(html_str, self.open_tag_callback_mock, self.data_callback_mock, self.close_tag_callback_mock)
        self.assertEqual(self.open_tag_callback_mock.call_count, 0)
        self.assertEqual(self.data_callback_mock.call_count, 3)
        self.assertEqual(self.close_tag_callback_mock.call_count, 0)
        self.data_callback_mock.assert_called_with(html_str)

        html_str = self.fake.bothify(text=' ' * rd.randint(1, 10) + '?' * rd.randint(1, 10) + ' ' * rd.randint(1, 10) + '?' * rd.randint(1, 10) + ' ' * rd.randint(1, 10))
        parse_html(html_str, self.open_tag_callback_mock, self.data_callback_mock, self.close_tag_callback_mock)
        self.assertEqual(self.open_tag_callback_mock.call_count, 0)
        self.assertEqual(self.data_callback_mock.call_count, 4)
        self.assertEqual(self.close_tag_callback_mock.call_count, 0)
        self.data_callback_mock.assert_called_with(html_str)

        first_tag_name = self.fake.bothify(text='?' * rd.randint(1, 10))
        html_str = f"<{first_tag_name}></{first_tag_name}>"
        parse_html(html_str, self.open_tag_callback_mock, self.data_callback_mock, self.close_tag_callback_mock)
        self.assertEqual(self.open_tag_callback_mock.call_count, 1)
        self.assertEqual(self.data_callback_mock.call_count, 4)
        self.assertEqual(self.close_tag_callback_mock.call_count, 1)
        self.open_tag_callback_mock.assert_called_with([f"{first_tag_name}"])
        self.close_tag_callback_mock.assert_called_with([f"{first_tag_name}"])

        first_tag_name = self.fake.bothify(text='?' * rd.randint(1, 10))
        html_str = f"<{first_tag_name}>"
        parse_html(html_str, self.open_tag_callback_mock, self.data_callback_mock, self.close_tag_callback_mock)
        self.assertEqual(self.open_tag_callback_mock.call_count, 2)
        self.assertEqual(self.data_callback_mock.call_count, 4)
        self.assertEqual(self.close_tag_callback_mock.call_count, 1)
        self.open_tag_callback_mock.assert_called_with([f"{first_tag_name}"])

        first_tag_name = self.fake.bothify(text='?' * rd.randint(1, 10))
        second_tag_name = self.fake.bothify(text='?' * rd.randint(1, 10))
        html_str = f"<{first_tag_name}></{second_tag_name}>"
        parse_html(html_str, self.open_tag_callback_mock, self.data_callback_mock, self.close_tag_callback_mock)
        self.assertEqual(self.open_tag_callback_mock.call_count, 3)
        self.assertEqual(self.data_callback_mock.call_count, 4)
        self.assertEqual(self.close_tag_callback_mock.call_count, 2)
        self.open_tag_callback_mock.assert_called_with([f"{first_tag_name}"])
        self.close_tag_callback_mock.assert_called_with([f"{second_tag_name}"])

        first_tag_name = self.fake.bothify(text='?' * rd.randint(1, 10))
        second_tag_name = self.fake.bothify(text='?' * rd.randint(1, 10))
        html_str = f"<{first_tag_name}></{second_tag_name}></{first_tag_name}>"
        parse_html(html_str, self.open_tag_callback_mock, self.data_callback_mock, self.close_tag_callback_mock)
        self.assertEqual(self.open_tag_callback_mock.call_count, 4)
        self.assertEqual(self.data_callback_mock.call_count, 4)
        self.assertEqual(self.close_tag_callback_mock.call_count, 4)
        self.open_tag_callback_mock.assert_called_with([f"{first_tag_name}"])
        self.close_tag_callback_mock.assert_has_calls([call([f"{second_tag_name}"]), call([f"{first_tag_name}"])])

        first_tag_name = self.fake.bothify(text='?' * rd.randint(1, 10))
        second_tag_name = self.fake.bothify(text='?' * rd.randint(1, 10))
        first_attr_name = self.fake.bothify(text='?' * rd.randint(1, 10))
        first_attr = self.fake.bothify(text='?' * rd.randint(1, 10))
        second_attr_name = self.fake.bothify(text='?' * rd.randint(1, 10))
        second_attr = self.fake.bothify(text='?' * rd.randint(1, 10))
        first_data = self.fake.bothify(text='?' * rd.randint(1, 10))
        second_data = self.fake.bothify(text='?' * rd.randint(1, 10))
        third_data = self.fake.bothify(text='?' * rd.randint(1, 10))
        html_str = f"{first_data}<{first_tag_name} {first_attr_name}={first_attr}>{second_data}"
        html_str += f"</{second_tag_name}>{third_data}</{first_tag_name} {second_attr_name}={second_attr}>"
        parse_html(html_str, self.open_tag_callback_mock, self.data_callback_mock, self.close_tag_callback_mock)
        self.assertEqual(self.open_tag_callback_mock.call_count, 5)
        self.assertEqual(self.data_callback_mock.call_count, 7)
        self.assertEqual(self.close_tag_callback_mock.call_count, 6)
        self.open_tag_callback_mock.assert_called_with([f"{first_tag_name}", f"{first_attr_name}={first_attr}"])
        self.data_callback_mock.assert_has_calls([call(f"{first_data}"), call(f"{second_data}"), call(f"{third_data}")])
        self.close_tag_callback_mock.assert_has_calls([call([f"{second_tag_name}"]), call([f"{first_tag_name}", f"{second_attr_name}={second_attr}"])])

        html_str = "<>"
        parse_html(html_str, self.open_tag_callback_mock, self.data_callback_mock, self.close_tag_callback_mock)
        self.assertEqual(self.open_tag_callback_mock.call_count, 6)
        self.assertEqual(self.data_callback_mock.call_count, 7)
        self.assertEqual(self.close_tag_callback_mock.call_count, 6)
        self.open_tag_callback_mock.assert_called_with([])


if __name__ == "__main__":
    unittest.main()
