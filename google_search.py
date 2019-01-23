#! python3
# google_search.py Opens several Google search results.

import requests, sys, webbrowser, bs4

if len(sys.argv)>1:
    res = requests.get('https://www.google.co.in/search?q' + ' '.join(sys.argv[1:]))
    res.raise_for_status()

#retrieve top search result links
soup = bs4.BeautifulSoup(res.text, features='html.parser')

#Open a browser tab for each result
linkElems = soup.select('.r a ')
numOpen = min(5, len(linkElems))

for i in range(numOpen):
    webbrowser.open('http://google.com'+linkElems[i].get('href'))
