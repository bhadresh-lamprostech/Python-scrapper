import requests
from bs4 import BeautifulSoup

# set the starting page and the number of pages to scrape
start_page = 1
num_pages = 5

for i in range(start_page, start_page + num_pages):
    # make a request to the webpage
    url = f"https://www.amazon.in/s?i=computers&rh=n%3A1375425031&fs=true&page=2&qid=1674021809&ref=sr_pg_2"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # save the page as an HTML file
    with open(f"page{i}.html", "w") as file:
        file.write(str(soup))