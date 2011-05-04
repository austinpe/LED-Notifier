import urllib
import BeautifulSoup 

url = BeautifulSoup.BeautifulSoup(urllib.urlopen("URL"))
table = url.find('table')
rows = table.findAll('tr')
text_initial = []
text_current = []
    
for tr in rows:
    cols = tr.findAll('td')
    for td in cols:
        text_initial.append(td.find(text=True))

def android_refresh():
    global text_initial
    global text_current
    url = BeautifulSoup.BeautifulSoup(urllib.urlopen("URL"))
    table = url.find('table')
    rows = table.findAll('tr')
    for tr in rows:
        cols = tr.findAll('td')
        for td in cols:
            text_current.append(td.find(text=True))
    
    if text_current[1] != text_initial[1]:
        url = ''
        table = ''
        rows = ''
        cols = ''
        text_initial = text_current
        return text_initial[1]
    text_current = []
    return None


    




        
