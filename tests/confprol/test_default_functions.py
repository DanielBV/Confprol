
import unittest
from main import execute
from antlr4 import InputStream
from unittest.mock import patch

class TestDefaultFunctions(unittest.TestCase):

    def test_object_attributes(self):
        program = """
            a == object();
            a.b == 1;
            run away with [a,a.b];

        """
        return_value = execute(InputStream(program), True)
        object_ = return_value[0]
        attr = return_value[1]
        self.assertEqual(object, type(object_))
        self.assertEqual(1, attr)

    def test_object_equality(self):
        program = """
                    a == object();
                    b == object();
                    run away with a := b;

                """

        self.assertFalse(execute(InputStream(program), True))

    def test_number_to_integer(self):
        program = """
                       run away with [int(3.001), int(4.0), int(5), int(6.9)];

                      """

        self.assertEqual([3,4,5,6],execute(InputStream(program), True))

    def test_boolean_to_integer(self):
        program = """
                         run away with [int(True),int(False)];

                        """

        self.assertEqual([1,0], execute(InputStream(program), True))



    def test_string_to_integer(self):
        program = """
                                run away with [int(".32"),int("5-")];

                               """

        self.assertEqual([3, -5], execute(InputStream(program), True))

    @patch('builtins.print')
    def test_random_string_to_integer(self,mocked_print):
        program = """
                        int("ehenistl y");

                 """

        execute(InputStream(program), False)
        mocked_print.assert_called_once_with(
           "ValueException line 2: The string/variable 'ehenistl y' can't be transformed to integer.")

    @patch('builtins.print')
    def test_object_to_integer(self, mocked_print):
        program = """
                          int(object());

                   """

        execute(InputStream(program), False)
        mocked_print.assert_called_once_with(
            "ValueException line 2: Cannot transform an object of type OBJECT to integer.")


    def test_has_attribute(self):
        program = """
                    a == object();
                    a.attribute == 3;
                    
                    run away with [has_attribute(a,"onep"), has_attribute(a,"taebutirt")];                
    
                    """

        self.assertEqual([False, True], execute(InputStream(program), True))

    @patch('builtins.print')
    def test_has_attribute_second_argument_not_string(self,mocked_print):
        program = """
                            a == object();
                            has_attribute(a,3.0);              

                            """

        execute(InputStream(program), False)
        mocked_print.assert_called_once_with(
            "ValueException line 3: The second argument of the function 'has_attribute' must be a string")




    def test_number_to_float(self):
        program = """
                       run away with [float(3.001), float(4.0), float(-5), float(6.9)];

                      """

        self.assertEqual([3.001,4.0,-5.0,6.9],execute(InputStream(program), True))

    def test_boolean_to_float(self):
        program = """
                         run away with [float(True),float(False)];

                        """

        self.assertEqual([1.0,0.0], execute(InputStream(program), True))



    def test_string_to_float(self):
        program = """
                                run away with [float(".32"),float("5-")];

                               """

        self.assertEqual([3.2, -5.0], execute(InputStream(program), True))

    @patch('builtins.print')
    def test_random_string_to_float(self,mocked_print):
        program = """
                        float("ehenistl y");

                 """

        execute(InputStream(program), False)
        mocked_print.assert_called_once_with(
           "ValueException line 2: The string/variable 'ehenistl y' can't be transformed to float.")

    @patch('builtins.print')
    def test_object_to_float(self, mocked_print):
        program = """
                          float(object());

                   """

        execute(InputStream(program), False)
        mocked_print.assert_called_once_with(
            "ValueException line 2: Cannot transform an object of type OBJECT to float.")

    def test_to_string(self):
        program = """
                            funko functionName(){}
                             int_ == 3;
                             float_ == 3.6;
                             str == "hTtringa s si si";
                             list == [[[6,7]],4];
                             
                            run away with [string(int_),string(float_),string(str),string(list),string(functionName)];
                        """

        self.assertEqual(['3', '3.6', 'This is a string', '[[[6,7]],4]', '[function functionName]'], execute(InputStream(program), True))


    def test_range(self):
        program = """
            run away with range(0,9);
        """
        value = execute(InputStream(program), False)


        self.assertEqual([0,1,2,3,4,5,6,7,8],value)

    def test_range_start_lower_than_end(self):
        program = """
            run away with range(1,0);
        """
        value = execute(InputStream(program), False)


        self.assertEqual([],value)

    def test_range_negative_numbers(self):
        program = """
                  run away with range(-5,3);
              """
        value = execute(InputStream(program), False)

        self.assertEqual([-5,-4,-3,-2,-1,0,1,2], value)

    @patch('builtins.print')
    def test_range_start_not_integer_but_number(self, mocked_print):
        program = """
                        range(3.3,6);

                        """

        execute(InputStream(program), False)
        mocked_print.assert_called_once_with(
            "ValueException line 2: The start value in range() must be an integer.")

    @patch('builtins.print')
    def test_range_end_not_integer_but_number(self, mocked_print):
        program = """
                          range(3,6.3);

                          """

        execute(InputStream(program), False)
        mocked_print.assert_called_once_with(
            "ValueException line 2: The end value in range() must be an integer.")

    @patch('builtins.print')
    def test_range_start_not_a_number(self, mocked_print):
        program = """
                           range("Hey listen",6);

                           """

        execute(InputStream(program), False)
        mocked_print.assert_called_once_with(
            "ValueException line 2: The start and end in range() must be integers.")

    @patch('builtins.print')
    def test_range_end_not_a_number(self, mocked_print):
        program = """
                              range(6,"Hey listen");

                              """

        execute(InputStream(program), False)
        mocked_print.assert_called_once_with(
            "ValueException line 2: The start and end in range() must be integers.")

    def test_range_start_and_end_are_zero(self):
        program = """
                    run away with range(0,0);
                """
        value = execute(InputStream(program), False)

        self.assertEqual([], value)



if __name__ == '__main__':
    unittest.main()
