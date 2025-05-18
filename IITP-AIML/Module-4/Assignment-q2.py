import requests
from bs4 import BeautifulSoup
import os
import sys
# Option to use test mode with current url

if len(sys.argv) > 1 and sys.argv[1] == "test":
    test_file_relative_path = os.path.join(os.path.dirname(__file__), "Resources", "test.html")
    url = f"file:///{os.path.abspath(test_file_relative_path).replace(os.sep, '/')}"
    file_path = url.replace("file:///", "")
else:
    url = input("Enter file URL (e.g., file:///C:/path/to/file.html): ")
    if url.startswith("file:///"):
        file_path = url.replace("file:///", "")
    elif url.startswith("http://") or url.startswith("https://"):
        response = requests.get(url)
        html_content = response.text
        file_path = None
    else:
        print("Invalid URL format.")
        sys.exit(1)
with open(file_path, 'r', encoding='utf-8') as f:
    html_content = f.read()


soup = BeautifulSoup(html_content, 'html.parser')

h1_tag = soup.find('h1')

if h1_tag:
    print(h1_tag.text)
else:
    print("H1 tag not found")