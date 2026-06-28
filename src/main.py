import os
import shutil
from textnode import TextNode, TextType


def main():
    copy_contents("static", "public")


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


if __name__ == "__main__":
    main()
