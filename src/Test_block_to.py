import unittest

from Block_to_type import *


class TestBlockToBlockType(unittest.TestCase):
    
    def test_paragraph(self):
        """Test normal paragraph blocks"""
        text = "This is a regular paragraph."
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
        
        # Test with multiple lines
        text = "This is a paragraph\nwith multiple lines."
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
    
    def test_heading(self):
        """Test heading blocks"""
        # Test different heading levels
        for i in range(1, 7):
            text = "#" * i + " Heading level " + str(i)
            self.assertEqual(block_to_block_type(text), BlockType.HEADING)
        
        # Test invalid heading (no space after #)
        text = "#This is not a valid heading"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
        
        # Test too many #s
        text = "#######" + " Too many"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
    
    def test_code(self):
        """Test code blocks"""
        text = "```\nCode goes here\n```"
        self.assertEqual(block_to_block_type(text), BlockType.CODE)
        
        # Test without closing backticks
        text = "```\nCode without closing"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
    
    def test_quote(self):
        """Test quote blocks"""
        text = ">This is a quote"
        self.assertEqual(block_to_block_type(text), BlockType.QUOTE)
        
        # Test with multiple lines
        text = ">Line 1\n>Line 2\n>Line 3"
        self.assertEqual(block_to_block_type(text), BlockType.QUOTE)
        
        # Test with a line that doesn't start with >
        text = ">Line 1\nLine 2\n>Line 3"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)

    def test_unordered_list(self):
        """Test unordered list blocks"""
        text = "- Item 1"
        self.assertEqual(block_to_block_type(text), BlockType.UNORDERED_LIST)
        
        # Test with multiple items
        text = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(text), BlockType.UNORDERED_LIST)
        
        # Test with a line that doesn't start with -
        text = "- Item 1\nNot an item\n- Item 3"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
        
        # Test without space after dash
        text = "-Item 1"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)

    def test_ordered_list(self):
        """Test ordered list blocks"""
        text = "1. Item 1"
        self.assertEqual(block_to_block_type(text), BlockType.ORDERED_LIST)
        
        # Test with multiple items
        text = "1. Item 1\n2. Item 2\n3. Item 3"
        self.assertEqual(block_to_block_type(text), BlockType.ORDERED_LIST)
        
        # Test with incorrect ordering
        text = "1. Item 1\n3. Item 3\n2. Item 2"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
        
        # Test with a line that doesn't follow ordered pattern
        text = "1. Item 1\nNot an item\n3. Item 3"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
        
        # Test without space after number + period
        text = "1.Item 1"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)    
            
if __name__ == "__main__":
     unittest.main()