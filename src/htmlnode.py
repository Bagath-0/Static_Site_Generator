def __repr__(self):
    return f"tag={self.tag} value={self.value} children={self.children} props={self.props}"

class HTML:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        if not self.props:  # Handles both `None` and empty cases
            return ""
        props_list = []
        for key, value in self.props.items():
            props_list.append(f"{key}='{value}'")  # Formatting with f-strings is neater
        return " "+" ".join(props_list)
    def __repr__(self):
        print (f"tag={self.tag} value={self.value} children={self.children} props={self.props}")
    
    def __eq__(self, other):
        return (self.tag == other.tag and 
        self.value == other.value and self.children == other.children and self.props == other.props)          


class Leaf(HTML):
    def __init__(self,tag,value,props=None):
        if value is None:
            raise ValueError("LeafNode must have a value")
        super().__init__(tag,value,children=None,props=props)
    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        striptag = self.tag.strip('"')
        stripvalue = self.value.strip('"')
        conv_props = self.props_to_html()
        return f"<{striptag}{conv_props}>{stripvalue}</{striptag}>"
        
    def __eq__(self, other):
        return (self.tag == other.tag and 
        self.value == other.value and self.props == other.props)

class ParentNode(HTML):
    def __init__(self,tag,children,props=None):
        super().__init__(tag,value=None,children=children,props=props)
        if not children:
            raise ValueError("A ParentNode must have children.")
    def to_html(self):
        # Validate that tag and children are present.
        if self.tag is None:
            raise ValueError("Tag is missing")
        if not self.children:  # This checks if the list is empty or None.
            raise ValueError("No children")

    # Prepare the opening and closing tags for this parent node.
        strip_tag_parent = self.tag.strip('"')
        start_tag_parent = f"<{strip_tag_parent}>"
        end_tag_parent = f"</{strip_tag_parent}>"

    # Combine the HTML of all children.
        children_html = ""
        for child in self.children:
            children_html += child.to_html()  # Accumulate each child's HTML.

    # Return the complete HTML for this parent node.
        return f"{start_tag_parent}{children_html}{end_tag_parent}"
    
