from extract_markdown import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    if not old_nodes:
        return []

    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        image_matches = extract_markdown_images(text)

        if not image_matches:
            new_nodes.append(node)
            continue

        split_text = text

        for alt_text, img_url in image_matches:
            text_parts = split_text.split(f"![{alt_text}]({img_url})", 1)

            if len(text_parts) < 2:
                continue

            if text_parts[0]:
                new_nodes.append(TextNode(text_parts[0], TextType.TEXT))

            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url=img_url))
            split_text = text_parts[1]

        if split_text:
            new_nodes.append(TextNode(split_text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    if not old_nodes:
        return []

    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        link_matches = extract_markdown_links(text)

        if not link_matches:
            new_nodes.append(node)
            continue

        split_text = text

        for link_text, link_url in link_matches:
            text_parts = split_text.split(f"[{link_text}]({link_url})", 1)

            if len(text_parts) < 2:
                continue

            if text_parts[0]:
                new_nodes.append(TextNode(text_parts[0], TextType.TEXT))

            new_nodes.append(TextNode(link_text, TextType.LINK, url=link_url))
            split_text = text_parts[1]

        if split_text:
            new_nodes.append(TextNode(split_text, TextType.TEXT))

    return new_nodes
