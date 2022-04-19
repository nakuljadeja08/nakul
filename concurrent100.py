from concurrent.futures import ThreadPoolExecutor
import time
import requests
from bs4 import BeautifulSoup

class ConcurrentListCrawler(object):

    def __init__(self,url_list, threads): 
        self.urls = url_list 
        self.results={}
        self.max_threads = threads
        print("Number of threads "+str(self.max_threads))

    def __make_request(self, url): 
        try:
            r=requests.get(url=url, timeout=20)
            r.raise_for_status() 
        except requests.exceptions. Timeout:
            r = requests.get(url=url, timeout=60) 
        except requests.exceptions.ConnectionError:

            r = requests.get(url-query, timeout=60)

        except requests.exceptions.RequestException as e:
            raise e

        return r.url, r.text

    def __parse_results(self, url, html): 
        try:
            soup = BeautifulSoup(html, 'html.parser') 
            title = soup.find('title').get_text() 
        except Exception as e:

            raise e

        if title: 
            self.results[url]=title

    def wrapper(self, url):

        url, html=self.__make_request(url)
        self.__parse_results(url, html)

    def run_script(self):
        with ThreadPoolExecutor(max_workers=min(len(self.urls),self.max_threads)) as Executor:
             jobs=[Executor.submit(self.wrapper, u) for u in self.urls]

