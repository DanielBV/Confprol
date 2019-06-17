import unittest
from src.multimethods.multimethod import multimethod,DISPATCH_ANY


@multimethod((float,bool),(float,bool))
def add(first,second):
    return first + second

@multimethod(str,DISPATCH_ANY)
@multimethod(DISPATCH_ANY,str)
def add(first,second):
    return str(first) + str(second)

@multimethod(DISPATCH_ANY)
def add(oneParameter):
    return oneParameter


class TestMultiMethod(unittest.TestCase):

    def test_union(self):
        self.assertEqual(5, add(3.0,2.0))
        self.assertEqual(3, add(True, 2.0))
        self.assertEqual(2, add(2.0,False))
        self.assertEqual(0, add(False, False))

    def test_dispatch_any(self):
        self.assertEqual("hey listen", add("hey ", "listen"))
        self.assertEqual("3listen", add(3, "listen"))
        self.assertEqual("hey14.0", add("hey",14.0))
        self.assertEqual("heyTrue", add("hey", True))
        self.assertEqual("hey<built-in function id>", add("hey", id))
        self.assertEqual("<built-in function id>listen",add(id,"listen"))

    def test_multiple_number_of_arguments(self):
        self.assertEqual(5, add(3.0, 2.0))
        self.assertEqual(5, add(5))

    def test_more_arguments_than_expected(self):
        with self.assertRaises(TypeError):
            add("arg","arg2","arg3")

    def test_less_arguments_than_expected(self):
        with self.assertRaises(TypeError):
            add()

if __name__ == '__main__':
    unittest.main()
