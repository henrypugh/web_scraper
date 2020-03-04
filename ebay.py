from bs4 import BeautifulSoup
import re

with open('ebay.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
    
# Dictionary for product information on current page      
d = {}
try:
    pattern = re.compile('EAN:')
    result = soup.find('td', text=pattern, attrs={'class' : 'attrLabels'})
    EAN = result.parent.span.text
    d['EAN'] = EAN 
except AttributeError as e:
    print("No EAN number for this item.")    
 
# Dictionary for recommended products on current page
rd = {}
rec_products = soup.find_all('li', class_='mfe-reco-ct')
for product in rec_products:
    link = product.a['href']
    title = product.find('div', class_='mfe-title')['data-orig-text']
    condition = product['data-condition']
    rd[title] = {}
    rd[title]['title'] = title
    rd[title]['link'] = link
    rd[title]['condition'] = condition
    