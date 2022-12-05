import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta

def bit_crawl():

    yesterday = date.today() - timedelta(3)
    yd = yesterday.strftime("%Y%m%d")

    name, marketCap, price, circulatingSupply, symbol = [], [], [], [], []

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
            
            # Circulating supply and symbol            
            circulatingSupplySymbol = row.find('td', attrs={'class':'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__circulating-supply'}).text.strip()
            supply = circulatingSupplySymbol.split(' ')[0]
            sym = circulatingSupplySymbol.split(' ')[1]
            # append the data
            name.append(cryptoname)
            marketCap.append(marketcap)
            price.append(crytoprice)
            circulatingSupply.append(supply)
            symbol.append(sym)

    for i in range(11):
        print(i, yd[i], name[i], price[i], symbol[i], '\n')  

    return yd, name, marketCap, price, circulatingSupply, symbol

    '''
    for i in [name, marketCap, price, circulatingSupply, symbol]:
        print(i,'\n')
    '''


if __name__ == "__main__":
    bit_crawl() 