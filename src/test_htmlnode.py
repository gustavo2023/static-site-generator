import unittest
from htmlnode import HTMLNode


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
