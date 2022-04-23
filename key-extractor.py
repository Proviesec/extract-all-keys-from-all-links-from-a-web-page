import requests
import sys
import re

headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

# Find and Extract all url parameter from a big text
def extract_url(text):
    key_list = set()
    text = text.decode('utf-8')
    urls_extract = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    for url in urls_extract:
        params = re.findall(r'([^=&]+)=([^=&]+)', url)
        res = dict()
        for key, val in params:
            key_list.add(val)
    return key_list
      
def crawl_miner(url):
    try:
        r = requests.get(url, headers=headers)
    except requests.exceptions.ConnectionError:
        return
    if r.status_code == 200:
        return r.content
    else:
        return

url = sys.argv[1]
if url.startswith("http") == False:
    url = "https://"+url
export = int(sys.argv[2]) 
crawl = crawl_miner(url)

words = set()

if crawl:
    txt_return = extract_url(crawl)
    for txt_url in txt_return:
        words.add(txt_url)

if export:
    with open('key-export.txt', 'w') as f:
        f.write(str(words))
            
print(words)
