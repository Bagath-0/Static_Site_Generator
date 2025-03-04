
from textnode import TextNode,TextType
from split_nodes import markdown_to_blocks, text_to_textnodes
from Block_to_type import *
from textnode import TextNode
from htmlnode import *
    
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    child_nodes = []  # List to collect all block nodes
    
    for block in blocks:
        block_type = block_to_block_type(block)
        
        match block_type:
            case BlockType.PARAGRAPH:
                # Replace multiple spaces and newlines with a single space
                normalized_text = " ".join(block.split())
                print (normalized_text)
                node = ParentNode("p", text_to_children(normalized_text))
                child_nodes.append(node)
                
            case BlockType.HEADING:
                # Calculate the heading level
                level = 0
                for char in block:
                    if char == '#':
                        level += 1
                    else:
                        break
                heading_text = block[level:].strip()
                node = ParentNode(f"h{level}", text_to_children(heading_text))
                child_nodes.append(node)
                
            case BlockType.CODE:
                # Handle code blocks
                
                text = block.strip("```")
                text_node = TextNode(text,TextType.CODE)
                html_node = text_node.text_node_to_html_node()
                node = ParentNode("pre",[html_node])
                child_nodes.append(node)
                
            case BlockType.UNORDERED_LIST:
                # Handle unordered lists
                items = block.strip().split("\n")
                list_items = []
                
                for item in items:
                    # Remove the "- " prefix and process the item text
                    item_text = item.strip()[2:].strip()
                    # Create li node with processed children
                    li_node = ParentNode("li",  text_to_children(item_text))
                    list_items.append(li_node)
                
                # Create ul node with all list items
                node = ParentNode("ul",list_items)
                child_nodes.append(node)

            case BlockType.ORDERED_LIST:
                # Handle ordered lists
                items = block.strip().split("\n")
                list_items = []
                
                
                for item in items:
                    item_text = item.strip()
                    dot_index = item_text.find(".")
                    if dot_index != -1:  # If we found a period
                        item_text = item_text[dot_index + 1:].strip()
                    
                    # Create li node with processed children
                    li_node = ParentNode("li", text_to_children(item_text))
                    list_items.append(li_node)
                
                # Create ol node with all list items
                node = ParentNode("ol", list_items)
                child_nodes.append(node)

            case BlockType.QUOTE:
                # Handle blockquotes
                # Remove the '>' prefix from each line
                lines = block.strip().split("\n")
                quote_content = " ".join(
                line[1:].strip() if line.startswith(">") else line.strip()
                for line in lines
                if line.strip() != ">"
            )
                node = ParentNode("blockquote", text_to_children(quote_content.strip()))
                child_nodes.append(node)          

                
    # Create parent div with all children
    
    return ParentNode("div", child_nodes)

def text_to_children(text):
    # Get the text nodes using your existing function
    text_nodes = text_to_textnodes(text)
    
    # Convert each TextNode to an HTMLNode
    html_nodes = []
    for node in text_nodes:
        html_node = node.text_node_to_html_node()
        html_nodes.append(html_node)
    
    return html_nodes