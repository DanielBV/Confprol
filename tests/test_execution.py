import unittest
from src.main import execute_file,execute
from antlr4 import InputStream
from src.exceptions import ConfProlSyntaxError, OperationNotSupported

class TestExecution(unittest.TestCase):

    def test_functions(self):
        self.assertEqual(27, execute_file("samples/test_function_declaration.con"))

    def test_return_no_return(self):
        self.assertEqual(None,execute(InputStream("")))

    def test_recursion(self):
        program = """  
        funko factorial(a){
            if(a==1){
                return 1;
            }else{
                return a*factorial(a-1);
            }

        }
        return factorial(10);"""
        self.assertEqual(3628800, execute(InputStream(program)))

    def test_equal_precedence(self):
        self.assertEqual(True, execute(InputStream("return 3+1 == 4;")))
        self.assertEqual(True, execute(InputStream("return 4 == 3+1;")))

    def test_string_plus_number(self):
        program = """ return "string" + 5;"""
        self.assertEqual("string5", execute(InputStream(program)))
        program2 = """ return 5+ "string";"""
        self.assertEqual("5string", execute(InputStream(program2)))

    def test_strig_mult_number(self):
        program = """ return "string" * 5;"""
        with self.assertRaises(OperationNotSupported):
            execute(InputStream(program))

        program2 = """ return 5* "string";"""
        with self.assertRaises(OperationNotSupported):
            execute(InputStream(program2))


    def test_missing_semicolon(self):
        program = """ return "string" + 5"""
        with self.assertRaises(ConfProlSyntaxError):
            execute(InputStream(program))

    def test_expression_without_statement(self):
        program = """3+2+10;"""
        self.assertEqual(None, execute(InputStream(program)))

    def test_inline_comment(self):
        program = """if 3  // THIS IS A COMMENT
                    { // A comment
                        // return 1;
                        return 6;  //Other comment
                    } // Is this a comment?"""
        self.assertEqual(6, execute(InputStream(program)))

    def test_comments(self):
        program = """if 3 /* IS THIS A REFERENCE? */
                      { //
                        /**/
                          /*Random string
                           // * /
                          
                                return 1;
                          Another random string*/
                          return 6;  
                      } 
                      /* NO, THIS ISN'T A REFERENCE */
                      
                      """
        self.assertEqual(6, execute(InputStream(program)))

    def test_boolean_true(self):
        program = """if True { 
                            return 6;
                     }else{
                            return 10;
                    }

                              """
        self.assertEqual(6, execute(InputStream(program)))

    def test_boolean_false(self):
        program = """if False { 
                               return 6;
                        }{
                               return 10;
                       }

                                 """
        self.assertEqual(6, execute(InputStream(program)))


if __name__ == '__main__':
    unittest.main()
