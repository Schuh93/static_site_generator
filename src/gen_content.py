import os
from markdown_to_html_node import markdown_to_html_node
from pathlib import Path


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if os.path.isdir(dir_path_content):
        if not os.path.exists(dest_dir_path):
            os.mkdir(dest_dir_path)
        
        files = os.listdir(dir_path_content)
        for file in files:
            new_src = os.path.join(dir_path_content, file)
            new_dst = os.path.join(dest_dir_path, file)
            generate_pages_recursive(new_src, template_path, new_dst)

    elif os.path.isfile(dir_path_content):
        if dir_path_content.endswith(".md"):
            dest_dir_path = Path(dest_dir_path).with_suffix(".html")
            generate_page(dir_path_content, template_path, dest_dir_path)

    else:
        print(f"invalid source {dir_path_content}")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, "r") as file:
        markdown = file.read()

    with open(template_path, "r") as file:
        template = file.read()

    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, "w") as file:
        file.write(template)


def extract_title(markdown):
    html_text = markdown_to_html_node(markdown).to_html()
    title_start = html_text.find("<h1>") + 4
    title_end = html_text.find("</h1>")

    title = html_text[title_start:title_end].strip()

    if title == "":
        raise ValueError("no title found")

    return title
    