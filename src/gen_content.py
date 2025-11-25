import os
from markdown_to_html_node import markdown_to_html_node

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
    