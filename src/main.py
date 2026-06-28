import os
import shutil
from markdown_to_htmlnode import markdown_to_html_node


def main():
    copy_contents("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")


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


def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as file:
        markdown = file.read()

    with open(template_path, "r") as file:
        template = file.read()

    html_str = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_str)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as file:
        file.write(template)


if __name__ == "__main__":
    main()
