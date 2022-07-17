from asyncio.windows_events import NULL
from contextlib import nullcontext
from turtle import fillcolor
import requests
from bs4 import BeautifulSoup
import concurrent.futures
import re



output_file=open('output.txt', 'w')


maxPageCount = 10
itemCounter = 1

CarList={}

def getTitle(Link):
    itemlink=Link['href']

    newPage = BeautifulSoup(requests.get(itemlink).content, "lxml");
    title_div=newPage.find_all('h1',class_="offer-title big-text")
    title_string=str(title_div)
    title_list=title_string.split('h1')

    if len(title_list)>1:

        car_title=title_list[1][60:].split('<')[0].strip()

        CarList[itemlink]=car_title

        stringReturn= car_title + '\n' + itemlink

        return stringReturn

    else: return 0


def getPage(page):
    global itemCounter
    soup = BeautifulSoup(requests.get(page).content, "lxml");
    allLinks = soup.find_all("a", class_='', href=True)

    results = concurrent.futures.ThreadPoolExecutor().map(getTitle, allLinks)
    for result in results:
        try:
            print(result)
            itemCounter += 1
        except:
            continue

with concurrent.futures.ThreadPoolExecutor() as executor:
  pages = []
  for count in range(1, maxPageCount + 1):
    pages.append(f"https://www.autovit.ro/autoturisme?page={count}")
    

  pageResults = executor.map(getPage, pages)


CarListSorted=dict(sorted(CarList.items(), key=lambda item: item[1]))

ctr=0;

for i in CarListSorted:
    # search for all bmw 3-series, 4-series, 5-series, 6-series and 7-series and all SUVs
    item1=re.search(r"[Bb][Mm][Ww] (([Ss]eria [3-7])|([Xx][1-6]))", CarListSorted[i])

    # search for all mercedes GL-SUVs, CL models and E-class, C-class and S-class
    item2=re.search(r"[Mm]ercedes(?:-[Bb]enz) ((GL[CES]) | (CL[ES]) | ([eEcCsS][\s*-][cC]lass))", CarListSorted[i])

    # search for all audi a4, a5, a6, a7, a8
    item3=re.search(r"[Aa]udi [Aa][4-8]", CarListSorted[i])

    if item2 or item3 or item1:
        output_file.write(str(CarListSorted[i]) + '\n'+ str(i) + '\n')
        
