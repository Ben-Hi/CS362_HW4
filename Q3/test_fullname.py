import fullname
import unittest

class Test_TestFullname(unittest.TestCase):
    def test_string_int(self):
        with self.assertRaises(TypeError):
            fullname.fullname("first", 1)

    def test_string_bool(self):
        with self.assertRaises(TypeError):
            fullname.fullname("first", True)

    def test_empty_strings(self):
        with self.assertRaises(TypeError):
            fullname.fullname("", "")