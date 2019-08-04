import unittest
from main import execute
from antlr4 import InputStream

from unittest.mock import patch

class TestNone(unittest.TestCase):
    def test_void_functions_return_none(self):
        program = """
                    funko a(){
                    
                    }
                    run away with a();

                                               """
        self.assertEqual(None, execute(InputStream(program)))

    def test_none_token(self):
        program = """run away with None;"""
        self.assertEqual(None, execute(InputStream(program)),True)

    def test_none_equals_none(self):
        program = """run away with None := None;"""
        self.assertEqual(True, execute(InputStream(program)), True)

    def test_only_one_none_and_attributes(self):
        program = """ a  == None;
                      a.attr == "udkc";
                      b == None;
                      run away with b.attr;"""
        self.assertEqual("duck", execute(InputStream(program)), True)


    @patch('builtins.print')
    def test_none_operations(self,mocked_print):
        program = """ run away with None * 6;"""

        execute(InputStream(program), False)

        mocked_print.assert_called_once_with(
            "OperationNotSupportedException line 1: Operation * can't be applied to NONE and NUMBER")


if __name__ == '__main__':
    unittest.main()
