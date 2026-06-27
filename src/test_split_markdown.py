import unittest
from split_raw_markdown import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


class TestSplitRawMarkdown(unittest.TestCase):
    def test_split_nodes_image(self):
        old_nodes = [
            TextNode("This is an image: ![alt text](image_url)", TextType.TEXT)
        ]
        expected_nodes = [
            TextNode("This is an image: ", TextType.TEXT),
            TextNode("alt text", TextType.IMAGE, url="image_url"),
        ]
        new_nodes = split_nodes_image(old_nodes)
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_link(self):
        old_nodes = [TextNode("This is a link: [link text](link_url)", TextType.TEXT)]
        expected_nodes = [
            TextNode("This is a link: ", TextType.TEXT),
            TextNode("link text", TextType.LINK, url="link_url"),
        ]
        new_nodes = split_nodes_link(old_nodes)
        self.assertEqual(new_nodes, expected_nodes)


if __name__ == "__main__":
    unittest.main()
