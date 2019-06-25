import unittest
from src.main import execute_file,execute
from antlr4 import InputStream
from src.exceptions import ConfProlSyntaxError, OperationNotSupported, RuntimeException
import os,sys

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

    def test_list(self):
        program = """
        
            e = [[6,[5,9],2],2,3,4];
            return  e.get(0).get(1).get(1);
        """
        self.assertEqual(9, execute(InputStream(program)))

    def test_lists_evaluate_expressions(self):
        program = """
                funko returnsFour(){
                    return 5; // The four was a lie, the cake too.   
                }
                  e = [6*5+4+ returnsFour()];
                  return  e.get(0);
              """
        self.assertEqual(39, execute(InputStream(program)))

    def test_list_length(self):
        program = """
                   e = [3,[1,2,3],4];
                   return  e.length();
               """
        self.assertEqual(3, execute(InputStream(program)))

    def test_list_add(self):
        program = """
                      e = [3];
                      e.append(4);
                      return  [e.length(),e.get(1),e];
                  """
        self.assertEqual([2,4,[3,4]], execute(InputStream(program)))

    def test_list_remove(self):
        program = """
                         e = [3,4,5,3,6];
                         e.remove(3);
                         return [e,e.length()];
                     """
        self.assertEqual([[4,5,3,6],4], execute(InputStream(program)))

    def test_list_remove_not_contained(self):
        program = """
                       e = [];
                       e.remove(9);
                       return e;
                """
        with self.assertRaises(RuntimeException) as e:
            execute(InputStream(program))

        self.assertIn(e.exception.get_message(),"ElementNotContainedException line 3: The list e doesn't contain 9")


    def test_list_insert(self):
        program = """
                             e = [];
                             e.insert(3,"VALUE");
                             f = [1,2,3,4];
                             f.insert(2,"VALUE");
                             return [e,f];
                      """
        self.assertEqual([["VALUE"],[1,2,"VALUE",3,4]], execute(InputStream(program)))

    def test_too_many_arguments(self):
        program = """
                        funko thisIsAFunction(a,b){
                                return a + b;
                        }
                        
                        a = 6;
                        c = 10;
                        thisIsAFunction(a,thisIsAFunction(a,c),c);
                            
                    """

        with self.assertRaises(RuntimeException) as e:
           execute(InputStream(program))

        self.assertEqual("TooManyArgumentsException line 8:  Too many arguments  ['a', 'thisIsAFunction(a,c)', 'c'] in function thisIsAFunction",
                      e.exception.get_message())

    def test_missing_arguments(self):
        program = """
                           funko thisIsAFunction(a,b){
                                   return a + b;
                           }

                           a = 6;
                           c = 10;
                           thisIsAFunction(c);

                       """

        with self.assertRaises(RuntimeException) as e:
            execute(InputStream(program))

        self.assertEqual(
            "ArgumentsMissingException line 8:  Missing arguments  ['b'] in function thisIsAFunction",
            e.exception.get_message())

    def test_division_by_zero(self):
        program = """ 7/0;"""

        with self.assertRaises(RuntimeException) as e:
             execute(InputStream(program))

        self.assertEqual(
            "DivisionByZeroException line 1: Division by 0",
            e.exception.get_message())

    def test_duplicated_parameters(self):
        program = """ funko thisIsAFunction(param,param){
                       
                        }
                  """

        with self.assertRaises(ConfProlSyntaxError) as e:
            execute(InputStream(program))

        self.assertEqual(
            "SyntaxException in line 1:1 Duplicated parameter {'param'} in function thisIsAFunction",
            e.exception.get_message())


    def test_function_not_defined(self):
        program = """ return pipo();"""

        with self.assertRaises(RuntimeException) as e:
            execute(InputStream(program))

        self.assertEqual(
            "FunctionNotDefinedException line 1: Function pipo not defined",
            e.exception.get_message())

    def test_method_not_define(self):
        program = """ a = 3;
                      a.platypus();"""

        with self.assertRaises(RuntimeException) as e:
            execute(InputStream(program))

        self.assertEqual(
          "MethodNotDefinedException line 2: Object a has no method platypus.",
            e.exception.get_message())



    def test_function_not_callable(self):
        program = """ a = 3;
                      a();"""

        with self.assertRaises(RuntimeException) as e:
            execute(InputStream(program))

        self.assertEqual(
            "NotCallableException line 2: The variable a is not callable.",
            e.exception.get_message())

    def test_method_not_callable(self):
        program = """ a=3;
                      a.b = 3;
                      a.b();"""

        with self.assertRaises(RuntimeException) as e:
            execute(InputStream(program))

        self.assertEqual(
            "NotCallableException line 3: The variable 3 is not callable.",
            e.exception.get_message())


    def test_operation_not_supported(self):
        program = """ return "string" * 5;"""
        with self.assertRaises(RuntimeException) as e:
            execute(InputStream(program))

        self.assertEqual(
            "OperationNotSupportedException line 1: Operation * can't be applied to ValueType.STRING and ValueType.NUMBER",
            e.exception.get_message())

    def test_variable_not_defined(self):
        program = """ return a;"""
        with self.assertRaises(RuntimeException) as e:
            execute(InputStream(program))

        self.assertEqual(
            "VariableNotDefinedException line 1: The variable a is not defined.",
            e.exception.get_message())

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
if __name__ == '__main__':
    unittest.main()
