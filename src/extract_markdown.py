import re


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    regex = r"!\[([^\]]*)\]\(([^)]+)\)"
    matches = re.findall(regex, text)

    return matches


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex, text)

    return matches
