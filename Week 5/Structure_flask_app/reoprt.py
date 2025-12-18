import os

OUTPUT_FILE = "APPLICATION.md"

# folders to ignore
IGNORE_DIRS = {
    ".env", "__pycache__", ".git", ".vscode",
    "node_modules", ".idea"
}

# files to ignore
IGNORE_FILES = {
    OUTPUT_FILE
}

def get_language_hint(filename):
    ext = os.path.splitext(filename)[1]
    return {
        ".py": "python",
        ".html": "html",
        ".css": "css",
        ".js": "javascript",
        ".json": "json",
        ".md": "markdown",
        ".txt": "text",
        ".sql": "sql",
        ".yml": "yaml",
        ".yaml": "yaml"
    }.get(ext, "")

def write_tree(root, md):
    md.write("## 📁 Project Structure\n\n")
    for root_dir, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        level = root_dir.replace(root, "").count(os.sep)
        indent = "│   " * level
        md.write(f"{indent}├── {os.path.basename(root_dir)}/\n")
        for file in files:
            if file not in IGNORE_FILES:
                md.write(f"{indent}│   ├── {file}\n")
    md.write("\n---\n\n")

def write_files(root, md):
    md.write("## 📄 File Contents\n\n")
    for root_dir, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for file in files:
            if file in IGNORE_FILES:
                continue

            path = os.path.join(root_dir, file)
            rel_path = os.path.relpath(path, root)

            md.write(f"### `{rel_path}`\n\n")

            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception as e:
                content = f"⚠️ Could not read file: {e}"

            lang = get_language_hint(file)
            md.write(f"```{lang}\n{content}\n```\n\n")

def main():
    root = os.getcwd()
    with open(OUTPUT_FILE, "w", encoding="utf-8") as md:
        md.write("# 📦 Application Documentation\n\n")
        md.write("Auto-generated application overview.\n\n")
        write_tree(root, md)
        write_files(root, md)

    print(f"✅ {OUTPUT_FILE} generated successfully.")

if __name__ == "__main__":
    main()
