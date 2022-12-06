# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import os
import webbrowser



URL = "https://www.amazon.com/hz/wishlist/ls/1R2BYKQJFHL5/ref=nav_wishlist_lists_1"
headers = {
    'accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53',
    'sec-fetch-user': '?1',
    'cookie': 'ubid-main=134-9232384-1680620; sp-cdn="L5Z9:AM"; csd-key=eyJ3YXNtVGVzdGVkIjp0cnVlLCJ3YXNtQ29tcGF0aWJsZSI6dHJ1ZSwid2ViQ3J5cHRvVGVzdGVkIjpmYWxzZSwidiI6MSwia2lkIjoiM2I5YWYwIiwia2V5IjoiU2xIUUhwTG84ZDhqc1E4bXZGd3FucjhjMFRaVHFPbTlEZ29rR3E3QmF6bEpQOUFhb0p5cEo3VC9DYmUrZHhVQnlINGhsbFVVaUtOUFZMMFQwSkVkTlIrYXVHWXVCenV2a3JRU3dIQ2pSc1BBK3R6dCtnYjZYa3dEbGZySFRMeFBxNlJNa2QreHZQRjhySmFsYmJpOGRET0lBWHcyYUlDQmRwc2RQWWZmcmx0WGlHZTZJUG1kYUFYR3VVUmNpNGt1RTNtbkFJYWxsSVhYbVY0SlFSYVNIVjNHazV1WlE0R29lWHNjcXBOa0xzakw0a0ZITVZadFNpYm1ZUnhIbldtTlNGNGFHeDhRdUVvOHRNak9XdU52Y0k5dEZGWmgvY0dKSCtWMWs5eE1YTW8wRHhSTk1lTUNhNXFEVjNKSXIzUWRuSHUrUzd0NDFwUTEvMEFtb2FNeEZ3PT0ifQ==; session-id=139-3186051-6691043; x-main="LV4Zy7BQqWvc@VoctApbYCuzYLQTHGp3LZTGFgr?YsfsvSf5B2vuu7yz3NFNzbea"; at-main=Atza|IwEBIKVOccfmTGI2aj5n_9Yrqzjkk7W8T6o8pyOd0495m9NZM8JhNy9Uy6HGYZ2OKZD0EFd5BUeZQitRsP1cab86OeqJMzfN3XrXO73Q__xYJZuweIBkCyHXFqklQe_LbcUj7ArzF7wh1dkRHucZoeIxDDFEdevr8CESRYhGib3aw60jhjI8YC8E6ke39Y3grRp-r-dbyFf2oTM3n9qu7W1ORyHl; sess-at-main="OT0rBoPnlfNr8TAm4g1gRTbAl3SUAPJgdO1rBjezL6A="; sst-main=Sst1|PQEjLgOr0pxtEw-FV69xyGxaCWQoXqH75cLf7rqBtPBlVWNxD0BaQo-oAarLiTFlOpz0tfyMaK2VsUa38BmfABZLVNdrXxl3sOV0cC9YwHWjjEbZGZwypOhJEoO8olbpBkf9oWtVCepRuTv6HMCPT1inEV5eYqp3aYnoYoKd1vTb4R3-CEYKCzUrZri3iMoOe-ELGQeztT1YqWIBr8CHPX4KdliBff52Tx0F7rmxmVEOfAqg_aye4RsjTYg_zqLqwn39I075aQLjBlFNiFZJcesnKiGIy6aoiCBwnYgOfBvDj6Q; lc-main=en_US; session-id-time=2082787201l; i18n-prefs=USD; session-token=CPXZ5JqiSCIayK/yWxfobc7L6X3CJlKcjcHjzkmno4ThtG8ITEYXNodNIZk194JJWFrxrls+wtKrv7lZ2GdpNjRrYayDud5JpbZlZXh44v/Ec9+RYKFD744GWztlbj4q+5ui2+NGRLNfSv0dzAjNop57HHH+MBH6yk6YTxBvsYvz2yVU+xD4dUgkDrASP6pmrU2Fj8gt7YxeZDytfLysjhtd9L4X0U9eiGRiu5gCAYWwm7EMYtyx7fZsvqr1YPnA; skin=noskin; csm-hit=tb:1NN3K71ZCYTMH7DDNVPT+sa-RK24R24EV102T10P3H24-B65BD16GBTM95B2T6GEA|1669877343088&t:1669877343088&adb:adblk_no',
    'Accept-Language': 'en-US,en;q=0.9,it;q=0.8,es;q=0.7'}
r = requests.get(URL, headers=headers)
print(r.status_code)
#print(r.content)

soup = BeautifulSoup(r.content, 'html.parser')
orders = soup.findAll(class_="g-item-details")

total = 0.0
cnt = 0
#max=0
rating_list = []
for order in orders:
    if cnt == 5:
        break
    cnt+=1

    price = str(order.find("span",class_="a-offscreen").text).strip()
    rating = str(order.find("span",class_="a-icon-alt").text).strip()
    #rating=int(rating.replace(",",""))
    #print(float(rating))
    rating_list.append(rating)


    price = price[1:]  # remove first element of string
    total +=float(price)
    min_rating = "MIN-RATING IS:" + " " + min(rating_list)

total="TOTAL  AMOUNT IS:" + " " + str(total)
print(total)
print(min_rating)

base=os.path.dirname(os.path.abspath(__file__))
html=open(os.path.join(base, "Neww.html"))
soup1=BeautifulSoup(html, "html.parser")
old_text = soup1.find("div", {"role": "heading"})
# print(old_text)

new_text = old_text.find(text=re.compile(
    'Your Lists')).replace_with(total,min_rating)


#Alter HTML file to see the changes done
with open("Neww.html", "wb") as f_output:
    f_output.write(soup1.prettify("utf-8"))

webbrowser.open('file://' + os.path.realpath("Macintosh HD:Users\Araks\\Desktop\\AGBU\\WorkPythonfiles\\new.html"))



