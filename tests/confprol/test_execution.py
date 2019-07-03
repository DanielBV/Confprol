import unittest
from src.main import execute_file,execute
from antlr4 import InputStream
import os
from src.exceptions.syntax_error import ConfProlSyntaxError

from unittest.mock import patch

class TestExecution(unittest.TestCase):

    def setUp(self):
        self.test_path =   os.path.dirname(__file__)
    def test_functions(self):

        self.assertEqual(27, execute_file(f"{self.test_path}/samples/test_function_declaration.con"))

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
                        }else{
                               return 10;
                       }

                                 """
        self.assertEqual(10, execute(InputStream(program)))

    def test_string_length_inside_variable(self):
        program = """a = "Hey listen";
                    return a.length();"""
        self.assertEqual(10, execute(InputStream(program)))

    def test_string_length(self):
        program = """return "Heylisten".length();"""
        self.assertEqual(9, execute(InputStream(program)))

    def test_store_function_as_variable(self):
        program = """
            funko function(){
                funko gearsOfFunko(a,b){
                    return a+b;
                }
                
                return gearsOfFunko;
            
            }
            
            a = function();
            return a(2,3);
            
        
        """
        self.assertEqual(5, execute(InputStream(program)))

    def test_float(self):
        program = """
                  a = 0.0000003;
                  return a;

                """
        self.assertEqual(0.0000003, execute(InputStream(program)),0.0000000000000001)




    def test_assign_subattributes(self):
        program = """
            a = 6;
            a.a = 3;
            a.a.B = 5;
            return [a.a,a.a.B];"""

        self.assertEqual([3,5],   execute(InputStream(program)))

    def test_assignation_keeps_attribute(self):
        program = """
        a = 3;
        a.a = 5;
        
        b = a;
        return b.a;
        """

        self.assertEqual( 5, execute(InputStream(program)))

    def test_changing_attributes_changes_all_alias(self):
        program = """
        a = 3;
        a.a = 5;

        b = a;
        b.a = 7;
        return a.a;
        """

        self.assertEqual(7, execute(InputStream(program)))


    def test_function_attributes(self):
        program = """
        funko ralph(){
            }
        ralph.a = 3;
        return ralph.a;
        
        """

        self.assertEqual(3, execute(InputStream(program)))

    def test_method_attributes(self):
        program = """
                string = "This is a string";
                string.length.a = 42;
                return string.length.a;

              """

        self.assertEqual(42, execute(InputStream(program)))





    def test_context_is_stored_appropriately(self):
        program ="""
                funko mylength(value,original){
        
                        funko oneMore(){
                            return original + 1;
                    
                        }
        
                        return oneMore;
                }
        
                a =  mylength(3,4);
                first = a();
                b =  mylength(3,5);
                return [first,a(),b()];
               
                """
        self.assertEqual([5,5,6], execute(InputStream(program), False))


    def test_negative_numbers(self):
        program = """
                    return -3 * -6 / -1;
        
                  """
        self.assertEqual(-18, execute(InputStream(program), False))

    def test_variables_cant_start_with_number(self):
        program = """
                         6a = 3;
                         """

        with self.assertRaises(ConfProlSyntaxError) as e:
            execute(InputStream(program), True)

        self.assertEqual("SyntaxException in line 2:25 mismatched input '6a' expecting {<EOF>, 'import', 'print', 'if', 'return', '-', '(', '[', 'funko', BOOLEAN, FLOAT, 'None', ID, NUMBER, STRING}",e.exception.get_message())

    def test_variables_with_numbers_and_underscore(self):
        program = """
                    __oh_bOy53 =  14;
    
                    return __oh_bOy53;
                   """

        self.assertEqual(14,execute(InputStream(program), True))



    def test_import(self):
        program = """
            import "REPLACE_PATH" as imported;
            
            return [imported.value, imported.plus6(4)];
        """
        path = os.path.join(self.test_path, "samples","imported_file")
        program = program.replace("REPLACE_PATH", path)


        self.assertEqual([3,10],execute(InputStream(program), True))

    @patch('builtins.print')
    def test_import_file_not_found(self, mocked_print):
        program = """
                   import "./thisfileshouldntexist/nope/pizza" as smth;

                   return [imported.value, imported.plus6(4)];
               """

        execute(InputStream(program), False)
        mocked_print.assert_called_with(
            "FileNotFoundException line 2: File ./thisfileshouldntexist/nope/pizza not found.")

    @patch('builtins.print')
    def test_import_directory(self, mocked_print):
        program = """
                           import "REPLACE_PATH" as foo;
                       """

        path = os.path.join(self.test_path,"samples")
        program = program.replace("REPLACE_PATH",path)
        execute(InputStream(program), False)
        mocked_print.assert_called_with(
            f"CannotOpenDirectoryException line 2: The directory {path} can't be opened or imported.")


    def test_insum(self):
        program = """
                 a = 4;
                 a+=5;
                 return a;
             """

        self.assertEqual(9, execute(InputStream(program), True))

    def test_inmult(self):
        program = """
                 a = 4;
                 a*=5;
                 return a;
             """

        self.assertEqual(20, execute(InputStream(program), True))

    def test_indivision(self):
        program = """
                    a = 4;
                    a/=5;
                    return a;
                """

        self.assertEqual(0.8, execute(InputStream(program), True))

    def test_inminus(self):
        program = """
                       a = 4;
                       a-=5;
                       return a;
                   """

        self.assertEqual(-1, execute(InputStream(program), True))


if __name__ == '__main__':
    unittest.main()
