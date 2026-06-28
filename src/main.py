import os
import shutil
import sys
from pathlib import Path
from markdown_to_htmlnode import markdown_to_html_node


def main():
    basepath = "/"

    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    copy_contents("static", "public")
    generate_pages_recursive("content", "template.html", "docs", basepath)


def copy_contents(source_dir: str, dest_dir: str):
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"Source directory '{source_dir}' was not found")
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.mkdir(dest_dir)

    source_contents = os.listdir(source_dir)

    for item in source_contents:
        item_path = os.path.join(source_dir, item)

        if os.path.isdir(item_path):
            copy_contents(item_path, os.path.join(dest_dir, item))
        else:
            shutil.copy(item_path, dest_dir)


def extract_title(markdown: str) -> str:
    lines = markdown.splitlines()

    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found in markdown")


def generate_page(
    from_path: str, template_path: str, dest_path: str, basepath: str
) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as file:
        markdown = file.read()

    with open(template_path, "r") as file:
        template = file.read()

    html_str = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_str)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as file:
        file.write(template)


def generate_pages_recursive(
    dir_path_content: str, template_path: str, dest_dir_path: str, basepath: str
) -> None:
    content_items = os.listdir(dir_path_content)

    for item in content_items:
        item_path = os.path.join(dir_path_content, item)

        if os.path.isdir(item_path):
            generate_pages_recursive(
                item_path, template_path, os.path.join(dest_dir_path, item), basepath
            )
        else:
            if item_path.endswith(".md"):
                file_path = Path(item_path).with_suffix(".html")
                dest_file_path = os.path.join(dest_dir_path, file_path.name)
                generate_page(item_path, template_path, dest_file_path, basepath)


if __name__ == "__main__":
    main()
