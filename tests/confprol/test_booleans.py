
import unittest
from src.main import execute
from antlr4 import InputStream
from unittest.mock import patch,Mock
import datetime
from src.expressions.booleans.true_except_fridays import TrueExceptFridays


class TestBooleans(unittest.TestCase):

    @patch.object(TrueExceptFridays,'get_todays_weekday')
    def test_true_except_friday_in_saturday(self,mocked_day):
        mocked_day.return_value = 6

        program = """
                    run away with TrueExceptFridays;
                """
        value = execute(InputStream(program), False)

        self.assertTrue(value)

    @patch.object(TrueExceptFridays, 'get_todays_weekday')
    def test_true_except_friday_in_sunday(self, mocked_day):
        mocked_day.return_value = 7

        program = """
                       run away with TrueExceptFridays;
                   """
        value = execute(InputStream(program), False)

        self.assertTrue(value)

    @patch.object(TrueExceptFridays, 'get_todays_weekday')
    def test_true_except_friday_in_friday(self, mocked_day):
        mocked_day.return_value = 5

        program = """
                       run away with TrueExceptFridays;
                   """
        value = execute(InputStream(program), False)

        self.assertFalse(value)

    @patch.object(TrueExceptFridays, 'get_todays_weekday')
    def test_true_except_friday_in_thursday(self, mocked_day):
        mocked_day.return_value = 4

        program = """
                       run away with TrueExceptFridays;
                   """
        value = execute(InputStream(program), False)

        self.assertTrue(value)

    @patch.object(TrueExceptFridays, 'get_todays_weekday')
    def test_true_except_friday_in_wednesday(self, mocked_day):
        mocked_day.return_value = 3

        program = """
                       run away with TrueExceptFridays;
                   """
        value = execute(InputStream(program), False)

        self.assertTrue(value)

    @patch.object(TrueExceptFridays, 'get_todays_weekday')
    def test_true_except_friday_in_tuesday(self, mocked_day):
        mocked_day.return_value = 2

        program = """
                       run away with TrueExceptFridays;
                   """
        value = execute(InputStream(program), False)

        self.assertTrue(value)

    @patch.object(TrueExceptFridays, 'get_todays_weekday')
    def test_true_except_friday_in_monday(self, mocked_day):
        mocked_day.return_value = 1

        program = """
                       run away with TrueExceptFridays;
                   """
        value = execute(InputStream(program), False)

        self.assertTrue(value)

if __name__ == '__main__':
    unittest.main()
