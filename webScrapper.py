import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

while True:
  url = input("url : ")
  headers = {
      "User-Agent": "Mozilla/5.0"
  }
  response = requests.get(url, headers=headers, timeout=10)
  response.raise_for_status()
  soup = BeautifulSoup(response.text, "html.parser")
  for link in soup.find_all("a"):
      text = link.get_text(strip=True)
      href = link.get("href")
      if text and href:
          print("Title :", text)
          print("Link  :", urljoin(url, href))
          print("-" * 50)
