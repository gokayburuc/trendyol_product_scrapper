from requests import get 
from bs4 import BeautifulSoup 
from urllib.parse import urlparse, quote, parse_qs, urljoin

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36'}
baseurl = 'https://www.trendyol.com/sr?wb=254&qt=casio&st=casio&lc=34&os=1'

try: 
    status = get(baseurl, headers=headers).status_code
    print(status)

content = get(baseurl, headers = headers).content 
my_object = BeautifulSoup(content, 'lxml')

products = my_object.find_all('div', class_ = "prdct-desc-cntnr-wrppr")

# TODO:  23 Adet statik sonuç getiriyor. Bunu Dinamik sonuç getirecek hale getirmek gerekiyor. 

productlist = []
for p in products:
    try:
        price = p.find("div", class_ = "prc-box-dscntd").text
        rating = p.find("span",class_ = "ratingCount").text
        brand = p.find("span",class_ = "prdct-desc-cntnr-ttl").text
        productname = p.find("span",class_ ="prdct-desc-cntnr-name hasRatings").text
        row = [brand,productname,price,rating]
        productlist.append(row)
        print(row)
    except:
        pass