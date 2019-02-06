
workbook = xlsxwriter.Workbook('Praktiker2.xlsx')
worksheet = workbook.add_worksheet()
def pars(max_pages):
    page=1
    row = 0
    col = 0
    while page<=max_pages:
        url='http://ua-praktiker.com/ru/catalog_instrumenty/filter/page='+str(page)
        source_code = requests.get(url)
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': 'product_description'}):
           title = link.string
           href = "http://ua-praktiker.com" + link.get('href')
           worksheet.write(row, col,title)
           worksheet.write(row, col+1,href)
           row += 1
        for brand in soup.findAll('a', {'class': "product_brand"}):
           br=brand.string
           worksheet.write(row, col+2,br)
           row += 1
        for item_price in soup.findAll('div', {'class': 'short_price'}):
           b=re.findall('[-+]?[0-9]*\.?[0-9]+', str(item_price))
           str1 = ''.join(b)
           worksheet.write(row, col+3, str1)
           row += 1
        print ("Page:", page)
        page+=1
    print ("Done")
    workbook.close()

pars()
