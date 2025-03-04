import unittest

from extract_urls import *
def setUp(self):
    text1 = "Here is an image ![alt1](url1) and another ![alt2](url2)."
    # Expected: [("alt1", "url1"), ("alt2", "url2")]
    text2 = "This text has no valid markdown in it."
    # Expected: Exception with "No valid markdown found"
    text3 = "This is a broken markdown ![alt1](url1) and here is ![alt2]."
    # Expected: Exception with "Mismatch between alt texts and URLs"
    text4 = "Another broken case: ![alt1 some text still no url"
  # Expected: Exception with "Mismatch between alt texts and URLs"
    text5 = "Valid: ![alt1](url1) Invalid: ![alt_missing_url]. Another valid ![alt2](url2)."
        # Expected: [("alt1", "url1"), ("alt2", "url2")]
    text6 = "Empty alt: ![](url1). Empty URL: ![alt2]()."
        # Expected: [("", "url1"), ("alt2", "")]

    
    def test_extract_markdown_images(text1):
        expected_output = [("alt1", "url1"), ("alt2", "url2")]
        actual_output = extract_markdown_images(text1)
        self.assertEqual(actual_output, expected_output)

    def test_no_markdown_found(self):
       with self.assertRaises(Exception):
            text2 = "This text has no valid markdown in it."
            extract_markdown_images(text2)

    def testempty (text5):
        expected = [("", "url1"), ("alt2", "")]
        actual = extract_markdown_images(text5)
        self.assertEqual(actual, expected)


        



if __name__ == "__main__":
    unittest.main()