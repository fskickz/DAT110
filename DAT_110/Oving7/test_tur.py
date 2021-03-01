import unittest
import DAT_110.Oving7.tur as tur

class TestTur(unittest.TestCase):
    def test_tur(self):
        tur1 = tur.Tur("Tur 1", 0, 5)
        tur1.add_posisjon_koordinater(2,3,2)
        tur1.add_posisjon_koordinater(20,5,20)
        tur1.add_posisjon_koordinater(18,13,22)
        tur1.add_posisjon_koordinater(2,3,2)
        self.assertEqual(40, tur1.hoydemeter())
        tur2 = tur.Tur("Tur 2", 5, 24)
        tur2.add_posisjon_koordinater(5,3,10)
        tur2.add_posisjon_koordinater(15,5,18)
        tur2.add_posisjon_koordinater(12,15,12)
        self.assertEqual(14, tur2.hoydemeter())
        self.assertTrue(tur1.er_rundtur())
        self.assertFalse(tur2.er_rundtur())
        with self.assertRaises(ValueError):
            tur.Tur("tur 3", 5, 4)
        tur3 = tur.Tur("Tur 3", 16, 18)
        tur3.add_posisjon_koordinater(1,2,3)
        tur3.add_posisjon_koordinater(1,4,9)
        tur3.add_posisjon_koordinater(2,6,12)
        tur3.add_posisjon_koordinater(1,4,6)
        self.assertEqual(15, tur3.hoydemeter())
        self.assertFalse(tur3.er_rundtur())



if __name__ == "__main__":
    unittest.main()
