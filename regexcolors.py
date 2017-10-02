import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib


# extract text from given url
def extract_text(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")

    # kill scripts and style elements
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()

    return text


# take a url, run text extraction, create regex to search color scheme names
# return a list of schemes
def extract_scheme_names():
    address = "https://github.com/flazz/vim-colorschemes/tree/master/colors"
    content = extract_text(address)
    colorReg = re.compile(r'([0-9a-zA-z]+)(\.vim)')
    mo = colorReg.findall(content)

    name_list = []
    for i in mo:
        name_list.append(i[0])

    return name_list

