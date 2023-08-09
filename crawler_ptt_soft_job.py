
import requests
import re
import urllib.request

url="https://www.ptt.cc/bbs/soft_job/index.html"

response=requests.get(url)

html_data=response.text

title_Regex=r'<a href=\".+?>(.*)<\/a>'


titles_list=re.findall(title_Regex,html_data)

for index in range(len(titles_list)):
    print("\n",titles_list[index])