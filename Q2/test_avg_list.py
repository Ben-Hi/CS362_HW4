import avg_list
import unittest

class Test_TestAvgList(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(avg_list.avg_list([]), 0)

    def test_invalid_elements(self):
        with self.assertRaises(TypeError):
            avg_list.avg_list([1,2,"string"])

    def test_int_float(self):
        self.assertEqual(avg_list.avg_list([1,1.5,1,0.5]), 1)