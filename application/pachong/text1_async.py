import requests

url = "https://mp.weixin.qq.com/s/MQY6Iur9_qf1jiMX2VGPew"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
# response = requests.get(url, headers=headers)
response = requests.get(url)
html_content = response.text

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_content, "html.parser")
print(soup)
poem_items = soup.find_all("div", class_="poem-item")