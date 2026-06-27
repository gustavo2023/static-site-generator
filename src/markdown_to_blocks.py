def markdown_to_blocks(markdown_text: str) -> list[str]:
    blocks = [block.strip() for block in markdown_text.split("\n\n") if block.strip()]
    return blocks
