import unittest
from block_type import BlockType, block_to_block_type


class TestBlockType(unittest.TestCase):
    def test_single_line_heading(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)

    def test_heading_with_seven_hashes(self):
        self.assertEqual(block_to_block_type("####### Heading"), BlockType.PARAGRAPH)

    def test_empty_code_block(self):
        self.assertEqual(block_to_block_type("```\n```"), BlockType.PARAGRAPH)

    def test_one_line_fenced_code_block_without_internal_newline(self):
        self.assertEqual(block_to_block_type("```code```"), BlockType.PARAGRAPH)

    def test_ordered_list_starting_at_two(self):
        block = "2. first\n3. second"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list_skipping_a_number(self):
        block = "1. first\n3. third"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
