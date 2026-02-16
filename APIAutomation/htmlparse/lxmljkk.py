import requests
from lxml import html

# URL set to Hacker News as the 'titleline' class suggests
url = "https://news.ycombinator.com/"
response = requests.get(url) # Fixed spelling from 'respose'

# Fixed 'fromString' to 'fromstring' (lowercase 's')
data = html.fromstring(response.content)

# Fixed title extraction logic
title = data.xpath("//title/text()")[0]
print(title)

links = data.xpath("//a/@href")
print(links)

links = data.xpath("//a")
for link in links:
    print(link.text)
    print(link.get("href"))

# Extracting title lines
titlelines = data.xpath("//span[@class='titleline']")
print(titlelines)
for title_span in titlelines:
    # On Hacker News, the text is inside the <a> tag within the <span>
    text = title_span.xpath(".//a/text()")
    if text:
        print(text[0])