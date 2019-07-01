
import unittest
from src.main import execute
from antlr4 import InputStream
from unittest.mock import patch

class TestDefaultFunctions(unittest.TestCase):

    def test_object_attributes(self):
        program = """
            a = object();
            a.b = 1;
            return [a,a.b];

        """
        return_value = execute(InputStream(program), True)
        object_ = return_value[0]
        attr = return_value[1]
        self.assertEqual(object, type(object_))
        self.assertEqual(1, attr)

    def test_object_equality(self):
        program = """
                    a = object();
                    b = object();
                    return a == b;

                """

        self.assertFalse(execute(InputStream(program), True))

    def test_number_to_integer(self):
        program = """
                       return [int(3.001), int(4.0), int(5), int(6.9)];

                      """

        self.assertEqual([3,4,5,6],execute(InputStream(program), True))

    def test_boolean_to_integer(self):
        program = """
                         return [int(True),int(False)];

                        """

        self.assertEqual([1,0], execute(InputStream(program), True))



    def test_string_to_integer(self):
        program = """
                                return [int("3.2"),int("-5")];

                               """

        self.assertEqual([3, -5], execute(InputStream(program), True))

    @patch('builtins.print')
    def test_random_string_to_integer(self,mocked_print):
        program = """
                        int("hey listen");

                 """

        execute(InputStream(program), False)
        mocked_print.assert_called_once_with(
           "ValueException line 2: The string 'hey listen' can't be transformed to integer.")

    @patch('builtins.print')
    def test_object_to_integer(self, mocked_print):
        program = """
                          int(object());

                   """

        execute(InputStream(program), False)
        mocked_print.assert_called_once_with(
            "ValueException line 2: Cannot transform an object of type OBJECT to integer.")




if __name__ == '__main__':
    unittest.main()