if __name__ =='__main__':
    q=time.time ()
    example = ConcurrentListCrawler(["https://timesofindia.indiatimes.com/defaultinterstitial.cms",
"https://www.theguardian.com/international",
"https://www.apple.com/in/?afid=p238%7CsdUuvv563-dc_mtid_187079nc38483_pcrid_474706300243_pgrid_109516736379_&cid=aos-IN-kwgo-brand--slid---product-",
"https://www.samsung.com/in/",
"https://www.amazon.jobs/en-gb/",
"https://www.fidelity.com/",
"https://www.fidelity.com/news/overview",
"https://www.amazon.jobs/en-gb/faqs",
"https://www.maybelline.com/",
"https://www.nykaa.com/skin/c/8377?root=nav_1&dir=desc&order=popularity",
"https://www.nykaa.com/best-wellness-products-online-sale?root=nav_1&dir=desc&order=popularity",
"https://www.myntra.com/shop/women",
"https://vit.ac.in/",
"https://vtop.vit.ac.in/vtop/initialProcess",
"https://practice.geeksforgeeks.org/problems/count-the-zeros2550/1/?company[]=Amazon&difficulty[]=0&page=1&query=company[]Amazondifficulty[]0page1",
"https://en.wikipedia.org/wiki/Taylor_Swift",
"https://en.wikipedia.org/wiki/Billboard_200",
"https://en.wikipedia.org/wiki/Calliotropis_solomonensis",
"https://en.wikipedia.org/wiki/Antonio_Morelli",
"https://en.wikipedia.org/wiki/Harry_Styles",
"https://en.wikipedia.org/wiki/One_Direction",
"https://en.wikipedia.org/wiki/Louis_Tomlinson",
"https://en.wikipedia.org/wiki/Liam_Payne",
"https://en.wikipedia.org/wiki/Niall_Horan",
"https://en.wikipedia.org/wiki/Zayn_Malik",
"https://en.wikipedia.org/wiki/Ostro%C5%82%C4%99ka_railway_station",
"https://en.wikipedia.org/wiki/Ezekiel_35",
"https://en.wikipedia.org/wiki/Canela_Preta_Biological_Reserve"
"https://en.wikipedia.org/wiki/Kavali,_Srikakulam_district",
"https://en.wikipedia.org/wiki/Satch_and_Josh...Again",
"https://en.wikipedia.org/wiki/Joe_Walker_(Zydeco)",
"https://en.wikipedia.org/wiki/Der_Preis_f%C3%BCrs_%C3%9Cberleben",
"https://en.wikipedia.org/wiki/Sacramento_High_School",
"https://en.wikipedia.org/wiki/Cathy_Crowe",
"https://en.wikipedia.org/wiki/Maisons,_Calvados",
"https://en.wikipedia.org/wiki/Lisa_M._Dugan",
"https://en.wikipedia.org/wiki/E._K._T._Sivakumar",
"https://en.wikipedia.org/wiki/Julian_Hoke_Harris",
"https://en.wikipedia.org/wiki/Paul_Sample_(ice_hockey)",
"https://en.wikipedia.org/wiki/1_Regiment_Army_Air_Corps",
"https://en.wikipedia.org/wiki/Botwood",
"https://en.wikipedia.org/wiki/Phil_Morton",
"https://en.wikipedia.org/wiki/Biddulph_Moor",
"https://en.wikipedia.org/wiki/List_of_PC_games_(Q)",
"https://en.wikipedia.org/wiki/Pouillet_effect",
"https://en.wikipedia.org/wiki/Par%C4%85dzice",
"https://en.wikipedia.org/wiki/Drobyazkin",
"https://en.wikipedia.org/wiki/2006_Nyk%C3%B6ping_municipal_election",
"https://en.wikipedia.org/wiki/British-American_Institute",
"https://en.wikipedia.org/wiki/Sweet_Falls",
"https://timesofindia.indiatimes.com/defaultinterstitial.cms",
"https://www.theguardian.com/international",
"https://www.apple.com/in/?afid=p238%7CsdUuvv563-dc_mtid_187079nc38483_pcrid_474706300243_pgrid_109516736379_&cid=aos-IN-kwgo-brand--slid---product-",
"https://www.samsung.com/in/",
"https://www.amazon.jobs/en-gb/",
"https://www.fidelity.com/",
"https://www.fidelity.com/news/overview",
"https://www.amazon.jobs/en-gb/faqs",
"https://www.maybelline.com/",
"https://www.nykaa.com/skin/c/8377?root=nav_1&dir=desc&order=popularity",
"https://www.nykaa.com/best-wellness-products-online-sale?root=nav_1&dir=desc&order=popularity",
"https://www.myntra.com/shop/women",
"https://vit.ac.in/",
"https://vtop.vit.ac.in/vtop/initialProcess",
"https://practice.geeksforgeeks.org/problems/count-the-zeros2550/1/?company[]=Amazon&difficulty[]=0&page=1&query=company[]Amazondifficulty[]0page1",
"https://en.wikipedia.org/wiki/Taylor_Swift",
"https://en.wikipedia.org/wiki/Billboard_200",
"https://en.wikipedia.org/wiki/Calliotropis_solomonensis",
"https://en.wikipedia.org/wiki/Antonio_Morelli",
"https://en.wikipedia.org/wiki/Harry_Styles",
"https://en.wikipedia.org/wiki/One_Direction",
"https://en.wikipedia.org/wiki/Louis_Tomlinson",
"https://en.wikipedia.org/wiki/Liam_Payne",
"https://en.wikipedia.org/wiki/Niall_Horan",
"https://en.wikipedia.org/wiki/Zayn_Malik",
"https://en.wikipedia.org/wiki/Ostro%C5%82%C4%99ka_railway_station",
"https://en.wikipedia.org/wiki/Ezekiel_35",
"https://en.wikipedia.org/wiki/Canela_Preta_Biological_Reserve"
"https://en.wikipedia.org/wiki/Kavali,_Srikakulam_district",
"https://en.wikipedia.org/wiki/Satch_and_Josh...Again",
"https://en.wikipedia.org/wiki/Joe_Walker_(Zydeco)",
"https://en.wikipedia.org/wiki/Der_Preis_f%C3%BCrs_%C3%9Cberleben",
"https://en.wikipedia.org/wiki/Sacramento_High_School",
"https://en.wikipedia.org/wiki/Cathy_Crowe",
"https://en.wikipedia.org/wiki/Maisons,_Calvados",
"https://en.wikipedia.org/wiki/Lisa_M._Dugan",
"https://en.wikipedia.org/wiki/E._K._T._Sivakumar",
"https://en.wikipedia.org/wiki/Julian_Hoke_Harris",
"https://en.wikipedia.org/wiki/Paul_Sample_(ice_hockey)",
"https://en.wikipedia.org/wiki/1_Regiment_Army_Air_Corps",
"https://en.wikipedia.org/wiki/Botwood",
"https://en.wikipedia.org/wiki/Phil_Morton",
"https://en.wikipedia.org/wiki/Biddulph_Moor",
"https://en.wikipedia.org/wiki/List_of_PC_games_(Q)",
"https://en.wikipedia.org/wiki/Pouillet_effect",
"https://en.wikipedia.org/wiki/Par%C4%85dzice",
"https://en.wikipedia.org/wiki/Drobyazkin",
"https://en.wikipedia.org/wiki/2006_Nyk%C3%B6ping_municipal_election",
"https://en.wikipedia.org/wiki/British-American_Institute",
"https://en.wikipedia.org/wiki/Sweet_Falls"],25)
    example.run_script()
    q1=time.time()

#print(example, results)
    for key, val in example.results.items (): 
       print (key+": "+val)
    print("Time taken to crawl the given web pages: "+str(q1-q))
