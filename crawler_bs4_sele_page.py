from bs4 import BeautifulSoup
import requests

# 連結網站

for page in range(1,4):

    response = requests.get(
        "http://www.inside.com.tw/tag/AI?page=" + str(page)
    )

    # HTML原始碼解析

soup = BeautifulSoup(response.text, "html.parser")

    # 取得所有class為post_title的<h3>

titles = soup.find_all("h3" , {"class": "post_title"})

print(f"=======第strpage頁============")

    #取得標題文字
for title in titles:
    print(title.select_one("a").getText()) 

