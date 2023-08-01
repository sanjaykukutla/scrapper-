from os import link
from bs4 import BeautifulSoup
from requests import get

def domains(url, filename):
    headUrl="https://www.thehindu.com/"
    soup = BeautifulSoup(get(url).text, 'lxml')
    
    with open(filename, 'w', encoding='utf8') as file:
        site_maps=[]
        
        
        # links = [ul for ul in soup.findAll('ul', attrs={'class':'sub-menu'})]
        links = [ul for ul in soup.findAll('ul', attrs={'class':'sub-menu'})]
        print(links)
        for ul in links:
          Li = [li.a for li in ul.findAll('li')]
          # print(Li)
          for li in Li:
          #print(hasattr(li, 'href'))
           #print(li)
           try:
             if(hasattr(li, 'href')):
                if "sport" in li["href"]:
                 site_maps.append(li['href'])
           except TypeError:
                    print("Type error occured")
           except KeyError:
                    print("Key error occured")
        
        for i in site_maps:
            file.write(i+"\n")
            
domains("https://www.thehindu.com/", "sitemaps1.txt")
                    