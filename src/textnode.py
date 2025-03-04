from enum import Enum
from htmlnode import HTML, Leaf ,ParentNode

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "link"
    IMAGES = "image"

class TextNode:
    def __init__(self,Text,Text_type,Url=None):
        self.text = Text
        self.text_type = Text_type
        self.URL = Url

    def __eq__(self, other):
        return (self.text == other.text and 
        self.text_type == other.text_type and self.URL == other.URL)
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.URL})"

    def text_node_to_html_node(text_node):
        match (text_node.text_type):
            case (TextType.NORMAL):
                return (Leaf(None,text_node.text))
            case (TextType.BOLD):
                return (Leaf('"b"',text_node.text))
            case (TextType.ITALIC):
                return (Leaf('"i"',text_node.text))
            case (TextType.CODE):
                return (Leaf('"code"',text_node.text))
            case (TextType.LINKS):
                return (Leaf('"a"',text_node.text,{"href":text_node.URL}))
            case (TextType.IMAGES):
                return (Leaf('"img"',"",{"src":text_node.URL,"alt":text_node.text}))
            case _:
                raise Exception ("invalid type")
            

