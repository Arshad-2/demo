# if you want to scrape a website :
# 1.use the API
# 2.Html web scraping using some tools like bs4(beutifulsoup's)


# step 0: install all the requirement
# pip install requests 
# pip install bs4
# pip install html5lib 
import requests
from bs4 import BeautifulSoup
url = "http://codewithharry.com"
# step 1: get the html
r= requests.get(url)
htmlcontent=r.content
print(htmlcontent)
# step 2: parse the html
# step 3: html tree transversal 


