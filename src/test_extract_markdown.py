import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "![alt text](image.jpg) ![another image](image2.png)"
        expected = [("alt text", "image.jpg"), ("another image", "image2.png")]
        result = extract_markdown_images(text)
        self.assertEqual(result, expected)

    def test_extract_markdown_links(self):
        text = "[link text](https://example.com) [another link](https://example.org)"
        expected = [
            ("link text", "https://example.com"),
            ("another link", "https://example.org"),
        ]
        result = extract_markdown_links(text)
        self.assertEqual(result, expected)

    def test_extract_markdown_links_with_exclamation(self):
        text = "![image](image.jpg) [link](https://example.com)"
        expected = [("link", "https://example.com")]
        result = extract_markdown_links(text)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
