import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta

def bit_crawl():

    yesterday = date.today() - timedelta(4)
    yd = yesterday.strftime("%Y%m%d")

    name, marketCap, price = [], [], []

    req  = requests.get('https://coinmarketcap.com/historical/'+yd+'/')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    tr = soup.find_all('tr', attrs={'class':'cmc-table-row'})

    count = 0
    
    for row in tr:
        if count == 10:
            break
        else:
            count += 1
            
            # Store name of the crypto currency            
            name_col = row.find('td', attrs={'class':'cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__name'})
            cryptoname = name_col.find('a', attrs={'class':'cmc-table__column-name--name cmc-link'}).text.strip()
            
            # Market cap
            marketcap = row.find('td', attrs={'class':'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__market-cap'}).text.strip()
            
            # Price
            crytoprice = row.find('td', attrs={'class':'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price'}).text.strip()
            
            # append the data
            name.append(cryptoname)
            marketCap.append(marketcap)
            price.append(crytoprice)

    for i in range(count):
        print(i+1, name[i], price[i], '\n')  

    return yd, name, marketCap, price

    '''
    for i in [name, marketCap, price, circulatingSupply, symbol]:
        print(i,'\n')
    '''



if __name__ == "__main__":
    bit_crawl() 