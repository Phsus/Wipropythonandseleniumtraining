import requests
import re
from bs4 import BeautifulSoup

html = '''
<html>
<head><title>My Page</title></head>
<body>
    <h1>Welcome</h1>
    <h2 id="subtitle">Subtitle One</h2>
    <p>This is a <b>bold paragraph</b>.</p>
    <p>Check out <a href="https://google.com">Google</a> and <a href="https://github.com">GitHub</a>.</p>
    <table>
        <tr><td>Row 1, Col 1</td><td>Row 1, Col 2</td></tr>
        <tr><td>Row 2, Col 1</td><td>Row 2, Col 2</td></tr>
    </table>
    <img src="logo.png" alt="Logo">
    <img src="banner.jpg" alt="Banner">
</body>
</html>
'''
soup = BeautifulSoup(html, 'html.parser')

# 1) Parse HTML – Extract title and h1
print(f"1. Title: {soup.title.string}, H1: {soup.h1.text}")

# 2) Extract All Paragraphs
print(f"2. Paragraphs: {[p.text for p in soup.find_all('p')]}")

# 3) Extract All Links and Count
links = soup.find_all('a')
print(f"3. Links: {links}, Count: {len(links)}")

# 4) Extract Attributes
print(f"4. Attributes of H2: {soup.h2.attrs}")

# 5) Extract First h2
print(f"5. First H2: {soup.h2.text}")

# 6) Extract Bold Text
print(f"6. Bold Text: {[b.text for b in soup.find_all('b')]}")

# 7) Extract All href Values
print(f"7. All Hrefs: {[a.get('href') for a in soup.find_all('a')]}")

# 8) Get All Text Without Tags
print(f"8. Text Only: {soup.get_text(separator=' ', strip=True)}")

# 9) Extract Title from Website
try:
    live_html = requests.get("https://www.google.com", timeout=5).text
    print(f"9. Website Title: {BeautifulSoup(live_html, 'html.parser').title.string}")
except:
    print("9. Website Title: Request failed")

# 10) Extract All Headings
print(f"10. All Headings: {[h.text for h in soup.find_all(re.compile('^h[1-6]$'))]}")

# 11) Extract Table Data
print(f"11. Table Data: {[[td.text for td in tr.find_all('td')] for tr in soup.find_all('tr')]}")

# 12) Extract Images
print(f"12. Image Sources: {[img.get('src') for img in soup.find_all('img')]}")