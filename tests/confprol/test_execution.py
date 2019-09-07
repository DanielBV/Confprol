import unittest
from main import execute_file,execute
from antlr4 import InputStream
import os
from exceptions.syntax_error import ConfProlSyntaxError

from unittest.mock import patch

class TestExecution(unittest.TestCase):

    def setUp(self):
        self.test_path =   os.path.dirname(__file__)
    def test_functions(self):

        self.assertEqual(27, execute_file(f"{self.test_path}/samples/test_function_declaration.con"))

    def test_returns_none_if_there_isnt_run_away_with(self):
        self.assertEqual(None,execute(InputStream("")))

    def test_recursion(self):
        program = """  
        funko factorial(a){
            if not (a:=1){
                run away with a*factorial(a-1);
            }else{
                run away with 1;
               
            }

        }
        run away with factorial(10);"""
        self.assertEqual(3628800, execute(InputStream(program)))

    def test_equal_precedence(self):
        self.assertEqual(True, execute(InputStream("run away with 3+1 := 4;")))
        self.assertEqual(True, execute(InputStream("run away with 4 := 3+1;")))






    def test_expression_without_statement(self):
        program = """3+2+10;"""
        self.assertEqual(None, execute(InputStream(program)))


    def test_comments(self):
        program = """if not 0 @useless_comment    (IS THIS A REFERENCE? 
        )
                      { 
                        @useless_comment()
                          @useless_comment( run away with 1;)
                           
                          
                               
                         
                          run away with 6;  
                      } 
                      @useless_comment( NO, THIS ISN'T A REFERENCE )
                      
                      """
        self.assertEqual(6, execute(InputStream(program)))

    def test_boolean_true(self):
        program = """if not True { 
                           run away with 10;
                     }else{
                          run away with 6;
                           
                    }

                              """
        self.assertEqual(6, execute(InputStream(program)))

    def test_boolean_false(self):
        program = """if not False { 
                              run away with 10; 
                        }else{
                            run away with 6;
                               
                       }

                                 """
        self.assertEqual(10, execute(InputStream(program)))

    def test_string_length_inside_variable(self):
        program = """a == "Hey listen";
                    run away with a.length();"""
        self.assertEqual(10, execute(InputStream(program)))

    def test_string_length(self):
        program = """run away with "Heylisten".length();"""
        self.assertEqual(9, execute(InputStream(program)))

    def test_store_function_as_variable(self):
        program = """
            funko function(){
                funko gearsOfFunko(a,b){
                    run away with a+b;
                }
                
                run away with gearsOfFunko;
            
            }
            
            a == function();
            run away with a(2,3);
            
        
        """
        self.assertEqual(5, execute(InputStream(program)))

    def test_float(self):
        program = """
                  a == 0.0000003;
                  run away with a;

                """
        self.assertEqual(0.0000003, execute(InputStream(program)),0.0000000000000001)




    def test_assign_subattributes(self):
        program = """
            a == 6;
            a.a == 3;
            a.a.B == 5;
            run away with [a.a,a.a.B];"""

        self.assertEqual([3,5],   execute(InputStream(program)))

    def test_assignation_keeps_attribute(self):
        program = """
        a == 3;
        a.a == 5;
        
        b == a;
        run away with b.a;
        """

        self.assertEqual( 5, execute(InputStream(program)))

    def test_changing_attributes_changes_all_alias(self):
        program = """
        a == 3;
        a.a == 5;

        b == a;
        b.a == 7;
        run away with a.a;
        """

        self.assertEqual(7, execute(InputStream(program)))


    def test_function_attributes(self):
        program = """
        funko ralph(){
            }
        ralph.a == 3;
        run away with ralph.a;
        
        """

        self.assertEqual(3, execute(InputStream(program)))

    def test_method_attributes(self):
        program = """
                string == "This is a string";
                string.length.a == 42;
                run away with string.length.a;

              """

        self.assertEqual(42, execute(InputStream(program)))





    def test_context_is_stored_appropriately(self):
        program ="""
                funko mylength(value,original){
        
                        funko oneMore(){
                            run away with original + 1;
                    
                        }
        
                        run away with oneMore;
                }
        
                a ==  mylength(3,4);
                first == a();
                b ==  mylength(3,5);
                run away with [first,a(),b()];
               
                """
        self.assertEqual([5,5,6], execute(InputStream(program), False))


    def test_negative_numbers(self):
        program = """
                    run away with -3 * -6 / -1;
        
                  """
        self.assertEqual(-18, execute(InputStream(program), False))

    def test_variables_cant_start_with_number(self):
        program = """
                         6a == 3;
                         """

        with self.assertRaises(ConfProlSyntaxError) as e:
            execute(InputStream(program), True)

        self.assertIn("SyntaxException in line 2:25 mismatched input '6a' expecting",e.exception.get_message())

    def test_variables_with_numbers_and_underscore(self):
        program = """
                    __oh_bOy53 ==  14;
    
                    run away with __oh_bOy53;
                   """

        self.assertEqual(14,execute(InputStream(program), True))



    def test_import(self):
        program = """
            import "REPLACE_PATH" as imported;
            
            run away with [imported.value, imported.plus6(4)];
        """
        path = os.path.join(self.test_path, "samples","imported_file")
        program = program.replace("REPLACE_PATH", path)


        self.assertEqual([3,10],execute(InputStream(program), True))

    @patch('builtins.print')
    def test_import_file_not_found(self, mocked_print):
        program = """
                   import "./thisfileshouldntexist/nope/pizza" as smth;

                   run away with [imported.value, imported.plus6(4)];
               """

        execute(InputStream(program), False)
        mocked_print.assert_called_with(
            "FileNotFoundException line 2: File .\\./thisfileshouldntexist/nope/pizza not found.")

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
                 a == 4;
                 a=+=5;
                 run away with a;
             """

        self.assertEqual(9, execute(InputStream(program), True))

    def test_inmult(self):
        program = """
                 a == 4;
                 a=*=5;
                 run away with a;
             """

        self.assertEqual(20, execute(InputStream(program), True))

    def test_indivision(self):
        program = """
                    a == 4;
                    a=/=5;
                    run away with a;
                """

        self.assertEqual(0.8, execute(InputStream(program), True))

    def test_inminus(self):
        program = """
                       a == 4;
                       a=-=5;
                       run away with a;
                   """

        self.assertEqual(-1, execute(InputStream(program), True))

    def test_run_away_with_with_spaces(self):
        program = """
                    run                       away                   with             9   ;
                          """

        self.assertEqual(9, execute(InputStream(program), True))


    def test_load_string(self):
        program = """
            run away with ["esto_es_una_cadena","a","ab","aba"]; 
            """


        value=  execute(InputStream(program), True)
        self.assertEqual(["seanedac_unato_es_","a","ba","baa"],value)

    def test_string_new_line(self):
        program = r"""
              run away with ["Just one \n line","nOher linenotAn\ enil e"]; 
              """

        value = execute(InputStream(program), True)
        self.assertEqual(["uJenil ne \st on","One line \nAnother line"], value)

    def test_escape_character_double_quote(self):
        program = r"""
            run away with "eTcharacter: \"pe acse etouq ts";
        """
        value = execute(InputStream(program), True)
        self.assertEqual("Test quote escape character: \"", value)

    def test_negation_preference(self):
        program = """
        run away with !-1+1;
        """
        value = execute(InputStream(program), True)

        self.assertTrue(value)

    def test_multiple_negation(self):
        program = """
               run away with !!!!True;
               """

        value = execute(InputStream(program), True)

        self.assertTrue(value)

    def test_multiple_backward_slashes(self):
        program = r"""
            string == "\\\\";
            other_string == "\a\""
            this_fails == "\\"";
        
        """

        with self.assertRaises(ConfProlSyntaxError) as e:
            value = execute(InputStream(program), True)

        self.assertIn("SyntaxException in line 4:12 missing ';' at 'this_fails'", e.exception.get_message())


if __name__ == '__main__':
    unittest.main()
