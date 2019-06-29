import unittest
from src.main import execute
from antlr4 import InputStream


from unittest.mock import patch, MagicMock



class TestMessages(unittest.TestCase):

    @patch('builtins.print')
    def test_function_not_callable(self,mocked_print):
        program = """ a = 3;
                         a();"""


        execute(InputStream(program), False)

        mocked_print.assert_called_once_with(
            "NotCallableException line 2: The variable a is not callable.")


    @patch('builtins.print')
    def test_message_prints_full_method_and_attribute_path(self, mocked_print: MagicMock):
        program = """funko pop(){}
                            a = 3;
                            a.a = 6;
                            a.a.list = [[[0]]];

                            pop(a.a.list.get(0).get(0).get(0));

                """

        execute(InputStream(program), False)
        mocked_print.assert_called_once_with(
            "TooManyArgumentsException line 6:  Too many arguments  ['get(get(get(a.a.list,0),0),0)'] in function pop")

    @patch('builtins.print')
    def test_message_prints_full_attribute_path(self, mocked_print: MagicMock):
        program = """funko pop(){}
                            a = 0;
                            a.a = 0;
                            a.a.a = 0;
                            a.a.a.a = 0;
                            a.a.a.a.b = 0;
                            a.a.a.a.b.attribute = 3;
                            pop(a.a.a.a.b.attribute);

                """

        execute(InputStream(program), False)
        mocked_print.assert_called_once_with(
            "TooManyArgumentsException line 8:  Too many arguments  ['a.a.a.a.b.attribute'] in function pop")



    @patch('builtins.print')
    def test_message_to_many_arguments_function_call(self, mocked_print: MagicMock):
        program = """funko pop(){}
                      b = 3;
                      c = b;
                      a = [c,4,5,6];
                      pop(a.get(0));
          """

        execute(InputStream(program), False)
        mocked_print.assert_called_once_with(
            "TooManyArgumentsException line 5:  Too many arguments  ['get(a,0)'] in function pop")

    @patch('builtins.print')
    def test_message_prints_right_variable_name(self, mocked_print: MagicMock):
        program = """funko pop(){}
                                  b = 3;
                                  c = b;
                                  pop(c);

                      """

        execute(InputStream(program), False)
        mocked_print.assert_called_once_with(
            "TooManyArgumentsException line 4:  Too many arguments  ['c'] in function pop")

    @patch('builtins.print')
    def test_method_not_defined(self,mocked_print):
        program = """ a = 3;
                      a.platypus();"""

        execute(InputStream(program), False)
        mocked_print.assert_called_once_with(
            "AttributeNotDefinedException line 2: Object a of type NUMBER doesn't have an attribute platypus.")

    @patch('builtins.print')
    def test_operation_not_supported(self,mocked_print):
        program = """ return "string" * 5;"""

        execute(InputStream(program), False)

        mocked_print.assert_called_once_with(
            "OperationNotSupportedException line 1: Operation * can't be applied to STRING and NUMBER")

    @patch('builtins.print')
    def test_variable_not_defined(self,mocked_print):
        program = """ return a;"""
        execute(InputStream(program), False)

        mocked_print.assert_called_once_with(
            "VariableNotDefinedException line 1: The variable a is not defined.")

    @patch('builtins.print')
    def test_method_not_callable(self, mocked_print):
        program = """ a=3;
                         a.b = 3;
                         a.b();"""

        execute(InputStream(program), False)

        mocked_print.assert_called_once_with(
            "NotCallableException line 3: The variable a.b is not callable.")

    @patch('builtins.print')
    def test_function_not_defined(self, mocked_print):
        program = """ return pipo();"""

        execute(InputStream(program), False)

        mocked_print.assert_called_once_with(
            "FunctionNotDefinedException line 1: Function pipo not defined.")

    @patch('builtins.print')
    def test_duplicated_parameters(self, mocked_print):
        program = """ funko thisIsAFunction(param,param){

                        }
                  """

        execute(InputStream(program), False)

        mocked_print.assert_called_once_with(
            "SyntaxException in line 1:1 Duplicated parameter {'param'} in function thisIsAFunction.")

    @patch('builtins.print')
    def test_division_by_zero(self, mocked_print):
        program = """ 7/0;"""

        execute(InputStream(program), False)

        mocked_print.assert_called_once_with(
            "DivisionByZeroException line 1: Division by 0")

    @patch('builtins.print')
    def test_missing_arguments(self, mocked_print):
        program = """
                            funko thisIsAFunction(a,b){
                                    return a + b;
                            }

                            a = 6;
                            c = 10;
                            thisIsAFunction(c);

                        """

        execute(InputStream(program), False)

        mocked_print.assert_called_once_with(
            "ArgumentsMissingException line 8:  Missing arguments  ['b'] in function thisIsAFunction")

    @patch('builtins.print')
    def test_missing_semicolon(self, mocked_print):
        program = """ return "string" + 5"""

        execute(InputStream(program), False)

        mocked_print.assert_called_once_with(
            "SyntaxException in line 1:20 missing ';' at '<EOF>'")
