import unittest
from src.expressions.operations import TypeOperations
from src.expressions.expression import Expression
from src.type import ValueType
from src.exceptions import OperationNotSupported, DivisionByZero

class TestOperations(unittest.TestCase):

    def setUp(self):
        self.number1 = Expression(3,3,ValueType.NUMBER)
        self.number2 = Expression(5, 5, ValueType.NUMBER)
        self.boolean_true = Expression(True, True, ValueType.BOOLEAN)
        self.boolean_false = Expression(False, False, ValueType.BOOLEAN)
        self.string1 = Expression("firstString", "firstString", ValueType.STRING)
        self.string2 = Expression("secondString","secondString", ValueType.STRING)

    def test_plus_two_numbers(self):
        expr = TypeOperations.plus(self.number1,self.number2)
        self.assertEqual(8,expr.value)
        self.assertEqual("3 + 5", expr.name)

    def test_plus_number_boolean(self):
        expr = TypeOperations.plus(self.number1, self.boolean_true)
        self.assertEqual(4,expr.value)
        self.assertEqual("3 + True",expr.name)

        expr2 = TypeOperations.plus(self.boolean_false, self.number1)
        self.assertEqual(3, expr2.value)
        self.assertEqual("False + 3", expr2.name)

    def test_plus_number_string(self):
        expr = TypeOperations.plus(self.number1, self.string1)
        self.assertEqual("3firstString", expr.value)
        self.assertEqual("3 + firstString", expr.name)

        expr = TypeOperations.plus(self.string1, self.number1)
        self.assertEqual("firstString3", expr.value)
        self.assertEqual("firstString + 3", expr.name)

    def test_plus_two_booleans(self):
        expr = TypeOperations.plus(self.boolean_true, self.boolean_false)
        self.assertEqual(1, expr.value)
        self.assertEqual("True + False", expr.name)

    def test_plus_boolean_string(self):
        expr = TypeOperations.plus(self.string1, self.boolean_false)
        self.assertEqual("firstStringFalse", expr.value)
        self.assertEqual("firstString + False", expr.name)

        expr2 = TypeOperations.plus(self.boolean_true, self.string1)
        self.assertEqual("TruefirstString", expr2.value)
        self.assertEqual("True + firstString", expr2.name)

    def test_plus_two_string(self):
        expr = TypeOperations.plus(self.string1, self.string2)
        self.assertEqual("firstStringsecondString", expr.value)
        self.assertEqual("firstString + secondString", expr.name)

        expr2 = TypeOperations.plus(self.string2, self.string1)
        self.assertEqual("secondStringfirstString", expr2.value)
        self.assertEqual("secondString + firstString", expr2.name)

    def test_plus_second_argument_not_expression(self):
        with self.assertRaises(AttributeError):
            TypeOperations.plus(3,self.string2)

    def test_plus_first_argument_not_expression(self):
        with self.assertRaises(AttributeError):
            TypeOperations.plus(self.string2,3)






    def test_mult_two_numbers(self):
        expr = TypeOperations.mult(self.number1,self.number2)

        self.assertEqual(15, expr.value)
        self.assertEqual("3 * 5", expr.name)

    def test_mult_number_boolean(self):
        expr = TypeOperations.mult(self.number1, self.boolean_true)
        self.assertEqual(3, expr.value)
        self.assertEqual("3 * True", expr.name)

        expr2 = TypeOperations.mult(self.boolean_false, self.number1)
        self.assertEqual(0, expr2.value)
        self.assertEqual("False * 3", expr2.name)

    def test_mult_number_string(self):
        with self.assertRaises(OperationNotSupported):
            TypeOperations.mult(self.number1,self.string1)

        with self.assertRaises(OperationNotSupported):
            TypeOperations.mult(self.string2,self.number1)

    def test_mult_two_booleans(self):
        expr = TypeOperations.mult(self.boolean_true, self.boolean_true)
        self.assertEqual(1, expr.value)
        self.assertEqual("True * True", expr.name)

        expr2 = TypeOperations.mult(self.boolean_true, self.boolean_false)
        self.assertEqual(0, expr2.value)
        self.assertEqual("True * False", expr2.name)

    def test_mult_string_boolean(self):
        with self.assertRaises(OperationNotSupported):
            TypeOperations.mult(self.boolean_true, self.string1)

        with self.assertRaises(OperationNotSupported):
            TypeOperations.mult(self.string2, self.boolean_false)

    def test_mult_two_string(self):
        with self.assertRaises(OperationNotSupported):
            TypeOperations.mult(self.string2, self.string1)

    def test_mult_second_argument_not_expression(self):
        with self.assertRaises(AttributeError):
            TypeOperations.mult(3, self.string2)

    def test_mult_first_argument_not_expression(self):
        with self.assertRaises(AttributeError):
            TypeOperations.mult(self.string2, 3)







    def test_div_two_numbers(self):
        expr = TypeOperations.div(self.number1,self.number2)

        self.assertEqual(3/5, expr.value,0.00000001)
        self.assertEqual("3 / 5", expr.name)

    def test_div_by_0(self):
        zero = Expression(0,0,ValueType.NUMBER)
        with self.assertRaises(DivisionByZero):
            TypeOperations.div(self.number1,zero)


    def test_div_number_boolean(self):
        expr = TypeOperations.div(self.number1, self.boolean_true)
        self.assertEqual(3, expr.value)
        self.assertEqual("3 / True", expr.name)

        expr2 = TypeOperations.div(self.boolean_false, self.number1)
        self.assertEqual(0, expr2.value)
        self.assertEqual("False / 3", expr2.name)

    def test_div_number_string(self):
        with self.assertRaises(OperationNotSupported):
            TypeOperations.div(self.number1,self.string1)

        with self.assertRaises(OperationNotSupported):
            TypeOperations.div(self.string2,self.number1)

    def test_div_two_booleans(self):
        expr = TypeOperations.div(self.boolean_true, self.boolean_true)
        self.assertEqual(1, expr.value)
        self.assertEqual("True / True", expr.name)

        expr2 = TypeOperations.div(self.boolean_false, self.boolean_true)
        self.assertEqual(0, expr2.value)
        self.assertEqual("False / True", expr2.name)

    def test_div_string_boolean(self):
        with self.assertRaises(OperationNotSupported):
            TypeOperations.div(self.boolean_true, self.string1)

        with self.assertRaises(OperationNotSupported):
            TypeOperations.div(self.string2, self.boolean_false)

    def test_div_two_string(self):
        with self.assertRaises(OperationNotSupported):
            TypeOperations.div(self.string2, self.string1)

    def test_div_second_argument_not_expression(self):
        with self.assertRaises(AttributeError):
            TypeOperations.div(3, self.string2)

    def test_div_first_argument_not_expression(self):
        with self.assertRaises(AttributeError):
            TypeOperations.div(self.string2, 3)








    def test_minus_two_numbers(self):
        expr = TypeOperations.minus(self.number1,self.number2)

        self.assertEqual(-2, expr.value)
        self.assertEqual("3 - 5", expr.name)



    def test_minus_number_boolean(self):
        expr = TypeOperations.minus(self.number1, self.boolean_true)
        self.assertEqual(2, expr.value)
        self.assertEqual("3 - True", expr.name)

        expr2 = TypeOperations.minus(self.boolean_false, self.number1)
        self.assertEqual(-3, expr2.value)
        self.assertEqual("False - 3", expr2.name)

    def test_minus_number_string(self):
        with self.assertRaises(OperationNotSupported):
            TypeOperations.minus(self.number1,self.string1)

        with self.assertRaises(OperationNotSupported):
            TypeOperations.minus(self.string2,self.number1)

    def test_minus_two_booleans(self):
        expr = TypeOperations.minus(self.boolean_true, self.boolean_true)
        self.assertEqual(0, expr.value)
        self.assertEqual("True - True", expr.name)

        expr2 = TypeOperations.minus(self.boolean_false, self.boolean_true)
        self.assertEqual(-1, expr2.value)
        self.assertEqual("False - True", expr2.name)

    def test_minus_string_boolean(self):
        with self.assertRaises(OperationNotSupported):
            TypeOperations.div(self.boolean_true, self.string1)

        with self.assertRaises(OperationNotSupported):
            TypeOperations.div(self.string2, self.boolean_false)

    def test_minus_two_string(self):
        with self.assertRaises(OperationNotSupported):
            TypeOperations.minus(self.string2, self.string1)

    def test_minus_second_argument_not_expression(self):
        with self.assertRaises(AttributeError):
            TypeOperations.minus(3, self.string2)

    def test_minus_first_argument_not_expression(self):
        with self.assertRaises(AttributeError):
            TypeOperations.minus(self.string2, 3)







    def test_equal_two_numbers(self):
        expr = TypeOperations.equals(self.number1,self.number2)

        self.assertFalse(expr.value)
        self.assertEqual("3 == 5", expr.name)

        expr2 = TypeOperations.equals(self.number1,self.number1)
        self.assertTrue(expr2.value)

    def test_equal_number_boolean(self):
        expr = TypeOperations.equals(self.number1, self.boolean_true)
        self.assertFalse(expr.value)
        self.assertEqual("3 == True", expr.name)

        zero = Expression(0,0,ValueType.NUMBER)
        expr2 = TypeOperations.equals(self.boolean_false, zero)
        self.assertTrue(expr2.value)
        self.assertEqual("False == 0", expr2.name)

    def test_equal_number_string(self):
        three_str = Expression("3","3",ValueType.STRING)
        expr = TypeOperations.equals(self.number1,three_str)
        self.assertFalse(expr.value)
        self.assertEqual("3 == 3", expr.name)

        expr2 = TypeOperations.equals(self.string1,self.number2)
        self.assertFalse(expr2.value)
        self.assertEqual("firstString == 5", expr2.name)

    def test_equal_two_booleans(self):
        expr = TypeOperations.equals(self.boolean_true, self.boolean_true)
        self.assertTrue(expr.value)
        self.assertEqual("True == True", expr.name)

        expr2 = TypeOperations.equals(self.boolean_false, self.boolean_true)
        self.assertFalse(expr2.value)
        self.assertEqual("False == True", expr2.name)

    def test_equals_string_boolean(self):
        expr = TypeOperations.equals(self.string1, self.boolean_true)
        self.assertFalse(expr.value)
        self.assertEqual("firstString == True", expr.name)

        expr2 = TypeOperations.equals(self.boolean_false, self.string1)
        self.assertFalse(expr2.value)
        self.assertEqual("False == firstString", expr2.name)

    def test_equals_two_string(self):
        expr = TypeOperations.equals(self.string1,self.string1)
        self.assertTrue(expr.value)
        self.assertEqual("firstString == firstString", expr.name)

        expr2 = TypeOperations.equals(self.string2, self.string1)
        self.assertFalse(expr2.value)
        self.assertEqual("secondString == firstString", expr2.name)

    def test_equals_second_argument_not_expression(self):
        with self.assertRaises(AttributeError):
            TypeOperations.div(3, self.string2)

    def test_equals_first_argument_not_expression(self):
        with self.assertRaises(AttributeError):
            TypeOperations.div(self.string2, 3)




    #TODO Test division /0

if __name__ == '__main__':
    unittest.main()
