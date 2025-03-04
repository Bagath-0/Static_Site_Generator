from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(text):
    if text.startswith("#"):
    # Check if it's a valid heading (# followed by a space)
        for i in range(1, 7):
            if text.startswith("#" * i + " "):
                return BlockType.HEADING
    if text.startswith("```") and text.endswith("```"):
        return BlockType.CODE
    if block_to_helper(text,">") == True:
        return BlockType.QUOTE
    if block_to_helper(text,"-"," ") == True:
        return BlockType.UNORDERED_LIST
    if block_to_helper(text,"."," ",True) == True:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
    

def block_to_helper(text, character, follower=None, ordercheck=None):
    lines = text.split("\n")
    
    if ordercheck is None:
        # For quote, unordered list
        check_string = character if follower is None else character + follower
        for line in lines:
            if not line.startswith(check_string):
                return False
    else:
        # For ordered list
        expected_num = 1
        for line in lines:
            expected_prefix = f"{expected_num}{character}{follower}"
            if not line.startswith(expected_prefix):
                return False
            expected_num += 1
            
    return True
        