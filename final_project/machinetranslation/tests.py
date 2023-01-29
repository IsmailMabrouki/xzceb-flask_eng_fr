import unittest
import translator as tr

class testenglish_french(unittest.TestCase):
    def test_en_fr(self):
        self.assertEqual(tr.english_to_french(None), "")
        self.assertEqual(tr.english_to_french('Hello'),"Bonjour")


class testfrench_english(unittest.TestCase):
    def test_fr_en(self):
        self.assertEqual(tr.french_to_english(None), "")
        self.assertEqual(tr.french_to_english("Bonjour"),"Hello")

unittest.main()