import unittest
from textnode import TextNode, TextType, text_node_to_html_node
from split_nodes import split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_text_node_creation(self):
        text_node = TextNode("Hello, World!", TextType.TEXT)
        self.assertEqual(text_node.text, "Hello, World!")
        self.assertEqual(text_node.text_type, TextType.TEXT)
        self.assertIsNone(text_node.url)

    def test_text_node_equality(self):
        node1 = TextNode("Hello", TextType.TEXT)
        node2 = TextNode("Hello", TextType.TEXT)
        node3 = TextNode("Hello", TextType.BOLD)
        self.assertEqual(node1, node2)
        self.assertNotEqual(node1, node3)

    def test_text_node_to_html_node(self):
        text_node = TextNode("Hello", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "Hello")

        bold_node = TextNode("Bold", TextType.BOLD)
        html_bold_node = text_node_to_html_node(bold_node)
        self.assertEqual(html_bold_node.tag, "strong")
        self.assertEqual(html_bold_node.value, "Bold")

    def test_split_nodes_delimiter(self):
        nodes = [
            TextNode("This is *bold* text.", TextType.TEXT),
            TextNode("This is normal.", TextType.TEXT),
        ]
        split_nodes = split_nodes_delimiter(nodes, "*", TextType.BOLD)

        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.TEXT),
            TextNode("This is normal.", TextType.TEXT),
        ]

        self.assertEqual(split_nodes, expected_nodes)


if __name__ == "__main__":
    unittest.main()
