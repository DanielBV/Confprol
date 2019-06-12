import unittest
from src.main import execute_file,execute
from antlr4 import InputStream

class TestExecution(unittest.TestCase):

    def test_functions(self):
        self.assertEqual(27, execute_file("samples/test_function_declaration.con"))

    def test_return_no_return(self):
        self.assertEqual(None,execute(InputStream("begin end")))


if __name__ == '__main__':
    unittest.main()
