import unittest
from src.main import execute
from antlr4 import InputStream


from unittest.mock import patch

class TestLists(unittest.TestCase):

    @patch('builtins.print')
    def test_list_remove_not_contained(self, mocked_print):
        program = """
                          e == [];
                          e.remove(9);
                          run away with e;
                   """
        execute(InputStream(program), False)

        mocked_print.assert_called_once_with(
            "ElementNotContainedException line 3: The list e doesn't contain 9")

    def test_list(self):
        program = """

              e == [[6,[5,9],2],2,3,4];
              run away with  e.get(0).get(1).get(1);
          """
        self.assertEqual(9, execute(InputStream(program)))

    def test_lists_evaluate_expressions(self):
        program = """
                  funko returnFour(){
                      run away with 5; @useless_comment(The four was a lie, the cake too.)   
                  }
                    e == [6*5+4+ returnFour()];
                    run away with  e.get(0);
                """
        self.assertEqual(39, execute(InputStream(program)))

    def test_list_length(self):
        program = """
                     e == [3,[1,2,3],4];
                     run away with  e.length();
                 """
        self.assertEqual(3, execute(InputStream(program)))

    def test_list_add(self):
        program = """
                        e == [3];
                        e.append(4);
                        run away with  [e.length(),e.get(1),e];
                    """
        self.assertEqual([2, 4, [3, 4]], execute(InputStream(program)))

    def test_list_remove(self):
        program = """
                           e == [3,4,5,3,6];
                           e.remove(3);
                           run away with [e,e.length()];
                       """
        self.assertEqual([[4, 5, 3, 6], 4], execute(InputStream(program)))

    def test_list_insert(self):
        program = """
                               e == [];
                               e.insert(3,"VALUE");
                               f == [1,2,3,4];
                               f.insert(2,"VALUE");
                               run away with [e,f];
                        """
        self.assertEqual([["VALUE"], [1, 2, "VALUE", 3, 4]], execute(InputStream(program)))

    def test_list_attributes(self):
        program = """
                     list == [3,4];
                     list.attr == 99;
                     run away with list.attr;
                     
                               """
        self.assertEqual(99, execute(InputStream(program)))

    @patch('builtins.print')
    def test_list_insert_first_argument_not_integer(self,mocked_print):
        program = """
                            list == [3,4];
                            list.insert(3.1,"VALUE");
                            run away with list;

                                      """
        execute(InputStream(program))

        mocked_print.assert_called_once_with(
            "ValueException line 3: The first argument of the method 'insert' must be an integer")

    def test_list_insert_position_can_be_float_without_decimal(self):
        program = """
                                list == [3,4];
                                list.insert(1.000000000000000,"VALUE");
                                run away with list;

                                          """
        self.assertEqual([3,"VALUE",4],execute(InputStream(program)))


    def test_list_remove_with_object(self):
        program = """       
                           a == object();
                           b == object();
                           list == [];
                           list.append(a);
                           list.append(b);
                           
                           
                           run away with list.get(0) := a;
                           

                                                 """
        self.assertTrue(execute(InputStream(program),True))


if __name__ == '__main__':
    unittest.main()
