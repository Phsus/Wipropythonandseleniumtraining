import requests
from bs4 import BeautifulSoup


html_string = """
<html>
  <head><title>Test Page</title></head>
  <body>
    <h1>Welcome</h1>
    <p>This is a paragraph.</p>
    <a href="https://example.com">Click Here</a>
  </body>
</html>
"""

soup_basic = BeautifulSoup(html_string, "html.parser")

# 1. Extract Title
print(f"Title Text: {soup_basic.title.string}")

# 2. Extract H1
print(f"H1 Text: {soup_basic.find('h1').text}")

# 3. Extract Paragraph
print(f"Paragraph Text: {soup_basic.find('p').text}")

# 4. Find first <a> and print href
first_link = soup_basic.find('a')
print(f"First Link Href: {first_link.get('href')}")

# 5. Prettify Output
print("\nPrettified HTML:")
print(soup_basic.prettify()[:100] + "...")


"""
find(): Returns the first matching element as a single object. 
        Returns None if no match is found.
find_all(): Returns a list (ResultSet) of all matching elements. 
            Returns an empty list [] if no match is found.
"""



product_url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
response = requests.get(product_url)
soup_product = BeautifulSoup(response.text, "html.parser")


name = soup_product.find("h1").text
price = soup_product.find("p", class_="price_color").text

rating_class = soup_product.find("p", class_="star-rating")["class"]
rating = rating_class[1] # Gets "Three"
availability = soup_product.find("p", class_="instock availability").text.strip()

print(f"Product Name: {name}")
print(f"Price:        {price}")
print(f"Rating:       {rating}")
print(f"Availability: {availability}")




# Going to the home page to get multiple images
home_url = "http://books.toscrape.com/"
home_response = requests.get(home_url)
soup_home = BeautifulSoup(home_response.text, "html.parser")

# Find all <img> tags
all_images = soup_home.find_all("img")

print(f"Found {len(all_images)} images on the homepage:")
for img in all_images[:5]:
    img_url = img.get("src")
    print(f"Image Source: {img_url}")

