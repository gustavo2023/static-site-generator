# Static Site Generator

A custom-built static site generator written in Python, developed as part of the [Boot.dev](https://boot.dev) backend curriculum. This tool takes raw Markdown files and a template, and compiles them into a complete, static HTML website ready for deployment.

## Features

- **Custom Markdown Parsing**: Parses Markdown into a custom abstract syntax tree (AST) without relying on external Markdown libraries.
- **HTML Node Generation**: Converts the custom AST into valid HTML elements.
- **Supported Markdown Features**:
  - Headings (H1 to H6)
  - Bold and Italic text
  - Blockquotes
  - Unordered and Ordered Lists
  - Code Blocks and Inline Code
  - Images and Links
- **Recursive Generation**: Recursively walks through the `content/` directory and mirrors the file structure in the output directory.
- **Static Asset Management**: Automatically copies all CSS, images, and other static assets from a `static/` directory to the output directory.
- **Relative Pathing**: Supports custom base paths to ensure CSS and links work perfectly regardless of where the site is hosted (e.g., GitHub Pages).

## Project Structure

- `src/` - Contains the Python source code for the generator.
  - `main.py` - The entry point for the generator.
  - `htmlnode.py` - Defines the HTML Node data structures.
  - `textnode.py` - Defines text nodes and conversions.
  - `markdown_to_blocks.py` - Handles splitting Markdown into distinct blocks.
  - `block_type.py` - Identifies the type of Markdown blocks.
  - `markdown_to_htmlnode.py` - Converts Markdown blocks to HTML nodes.
- `content/` - The source Markdown files to be converted.
- `static/` - Static assets like CSS and images.
- `docs/` or `public/` - The output directory where the final HTML is generated.
- `template.html` - The base HTML template used to wrap the generated content.

## Usage

### Local Development

To build the site and serve it locally on port 8888:

```bash
./main.sh
```

### Production Build

To build the site with a specific base path (e.g., for GitHub Pages):

```bash
./build.sh
```

## Deployment

This project is configured to be easily deployable to GitHub Pages. Ensure you run `./build.sh` before committing and pushing the `docs/` folder to your repository.
