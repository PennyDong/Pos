import urllib.request as req

url = 'https://news.ycombinator.com/'
#建立一個 Request 物件. 附加Request Headers 的資訊
request=req.Request(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"})

with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
print(data)
#解析原始碼
import bs4
root=bs4.BeautifulSoup(data, "html.parser")
titles=root.find_all("span",class_="titleline") #尋找 class="title" 的div 標籤

for title in titles:
    if title.a !=None: #如果標題包含 a 標籤 (沒有被刪除). 印出來
        print(title.a.string)