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

    def text_node_to_html_node(self, basepath):
        match (self.text_type):
            case (TextType.NORMAL):
                return Leaf(None, self.text)
            case (TextType.BOLD):
                return Leaf('"b"', self.text)
            case (TextType.ITALIC):
                return Leaf('"i"', self.text)
            case (TextType.CODE):
                return Leaf('"code"', self.text)
            case (TextType.LINKS):
                return Leaf('"a"', self.text, {"href": f"{basepath.rstrip("/")}{self.URL}"})
            case (TextType.IMAGES):
                return Leaf('"img"', "", {"src": f"{basepath.rstrip("/")}{self.URL}", "alt": self.text})
            case _:
                raise Exception("invalid type")
                    

