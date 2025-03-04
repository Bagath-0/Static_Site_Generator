import re

def extract_markdown_images(text):
    # Initial validation checks
    alt_text_matches = re.findall(r"\[.*?\]", text)
    url_matches = re.findall(r"\(.*?\)", text)
    
    if len(alt_text_matches) != len(url_matches):
        raise Exception("Mismatch between alt texts and URLs")
    if len(alt_text_matches) == 0 or len(url_matches) == 0:
        raise Exception("No valid markdown found")
    
    # Efficient tuple extraction using grouped regex
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    # Initial validation checks
    anchor_text_matches = re.findall(r"\[.*?\]", text)
    url_matches = re.findall(r"\(.*?\)", text)
    
    if len(anchor_text_matches) != len(url_matches):
        raise Exception("Mismatch between anchor texts and URLs")
    if len(anchor_text_matches) == 0 or len(url_matches) == 0:
        raise Exception("No valid markdown found")
    
    # Efficient tuple extraction using grouped regex
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


