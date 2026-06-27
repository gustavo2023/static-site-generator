from markdown_to_blocks import markdown_to_blocks
from block_type import block_to_block_type, BlockType
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import text_node_to_html_node
from text_to_textnodes import text_to_textnodes


def markdown_to_html_node(markdown_text: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown_text)
    children_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            children_nodes.append(handle_paragraph(block))
        elif block_type == BlockType.HEADING:
            children_nodes.append(handle_heading(block))
        elif block_type == BlockType.CODE_BLOCK:
            children_nodes.append(handle_code_block(block))
        elif block_type == BlockType.QUOTE:
            children_nodes.append(handle_quote_block(block))
        elif block_type == BlockType.UNORDERED_LIST:
            children_nodes.append(handle_unordered_list_block(block))
        elif block_type == BlockType.ORDERED_LIST:
            children_nodes.append(handle_ordered_list_block(block))

    return ParentNode("div", children_nodes)


def text_to_children(text: str) -> list[HTMLNode]:
    text_nodes = text_to_textnodes(text)
    html_nodes = []

    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        html_nodes.append(html_node)

    return html_nodes


def handle_heading(block: str) -> ParentNode:
    level = block.count("#", 0, block.find(" "))
    text = block[level + 1 :]
    children = text_to_children(text)

    return ParentNode(f"h{level}", children)


def handle_quote_block(block: str) -> ParentNode:
    lines = block.splitlines()
    new_lines = []

    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")

        new_lines.append(line.lstrip(">").strip())

    content = " ".join(new_lines)
    children = text_to_children(content)

    return ParentNode("blockquote", children)


def handle_unordered_list_block(block: str) -> ParentNode:
    lines = block.splitlines()
    html_items = []

    for line in lines:
        if not line.startswith("-"):
            raise ValueError("Invalid unordered list block")

        text = line[1:].strip()
        children = text_to_children(text)
        li_node = ParentNode("li", children)
        html_items.append(li_node)

    return ParentNode("ul", html_items)


def handle_ordered_list_block(block: str) -> ParentNode:
    lines = block.splitlines()
    html_items = []
    i = 1

    for line in lines:
        if not line.startswith(f"{i}."):
            raise ValueError("Invalid ordered list block")

        text = line.split(".", 1)[1].strip()
        children = text_to_children(text)
        li_node = ParentNode("li", children)
        html_items.append(li_node)
        i += 1

    return ParentNode("ol", html_items)


def handle_code_block(block: str) -> ParentNode:
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")

    text = block[3:-3].strip()
    code_node = LeafNode("code", text)

    return ParentNode("pre", [code_node])


def handle_paragraph(block: str) -> ParentNode:
    lines = block.splitlines()
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)
