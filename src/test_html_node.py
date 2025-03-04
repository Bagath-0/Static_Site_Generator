import unittest

from htmlnode import HTML, Leaf ,ParentNode
class TestHTMLNode(unittest.TestCase):
    def setUp(self):
        # Properties for testing
        self.car_props = {"class": "car-class"}
        self.something_props = {"id": "unique-id"}

        # Leaf nodes
        self.lnode1 = Leaf("p", "text stuffs", self.car_props)
        self.lnode2 = Leaf("span", "more text", self.something_props)

        # Parent nodes
        self.node4 = ParentNode("div", [self.lnode2])  # Child is a single Leaf
        self.node3 = ParentNode("section", [self.node4, self.lnode1])  # Parent contains a mix
        self.node2 = Leaf("h1", "Heading text")  # Another Leaf
        self.node = ParentNode("article", [self.node2, self.node3])  # The root ParentNode

    def test_leaf_to_html(self):
        # Generating HTML for a Leaf with props and value
        expected_output = "<p class='car-class'>text stuffs</p>"
        actual_output = self.lnode1.to_html()
        self.assertEqual(actual_output, expected_output)

        # Generating HTML for a Leaf without props
        no_props_leaf = Leaf("span", "text without props")
        expected_output_no_props = "<span>text without props</span>"
        actual_output_no_props = no_props_leaf.to_html()
        self.assertEqual(actual_output_no_props, expected_output_no_props)    

    def test_parent_node_to_html(self):
        # Generating HTML for a ParentNode with a mix of child nodes
        expected_output = (
            "<article>"
            "<h1>Heading text</h1>"
            "<section>"
            "<div><span id='unique-id'>more text</span></div>"
            "<p class='car-class'>text stuffs</p>"
            "</section>"
            "</article>"
        )
        actual_output = self.node.to_html()
        self.assertEqual(actual_output, expected_output)

        # Test an empty ParentNode (should raise an error)
        with self.assertRaises(ValueError):
            empty_parent = ParentNode("div", [])
            empty_parent.to_html()

        # Testing ParentNode without a tag (should raise a different error)
        with self.assertRaises(ValueError):
            invalid_node = ParentNode(None, [self.lnode1])
            invalid_node.to_html()   

    def test_nested_parent(self):
        child = ParentNode("ul", [Leaf("li", "item 1"), Leaf("li", "item 2")])
        parent = ParentNode("div", [child])
        assert parent.to_html() == "<div><ul><li>item 1</li><li>item 2</li></ul></div>"

    def test_missing_children(self):
        try:
            node = ParentNode("div", [])
            assert False, "Expected a ValueError for missing children, but none was raised."
        except ValueError as e:
    
            assert str(e) == "A ParentNode must have children.", "Unexpected error message raised."

    if __name__ == "__main__":
        unittest.main()