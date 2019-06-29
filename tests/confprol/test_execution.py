import unittest
from src.main import execute_file,execute
from antlr4 import InputStream
import os



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

    def test_changin_attributes_changes_all_alias(self):
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


if __name__ == '__main__':
    unittest.main()
