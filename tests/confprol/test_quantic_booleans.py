import unittest
from src.main import execute
from antlr4 import InputStream


from unittest.mock import patch



class TestQuanticBooleans(unittest.TestCase):

    @patch('builtins.print')
    def test_evaluate_quantic_boolean_in_condition(self,mocked_print):
        program = """ 
                    if not xTrue{
                        run away with 6;
                    }"""


        execute(InputStream(program), False)

        mocked_print.assert_called_once_with(
            "EvaluateQuanticBooleanException line 2: Quantic booleans can't be evaluated or operated as regular booleans. Use evalX() or evalY() to evaluate them first.")

    @patch('builtins.print')
    def test_multiply_quantic_boolean(self, mocked_print):
        program = """ 
                  run away with 3 * xFalse;
                  """

        execute(InputStream(program), False)

        mocked_print.assert_called_once_with(
            "EvaluateQuanticBooleanException line 2: Quantic booleans can't be evaluated or operated as regular booleans. Use evalX() or evalY() to evaluate them first.")


    @patch('builtins.print')
    def test_sum_quantic_boolean(self, mocked_print):
        program = """ 
                  run away with 3 + xFalse;
                  """

        execute(InputStream(program), False)

        mocked_print.assert_called_once_with(
            "EvaluateQuanticBooleanException line 2: Quantic booleans can't be evaluated or operated as regular booleans. Use evalX() or evalY() to evaluate them first.")

    @patch('builtins.print')
    def test_divide_quantic_boolean(self, mocked_print):
        program = """ 
                     run away with 3 / xFalse;
                     """

        execute(InputStream(program), False)

        mocked_print.assert_called_once_with(
            "EvaluateQuanticBooleanException line 2: Quantic booleans can't be evaluated or operated as regular booleans. Use evalX() or evalY() to evaluate them first.")

    @patch('builtins.print')
    def test_minus_quantic_boolean(self, mocked_print):
        program = """ 
                     run away with 3 - xFalse;
                     """

        execute(InputStream(program), False)

        mocked_print.assert_called_once_with(
            "EvaluateQuanticBooleanException line 2: Quantic booleans can't be evaluated or operated as regular booleans. Use evalX() or evalY() to evaluate them first.")

    @patch('builtins.print')
    def test_equals_quantic_boolean(self, mocked_print):
        program = """ 
                     run away with xTrue := xFalse;
                     """

        execute(InputStream(program), False)

        mocked_print.assert_called_once_with(
            "EvaluateQuanticBooleanException line 2: Quantic booleans can't be evaluated or operated as regular booleans. Use evalX() or evalY() to evaluate them first.")

    @patch('builtins.print')
    def test_quantic_boolean_to_int(self, mocked_print):
        program = """ 
                      int(yTrue);"""

        execute(InputStream(program), False)

        mocked_print.assert_called_once_with(
            "EvaluateQuanticBooleanException line 2: Quantic booleans can't be evaluated or operated as regular booleans. Use evalX() or evalY() to evaluate them first.")

    @patch('builtins.print')
    def test_quantic_boolean_to_float(self, mocked_print):
        program = """ 
                      float(yTrue);"""

        execute(InputStream(program), False)

        mocked_print.assert_called_once_with(
            "EvaluateQuanticBooleanException line 2: Quantic booleans can't be evaluated or operated as regular booleans. Use evalX() or evalY() to evaluate them first.")


    def test_quantic_boolean_to_string(self):
        program = """ 
                      run away with string(yFalse);"""

        string = execute(InputStream(program), True)
        self.assertIn("[Quantic Boolean",string)

    @patch('builtins.print')
    def test_evaluate_x_not_quantic_boolean(self,mocked_print):
        program = """ 
                        evalX(True);"""

        execute(InputStream(program), False)

        mocked_print.assert_called_once_with(
            "ValueException line 2: Cannot evaluate a non quantic value.")

    @patch('builtins.print')
    def test_evaluate_x_none(self, mocked_print):
        program = """ 
                         evalX(None);"""

        execute(InputStream(program), False)

        mocked_print.assert_called_once_with(
            "ValueException line 2: Cannot evaluate a non quantic value.")

    @patch('builtins.print')
    def test_evaluate_y(self,mocked_print):
        program = """ 
                        evalY(True);"""

        execute(InputStream(program), False)

        mocked_print.assert_called_once_with(
            "ValueException line 2: Cannot evaluate a non quantic value.")

    @patch('builtins.print')
    def test_evaluate_y_none(self, mocked_print):
        program = """ 
                          evalY(None);"""

        execute(InputStream(program), False)

        mocked_print.assert_called_once_with(
            "ValueException line 2: Cannot evaluate a non quantic value.")

    def test_evaluate_same_axis(self):
        program = """
            run away with [evalX(xTrue), evalX(xFalse), evalY(yTrue), evalY(yFalse)];
            """

        result = execute(InputStream(program), False)

        self.assertEqual([True,False,True,False],result)

    @patch('random.randint')
    def test_evaluate_x_different_axis_true(self, mocked_random):
        mocked_random.return_value = 6
        program = """
                    run away with evalX(yTrue);
                    """

        result = execute(InputStream(program), False)

        mocked_random.assert_called_once()
        self.assertEqual(True, result)

    @patch('random.randint')
    def test_evaluate_x_different_axis_false(self, mocked_random):
        mocked_random.return_value = 1
        program = """
                      run away with evalX(yTrue);
                      """

        result = execute(InputStream(program), False)

        mocked_random.assert_called_once()
        self.assertEqual(False, result)

    @patch('random.randint')
    def test_evaluate_y_different_axis_true(self, mocked_random):
        mocked_random.return_value = 6
        program = """
                       run away with evalY(xTrue);
                       """

        result = execute(InputStream(program), False)

        mocked_random.assert_called_once()
        self.assertEqual(True, result)

    @patch('random.randint')
    def test_evaluate_y_different_axis_false(self, mocked_random):
        mocked_random.return_value = 1
        program = """
                         run away with evalY(xTrue);
                         """

        result = execute(InputStream(program), False)

        mocked_random.assert_called_once()
        self.assertEqual(False, result)

