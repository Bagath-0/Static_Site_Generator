
import warnings
from Block_to_type import *

warnings.filterwarnings('always', category=UserWarning)
#split Textnodes into TextNode chunks for bold italics and code, does not allow for nested Text-types
from enum import Enum
from textnode import TextNode,TextType
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for each in old_nodes:
        match (each.text_type):
            case TextType.NORMAL:
                text = each.text
                start = text.find(delimiter)
                if start != -1:
                    end = text.find(delimiter, start + len(delimiter))
                    if end == -1:
                        raise Exception("Invalid markdown: unclosed delimiter")
                    before = TextNode(text[0:start], TextType.NORMAL)
                    middle = TextNode(text[start + len(delimiter):end], text_type)
                    after = TextNode(text[end + len(delimiter):], TextType.NORMAL)

                    nodes_to_add = []
                    if len(before.text) > 0:
                        nodes_to_add.append(before)
                    if len(middle.text) > 0:
                        nodes_to_add.append(middle)
                    if len(after.text) > 0:
                        if len(after.text) > 0:
                            nodes_to_add.extend(split_nodes_delimiter([after], delimiter, text_type))

                    new_nodes.extend(nodes_to_add)
                else:
                    new_nodes.append(each)
            case _:
                new_nodes.append(each)
    return new_nodes
#split Textnodes into TextNode chunks for images, does not allow for nested Text-types
def split_nodes_image(old_nodes):
    new_nodes = []
    for each in old_nodes:
        match (each.text_type):
            case TextType.NORMAL:
                text = each.text
                start_text = text.find("![")
                if start_text != -1:
                    end_text = text.find("]")
                    if end_text == -1:
                        raise Exception("Invalid markdown: unclosed text")
                    start_link = text.find("(")
                    if start_link == -1:
                        raise Exception("Invalid markdown: missing link start")
                    end_link = text.find(")")
                    if start_link == -1:
                        raise Exception("Invalid markdown: missing link end")                    
                    before = TextNode(text[0:start_text], TextType.NORMAL)
                    middle = TextNode(text[start_text + 2:end_text], TextType.IMAGES,text[start_link + 1:end_link])
                    after = TextNode(text[end_link + 1:], TextType.NORMAL)

                    nodes_to_add = []
                    if len(before.text) > 0:
                        nodes_to_add.append(before)
                    if len(middle.URL) > 0:
                        nodes_to_add.append(middle)
                    else:
                        raise Exception ("No URL included")
                    if len(after.text) > 0:
                        if len(after.text) > 0:
                            nodes_to_add.extend(split_nodes_image([after],))

                    new_nodes.extend(nodes_to_add)
                else:
                    new_nodes.append(each)
            case _:
                new_nodes.append(each)
    return new_nodes

 #split Textnodes into TextNode chunks for links, does not allow for nested Text-types   
def split_nodes_link(old_nodes):
    new_nodes = []
    for each in old_nodes:
        match (each.text_type):
            case TextType.NORMAL:
                text = each.text
                start_text = text.find("[")
                if start_text != -1:
                    end_text = text.find("]")
                    if end_text == -1:
                        raise Exception("Invalid markdown: unclosed text")
                    start_link = text.find("(")
                    if start_link == -1:
                        raise Exception("Invalid markdown: missing link start")
                    end_link = text.find(")")
                    if start_link == -1:
                        raise Exception("Invalid markdown: missing link end")                    
                    before = TextNode(text[0:start_text], TextType.NORMAL)
                    middle = TextNode(text[start_text + 1:end_text], TextType.LINKS,text[start_link + 1:end_link])
                    after = TextNode(text[end_link + 1:], TextType.NORMAL)

                    nodes_to_add = []
                    if len(before.text) > 0:
                        nodes_to_add.append(before)
                    if not middle.text:  
                        warnings.warn("Link created with empty anchor text")
                    if len(middle.URL) > 0:
                        nodes_to_add.append(middle)
                    
                    if len(after.text) > 0:
                        if len(after.text) > 0:
                            nodes_to_add.extend(split_nodes_link([after],))

                    new_nodes.extend(nodes_to_add)
                else:
                    new_nodes.append(each)
            case _:
                new_nodes.append(each)
    return new_nodes

#split raw markdown into TextNode chunks, basicly runs everything above in order and outputs TextNodes
def text_to_textnodes(text):
        node = [TextNode(text,TextType.NORMAL,)]
        test_cases = {TextType.BOLD:"**" ,TextType.ITALIC:"*",TextType.ITALIC:"_",TextType.CODE:"`"}
        for k,v in dict.items(test_cases):
            node = split_nodes_delimiter(node, v, k)
        node = split_nodes_image(node)
        node = split_nodes_link(node)
        return node

def markdown_to_blocks(markdown):
    new_blocks = []
    blocks = markdown.split("\n\n")
    for each in blocks:
        stripped = each.strip()
        if len(stripped) > 0:
            new_blocks.append(stripped)
    return new_blocks

