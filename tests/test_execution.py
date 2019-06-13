import unittest
from src.main import execute_file,execute
from antlr4 import InputStream

class TestExecution(unittest.TestCase):

    def test_functions(self):
        self.assertEqual(27, execute_file("samples/test_function_declaration.con"))

    def test_return_no_return(self):
        self.assertEqual(None,execute(InputStream("")))

    def test_recursion(self):
        program = """  
        funko factorial(a){
            if(a==1){
                return 1
            }else{
                return a*factorial(a-1)
            }

        }
        return factorial(10)"""
        self.assertEqual(3628800, execute(InputStream(program)))

    def test_equal_precedence(self):
        self.assertEqual(True, execute(InputStream("return 3+1 == 4")))
        self.assertEqual(True, execute(InputStream("return 4 == 3+1")))

    def test_string_plus_number(self):
        program = """ return "string" + 5"""
        self.assertEqual("string5", execute(InputStream(program)))
        program2 = """ return 5+ "string" """
        self.assertEqual("5string", execute(InputStream(program2)))



if __name__ == '__main__':
    unittest.main()
