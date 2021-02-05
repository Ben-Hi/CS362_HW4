import volume
import unittest

class Test_TestVolume(unittest.TestCase):
    def test_volume_pos_neg(self):
        self.assertEqual(volume.volume(1,-2,3), -1)
    
    def test_volume_string(self):
        with self.assertRaises(TypeError):
            volume.volume("string","string","string")

    def test_volume_pos_bool(self):
        with self.assertRaises(TypeError):
            volume.volume(1,True,False)

    