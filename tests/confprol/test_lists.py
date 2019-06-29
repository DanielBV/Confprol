import unittest
from src.main import execute
from antlr4 import InputStream


from unittest.mock import patch

class TestLists(unittest.TestCase):

    @patch('builtins.print')
    def test_list_remove_not_contained(self, mocked_print):
        program = """
                          e = [];
                          e.remove(9);
                          return e;
                   """
        execute(InputStream(program), False)

        mocked_print.assert_called_once_with(
            "ElementNotContainedException line 3: The list e doesn't contain 9")

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
        self.assertEqual([2, 4, [3, 4]], execute(InputStream(program)))

    def test_list_remove(self):
        program = """
                           e = [3,4,5,3,6];
                           e.remove(3);
                           return [e,e.length()];
                       """
        self.assertEqual([[4, 5, 3, 6], 4], execute(InputStream(program)))

    def test_list_insert(self):
        program = """
                               e = [];
                               e.insert(3,"VALUE");
                               f = [1,2,3,4];
                               f.insert(2,"VALUE");
                               return [e,f];
                        """
        self.assertEqual([["VALUE"], [1, 2, "VALUE", 3, 4]], execute(InputStream(program)))

    def test_list_attributes(self):
        program = """
                     list = [3,4];
                     list.attr = 99;
                     return list.attr;
                     
                               """
        self.assertEqual(99, execute(InputStream(program)))


if __name__ == '__main__':
    unittest.main()
