import os
import re
import sys

def replace_tags(path, old_open, old_close, new_open, new_close):

    def replace_content(content):
        pattern = re.escape(old_open) + r'(.*?)' + re.escape(old_close)
        replacement = f"{new_open}\\1{new_close}"
        new_content = re.sub(pattern, replacement, content)
        modified = new_content != content
        return new_content, modified
    
    def process_file(path):
        with open(path, "r+", encoding="utf-8") as f:
            content = f.read()
            new_content, modified = replace_content(content)
            if modified:
                print(f"Replaced in {path}")
                f.seek(0)
                f.write(new_content)
                f.truncate()
        
    def process_dir(path):
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r+", encoding="utf-8") as f:
                        content = f.read()
                        new_content, modified = replace_content(content)
                        if modified:
                            print(f"Replaced in {file}")
                            f.seek(0)
                            f.write(new_content)
                            f.truncate()
    
    if os.path.isfile(path):
        process_file(path)


    elif os.path.isdir(path):
        process_dir(path)
        
    else:
        sys.exit('The directory or file is not found.')

# path
# intial tags
# required tags
replace_tags(r"C:\YourValut\File.md",
                                                            "**", "**",
                                                            "<u>", "</u>")
