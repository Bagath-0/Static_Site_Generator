import os
import shutil
from pathlib import Path
from split_nodes import markdown_to_blocks
from markdown_to_html_node import markdown_to_html_node
import sys
# Get the basepath from the first command-line argument, or default to "/"
basepath = sys.argv[1] if len(sys.argv) > 1 else ""


def transfer_start(source,target):
    if os.path.exists(target):
        shutil.rmtree(target, ignore_errors=False, onerror=None,onexc=None, dir_fd=None)
    os.mkdir(target, mode=0o777, dir_fd=None)
    transfer_files(source,target)

def transfer_files(source,target):
    print (f"starting check for {source}")
    if os.path.isfile(source):
        print(f"file found! {source}")
        return shutil.copy(source, target, follow_symlinks=True)
    else:
        if os.path.isdir(source):
            print (f"directory found!{source}")
            files = os.listdir(path=source)
            print (f"heres whats in this directory! {files}")
            for file in files:
                if os.path.isdir((os.path.join(source, file ))):
                    new_target = (os.path.join(target, file))
                    os.mkdir(new_target)
                    print (f"checking {file}")
                    transfer_files((os.path.join(source, file )),new_target)
                else:
                    print (f"checking {file}")
                    transfer_files((os.path.join(source, file )),target)
                
        else:
            print("invalid file")            

transfer_start("/home/bagath/workspace/Static_Site_Generator/static","/home/bagath/workspace/Static_Site_Generator/public")

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# "):
            return block.strip("# ").strip()
    
    raise Exception ("No header 1 found")

def generate_page(from_path, template_path, dest_path,basepath):
    print (f"Generating page from {from_path} to {dest_path} using {template_path}")
    MD = Path(from_path).read_text()
    temp = Path(template_path).read_text()
    HTML = (markdown_to_html_node(MD,basepath)).to_html()
    title = extract_title(MD)
    temp = temp.replace("{{ Title }}", title)
    Full_HTML = temp.replace("{{ Content }}", HTML)
    if not os.path.exists(dest_path):
        os.makedirs(dest_path, mode=0o777, exist_ok=False)
    file = open(os.path.join(dest_path,'index.html'), 'w+')
    file.write(Full_HTML)
    file.close
    



def generate_pages_recursive(dir_path_content, template_path, dest_dir_path,basepath,old_dest = None):
    if os.path.isfile(dir_path_content):
        print(f"file found! {dir_path_content}")
        return generate_page(dir_path_content, template_path, old_dest,basepath)
    else:
        if os.path.isdir(dir_path_content):
            print (f"directory found!{dir_path_content}")
            files = os.listdir(path=dir_path_content)
            print (f"heres whats in this directory! {files}")
            for file in files:
                new_target = (os.path.join(dest_dir_path, file))
                print (f"new target dir is {new_target}")
                full_file = (os.path.join(dir_path_content, file ))
                print (f"checking {full_file}")
                generate_pages_recursive(full_file,template_path,new_target,basepath,dest_dir_path)              
        else:
            print("invalid file")    

generate_pages_recursive ("/home/bagath/workspace/Static_Site_Generator/content/","/home/bagath/workspace/Static_Site_Generator/template.html","/home/bagath/workspace/Static_Site_Generator/public",basepath)

