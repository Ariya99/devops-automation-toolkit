import unittest
import importlib.util
import os

# Dynamically import the script because of hyphens in the filename
current_dir = os.path.dirname(os.path.abspath(__file__))
script_path = os.path.join(current_dir, "syncprocess-fails-rating8.py")
spec = importlib.util.spec_from_file_location("syncprocess", script_path)
syncprocess = importlib.util.module_from_spec(spec)
spec.loader.exec_module(syncprocess)
is_valid_csv_filename = syncprocess.is_valid_csv_filename

class TestIsValidCsvFilename(unittest.TestCase):
    def test_valid_lowercase_csv(self):
        self.assertTrue(is_valid_csv_filename("data.csv"))

    def test_valid_uppercase_csv(self):
        self.assertTrue(is_valid_csv_filename("DATA.CSV"))

    def test_valid_mixedcase_csv(self):
        self.assertTrue(is_valid_csv_filename("Data.Csv"))

    def test_invalid_extension_txt(self):
        self.assertFalse(is_valid_csv_filename("data.txt"))

    def test_invalid_extension_missing(self):
        self.assertFalse(is_valid_csv_filename("data"))
        self.assertFalse(is_valid_csv_filename("data."))

    def test_empty_string(self):
        self.assertFalse(is_valid_csv_filename(""))

    def test_csv_in_middle_of_name(self):
        self.assertFalse(is_valid_csv_filename("data.csv.txt"))

if __name__ == '__main__':
    unittest.main()
