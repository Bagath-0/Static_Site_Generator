import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def setUp(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.node3 = TextNode("This is another text node", TextType.NORMAL)
        self.node4 = TextNode("This is another text node", TextType.BOLD)
        self.node5 = TextNode("This is another text node", TextType.IMAGES,"pics.com")
    
    def test_normal_to_html(self):
        expected_output = "This is another text node"
        New_Class = self.node3.text_node_to_html_node()
        actual_output = f"{New_Class.value}"
        self.assertEqual(actual_output, expected_output)

    def test_Bold_to_html(self):
        expected_output = '"b"This is another text node'
        New_Class = self.node4.text_node_to_html_node()
        actual_output = f"{New_Class.tag}{New_Class.value}"
        self.assertEqual(actual_output, expected_output)


        



if __name__ == "__main__":
    unittest.main()