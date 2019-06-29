import unittest
from src.main import execute
from antlr4 import InputStream

from unittest.mock import patch, MagicMock

class TestNone(unittest.TestCase):
    def test_void_functions_return_none(self):
        program = """
                    funko a(){
                    
                    }
                    return a();

                                               """
        self.assertEqual(None, execute(InputStream(program)))

    def test_none_token(self):
        program = """return None;"""
        self.assertEqual(None, execute(InputStream(program)),True)

    def test_none_equals_none(self):
        program = """return None == None;"""
        self.assertEqual(True, execute(InputStream(program)), True)

    def test_only_one_none_and_attributes(self):
        program = """ a  = None;
                      a.attr = "duck";
                      b = None;
                      return b.attr;"""
        self.assertEqual("duck", execute(InputStream(program)), True)


    @patch('builtins.print')
    def test_none_operations(self,mocked_print):
        program = """ return None * 6;"""

        execute(InputStream(program), False)

        mocked_print.assert_called_once_with(
            "OperationNotSupportedException line 1: Operation * can't be applied to NONE and NUMBER")


if __name__ == '__main__':
    unittest.main()
