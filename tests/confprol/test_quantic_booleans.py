import unittest

from src.expressions.booleans.quantic_axis import QuanticAxis
from src.main import execute
from antlr4 import InputStream
from src.expressions.booleans.quantic_boolean import QuanticBoolean

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
        self.assertTrue(result)

    @patch('random.randint')
    def test_evaluate_x_different_axis_false(self, mocked_random):
        mocked_random.return_value = 1
        program = """
                      run away with evalX(yTrue);
                      """

        result = execute(InputStream(program), False)

        mocked_random.assert_called_once()
        self.assertFalse(result)

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
        self.assertFalse(result)


    def test_evaluate_in_other_axis_changes_the_axis_x_axis(self):
        boolean = QuanticBoolean(QuanticAxis.X,True)

        value = boolean.evaluate(QuanticAxis.Y).value

        self.assertEqual(QuanticAxis.Y, boolean.object.axis)
        self.assertEqual(value, boolean.evaluate(QuanticAxis.Y).value)

    def test_evaluate_in_other_axis_changes_the_axis_y_axis(self):
        boolean = QuanticBoolean(QuanticAxis.Y, True)

        value = boolean.evaluate(QuanticAxis.X).value

        self.assertEqual(QuanticAxis.X, boolean.object.axis)
        self.assertEqual(value, boolean.evaluate(QuanticAxis.X).value)


    def test_return_quantic_boolean(self):
        program = """
                    run away with xTrue;
                  """

        result = execute(InputStream(program), False)

        self.assertIsNotNone(result)
        self.assertTrue(result.value)



    def test_quantic_boolean_attributes_x_axis(self):
        program = """
                     a == xTrue;
                     a.a == 3;
                     b == xTrue;
                     c == xFalse;
                     c.c == 6;
                     d == xFalse;
                     run away with [a.a,has_attribute(b,"a"),c.c,has_attribute(d,"c")];
                  """

        result = execute(InputStream(program), False)

        self.assertEqual([3, False,6,False], result)

    def test_quantic_boolean_attributes_y_axis(self):
        program = """
                        a == yTrue;
                        a.a == 3;
                        b == yTrue;
                        c == yFalse;
                        c.c == 6;
                        d == yFalse;
                        run away with [a.a,has_attribute(b,"a"),c.c,has_attribute(d,"c")];
                     """

        result = execute(InputStream(program), False)

        self.assertEqual([3, False, 6, False], result)