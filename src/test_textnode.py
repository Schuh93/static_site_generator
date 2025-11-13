import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text_type_not_eq(self):
        node = TextNode("short text", TextType.ITALIC)
        node2 = TextNode("short text", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode("typo", TextType.IMAGE)
        node2 = TextNode("tpyo", TextType.IMAGE)
        self.assertNotEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("text", TextType.BOLD)
        node2 = TextNode("text", TextType.BOLD, url="hyperlink")
        self.assertNotEqual(node, node2)

    def test_None_url_eq(self):
        node = TextNode("text", TextType.ITALIC)
        node2 = TextNode("text", TextType.ITALIC, None)
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()