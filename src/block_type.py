from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE_BLOCK = "code_block"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block: str) -> BlockType:
    def is_heading(block_text: str) -> bool:
        return bool(re.fullmatch(r"#{1,6}\s+.+", block_text))

    def is_code_block(block_text: str) -> bool:
        return bool(re.fullmatch(r"```\n[\s\S]+\n```", block_text))

    def is_quote(block_text: str) -> bool:
        lines = block_text.splitlines()
        return bool(lines) and all(re.fullmatch(r">\s?.*", line) for line in lines)

    def is_unordered_list(block_text: str) -> bool:
        lines = block_text.splitlines()
        return bool(lines) and all(re.fullmatch(r"-\s+.+", line) for line in lines)

    def is_ordered_list(block_text: str) -> bool:
        lines = block_text.splitlines()
        if not lines:
            return False

        for index, line in enumerate(lines, start=1):
            if not re.fullmatch(rf"{index}\.\s+.+", line):
                return False
        return True

    block_checkers = [
        (BlockType.CODE_BLOCK, is_code_block),
        (BlockType.HEADING, is_heading),
        (BlockType.QUOTE, is_quote),
        (BlockType.UNORDERED_LIST, is_unordered_list),
        (BlockType.ORDERED_LIST, is_ordered_list),
    ]

    for block_type, checker in block_checkers:
        if checker(block):
            return block_type

    return BlockType.PARAGRAPH
