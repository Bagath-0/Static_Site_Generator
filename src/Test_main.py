import unittest

from main import extract_title


class TestBlockToBlockType(unittest.TestCase):
    def test_H1(self):
        md = """
        #  This is a title.


this is not"""

        title = extract_title(md)
        self.assertEqual(title,"This is a title.")
    
if __name__ == "__main__":
     unittest.main()