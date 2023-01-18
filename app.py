from bs4 import BeautifulSoup
import openpyxl

# read index.html file and parse it with beautifulsoup
with open("page4.html", "r") as file:
    soup = BeautifulSoup(file, "html.parser")

# find all div with class= "s-card-container s-overflow-hidden aok-relative puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border"
divs = soup.find_all("div", {"class": "s-card-container s-overflow-hidden aok-relative puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border"})

# open data.xlsx and write link,title,rating and price.
workbook = openpyxl.Workbook()
worksheet = workbook.active

worksheet.append(["link", "title", "rating", "price"])

for div in divs:
    try:
        # try find img  with class="s-image" then link=img.src
        img = div.find("img", {"class": "s-image"})
        link = img["src"]
    except:
        # except link=''
        link = ""

    try:
        # try find span with class="a-size-base-plus a-color-base a-text-normal" then title=span.text
        title = div.find("span", {"class": "a-size-base-plus a-color-base a-text-normal"}).text
    except:
        # except title=''
        title = ""

    try:
        # try find span with class="a-icon-alt" then rating=span.text
        rating = div.find("span", {"class": "a-icon-alt"}).text
    except:
        # except rating=''
        rating = ""

    try:
        # try find span with class="a-price-whole" then price=span.text
        price = div.find("span", {"class": "a-price-whole"}).text
    except:
        # except price=''
        price = ""

    worksheet.append([link, title, rating, price])

workbook.save("data.xlsx")
