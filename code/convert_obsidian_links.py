import os
import re


def ensure_directory(path: str) -> None:
    """
    Ensure that the directory for the given path exists. If not, create it.

    Args:
        path (str): The file path whose directory structure needs verification.

    Returns:
        None
    """
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)


def create_placeholder_file(link: str, root: str) -> None:
    """
    Creates a placeholder markdown file for a link and add a predefined text to it.

    Args:
        link (str): The link text, which is used to generate the file name.
        root (str): The root directory where the file should be created.

    Returns:
        None
    """
    md_link = link.replace(" ", "-").lower() + ".md"
    file_path = os.path.join(root, md_link)
    ensure_directory(file_path)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("[[Under Construction]]\n")


def convert_obsidian_links(file_path: str, root: str) -> None:
    """
    Converts Obsidian-Style links in a markdown file to a standard markdown link.

    Args:
        file_path (str): The path to the markdown file to be converted.
        root (str): The root directory for searching for markdown files and creating new ones.

    Returns:
        None
    """

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Regex to find Obsidian-style links, e.g., [[Note Title]]
    obsidian_link_pattern = r"\[\[([^\]]+)\]\]"
    markdown_links = re.findall(obsidian_link_pattern, content)

    for link in markdown_links:
        md_link = link.replace(" ", "-").lower()
        md_file_path = os.path.join(root, md_link + ".md")
        if not os.path.exists(md_file_path):
            create_placeholder_file(link, root)
            print(f"Created placeholder for {link} at {md_file_path}")
        md_formatted_link = f"[{link}]({md_link}.md)"
        content = content.replace(f"[[{link}]]", md_formatted_link)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


def main():
    root_directory = "../notes"
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            if file.endswith(".md"):
                convert_obsidian_links(os.path.join(root, file), root)


if __name__ == "__main__":
    main()
