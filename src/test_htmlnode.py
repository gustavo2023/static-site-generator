import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode(
            tag="div", value="Hello", children=[], props={"class": "my-class"}
        )
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "my-class"})

    def test_init_with_none_children_and_props(self):
        node = HTMLNode(tag="span", value="World")
        self.assertEqual(node.tag, "span")
        self.assertEqual(node.value, "World")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

    def test_props_to_html(self):
        node = HTMLNode(tag="p", props={"id": "paragraph", "class": "text"})
        expected_html = 'id="paragraph" class="text"'
        self.assertEqual(node.props_to_html(), expected_html)

    def test_repr(self):
        node = HTMLNode(tag="a", value="Link", props={"href": "https://example.com"})
        expected_repr = "HTMLNode(tag=a, value=Link, children=[], props={'href': 'https://example.com'})"
        self.assertEqual(repr(node), expected_repr)

    def test_leaf_node_to_html(self):
        leaf_node = LeafNode(tag="span", value="Hello", props={"class": "my-class"})
        expected_html = '<span class="my-class">Hello</span>'
        self.assertEqual(leaf_node.to_html(), expected_html)

    def test_leaf_node_to_html_without_props(self):
        leaf_node = LeafNode(tag="span", value="Hello")
        expected_html = "<span>Hello</span>"
        self.assertEqual(leaf_node.to_html(), expected_html)

    def test_leaf_node_to_html_without_tag(self):
        leaf_node = LeafNode(tag=None, value="Hello")
        expected_html = "Hello"
        self.assertEqual(leaf_node.to_html(), expected_html)

    def test_parent_node_to_html(self):
        child1 = LeafNode(tag="span", value="Child 1")
        child2 = LeafNode(tag="span", value="Child 2")
        parent_node = ParentNode(
            tag="div", children=[child1, child2], props={"class": "parent"}
        )
        expected_html = (
            '<div class="parent"><span>Child 1</span><span>Child 2</span></div>'
        )
        self.assertEqual(parent_node.to_html(), expected_html)

    def test_parent_node_to_html_without_props(self):
        child1 = LeafNode(tag="span", value="Child 1")
        child2 = LeafNode(tag="span", value="Child 2")
        parent_node = ParentNode(tag="div", children=[child1, child2])
        expected_html = "<div><span>Child 1</span><span>Child 2</span></div>"
        self.assertEqual(parent_node.to_html(), expected_html)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
