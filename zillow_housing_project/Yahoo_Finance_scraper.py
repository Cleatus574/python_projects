import requests as req
from bs4 import BeautifulSoup

#url = "https://rocketleague.tracker.network/rocket-league/profile/epic/bro.ro711/overview"
url = "https://finance.yahoo.com/quote/MSFT?p=MSFT&.tsrc=fin-srch"
r = req.get(url)
soup = BeautifulSoup(r.content, 'lxml')
divs = soup.find('div', {'class':'Py(10px) Pstart(10px)'}).('span')[0].text

#spans = soup.find_all('span')
#soup.find_all('span')

#print(soup.prettify())

print(divs)

# Full table parent tag : id="Col1-1-HistoricalDataTable-Proxy"
#Header of table class="C($tertiaryColor) Fz(xs) Ta(end)"
#First column(Date) first row : class="Py(10px) Pstart(10px)"
#class="W(100%) M(0)"

#html_text = """<span data-v-04d83064="" class="value">1,224</span>"""

#html = BeautifulSoup(html_text, "lxml")

#spans = html.find_all('span', {'class': 'value'})

#for span in spans:
 #   print(span.text)

