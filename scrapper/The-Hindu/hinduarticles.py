from bs4 import BeautifulSoup
from requests import get
import numpy as np

def hinduarticles(url,filename):
    page_number=1
    headUrl="https://www.thehindu.com/"
    
    match_links=[]
    links_final=[]
    for x in range(1,50):
        Url = url + '?page='+ str(x)
        
        print(Url)
        soup = BeautifulSoup(get(Url).text, 'lxml')
        
        # match_links=[]
        # match_links=set()
        # with open(filename,'a',encoding='utf8') as file:
            # links = [div for div in soup.findAll('div', attrs={'class':'Other-StoryCard'})]
        links = [div for div in soup.findAll('div', attrs={'class':'container'})]
            # print(links)
            # break
            # print(links)
        for div in links:
            Div = [div for div in div.findAll('h3')]
            for h in Div:
                    if match_links.count(h.a['href'])==0:
                    # if h.a['href'] not in match_links:
                     match_links.append(h.a['href'])
                    # print(h.a['href'])
                    # match_links.update(str(h.a['href']))
            
            print(len(match_links))
            links_final = np.unique(match_links)
            print(len(links_final))
            # print(match_links, "\n")
            # for i in links_final:
            #     # print(i, sep = "\n")
            #     file.write(i+"\n")
                #+"\n"
            # break
    with open(filename,'a',encoding='utf8') as file:
     print(x)
     for i in links_final:
                # print(i, sep = "\n")
                file.write(i+"\n")
    
    



with open('sitemaps.txt', encoding = 'utf8') as file:
    counter = 1
    for url in file:
        # print(url.strip())
        hinduarticles(url.strip(), 'hinduarticles/link'+str(counter)+".txt")
        counter = counter + 1