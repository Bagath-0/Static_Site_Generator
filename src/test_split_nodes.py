import unittest

from split_nodes import *

class Test_split_nodes(unittest.TestCase):
    def setUp(self):
        self.text1 = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.NORMAL,)
        
        
    def test_split_link(self):
        test = self.text1
        expected_output = [TextNode("This is text with a link ", TextType.NORMAL),TextNode("to boot dev", TextType.LINKS, "https://www.boot.dev"),TextNode(" and ", TextType.NORMAL),TextNode("to youtube", TextType.LINKS, "https://www.youtube.com/@bootdotdev"),]
        actual_output = split_nodes_link([test])
        self.assertEqual(actual_output, expected_output) 

    def test_no_links(self):
        node = TextNode("Plain text without any links", TextType.NORMAL)
        result = split_nodes_link([node])
        expected = [node]  # Should return original node if no links
        self.assertEqual(result, expected)

    def test_only_link(self):
        node = TextNode("[boot.dev](https://boot.dev)", TextType.NORMAL)
        result = split_nodes_link([node])
        expected = [TextNode("boot.dev", TextType.LINKS, "https://boot.dev")]
        self.assertEqual(result, expected)                

    def test_empty_text(self):
        node = TextNode("", TextType.NORMAL)
        result = split_nodes_link([node])
        expected = [node]  # Should return original node as no links
        self.assertEqual(result, expected)

    def test_malformed_link(self):
        node = TextNode("[broken link(https://boot.dev)", TextType.NORMAL)
        with self.assertRaises(Exception):  # or whatever exception type you're raising
            split_nodes_link([node])

    def test_adjacent_links(self):
        node = TextNode("[link1](url1)[link2](url2)", TextType.NORMAL)
        expected = [
            TextNode("link1", TextType.LINKS, "url1"),
            TextNode("link2", TextType.LINKS, "url2")
        ]
        result = split_nodes_link([node])
        self.assertEqual(result, expected)

    def test_split_image(self):
        test = TextNode("Here's an image ![my image](image.jpg) in some text", TextType.NORMAL)
        expected_output = [
        TextNode("Here's an image ", TextType.NORMAL),
        TextNode("my image", TextType.IMAGES, "image.jpg"),
        TextNode(" in some text", TextType.NORMAL)
        ]
        actual_output = split_nodes_image([test])
        self.assertEqual(actual_output, expected_output)

    def test_only_image(self):
        node = TextNode("![solo image](solo.jpg)", TextType.NORMAL)
        expected = [TextNode("solo image", TextType.IMAGES, "solo.jpg")]
        result = split_nodes_image([node])
        self.assertEqual(result, expected)

    def test_empty_alt_text(self):
        node = TextNode("![](image.jpg)", TextType.NORMAL)
        expected = [TextNode("", TextType.IMAGES, "image.jpg")]
        result = split_nodes_image([node])
        self.assertEqual(result, expected)

    def test_url_with_spaces(self):
        node = TextNode("![alt text](my cool image.jpg)", TextType.NORMAL)
        expected = [TextNode("alt text", TextType.IMAGES, "my cool image.jpg")]
        result = split_nodes_image([node])
        self.assertEqual(result, expected)

    def test_sequential_images(self):
        node = TextNode("![img1](1.jpg)![img2](2.jpg)", TextType.NORMAL)
        expected = [
            TextNode("img1", TextType.IMAGES, "1.jpg"),
            TextNode("img2", TextType.IMAGES, "2.jpg")
        ]
        result = split_nodes_image([node])
        self.assertEqual(result, expected)      

    def test_empty_anchor_text(self):
        node = TextNode("[](url.com)", TextType.NORMAL)
        expected = [TextNode("", TextType.LINKS, "url.com")]
        result = split_nodes_link([node])
        self.assertEqual(result, expected)      
    
    def test_empty_anchor_text(self):
        node = TextNode("[](url.com)", TextType.NORMAL)
        expected = [TextNode("", TextType.LINKS, "url.com")]  # Corrected to LINKS
        with warnings.catch_warnings(record=True) as w:
            result = split_nodes_link([node])
            # Check that the node is created correctly
            self.assertEqual(result, expected)
            # Check that we got exactly one warning
            self.assertEqual(len(w), 1)
            # Check the warning message
            self.assertEqual(str(w[0].message), "Link created with empty anchor text")
    
    def test_text_to_textnodes_bold(self):
        # Test single bold text
        text = "This is **bold** text"
        actual = text_to_textnodes(text)
        expected =  [TextNode("This is ", TextType.NORMAL), TextNode("bold", TextType.BOLD),  TextNode(" text", TextType.NORMAL)]
        self.assertEqual(actual, expected)   

    def test_text_to_textnodes_multiple_bold(self):
        text = "This has **two** separate **bold** sections"
        actual = text_to_textnodes(text)
        expected =  [TextNode("This has ", TextType.NORMAL), TextNode("two", TextType.BOLD),  TextNode(" separate ", TextType.NORMAL), TextNode("bold", TextType.BOLD),TextNode(" sections", TextType.NORMAL)]
        self.assertEqual(actual, expected)  
    
    def test_text_to_textnodes_code(self):
        text = "Here is a `code block` example"
        actual = text_to_textnodes(text)
        expected =  [TextNode("Here is a ", TextType.NORMAL), TextNode("code block", TextType.CODE),  TextNode(" example", TextType.NORMAL)]
        self.assertEqual(actual, expected)  

    def test_markdown_to_blocks(self):
        text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        actual = markdown_to_blocks(text)
        expected = ["# This is a heading","This is a paragraph of text. It has some **bold** and *italic* words inside of it.","* This is the first list item in a list block\n* This is a list item\n* This is another list item"]
        self.assertEqual(actual, expected)  

    def test_empty_document(self):
        text = ""
        actual = markdown_to_blocks(text)
        expected = []
        self.assertEqual(actual, expected)

    def test_whitespace_only(self):
        text = "    \t    \n\n   \t   "
        actual = markdown_to_blocks(text)
        expected = []
        self.assertEqual(actual, expected)

    def test_single_block_with_newlines(self):
        text = """* First item
* Second item
* Third item"""
        
        actual = markdown_to_blocks(text)
        expected = ["* First item\n* Second item\n* Third item"]
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()