import requests
import time
from bs4 import BeautifulSoup

class GILBlocking(object):

    def __init__(self, url_list):

        self.urls = url_list
        self.results = {}

    def __make_request(self, url):
        try:
            r = requests.get(url=url, timeout=20)
            r.raise_for_status()
        except requests.exceptions.Timeout:
            r = requests.get(url=url, timeout=60)
        except requests.exceptions.ConnectionError:
            r = requests.get(url=url, timeout=60)
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
            self.results[url] = title

    def wrapper(self, url):
        url, html = self.__make_request(url)
        self.__parse_results(url, html)

    def get_results(self):
        for url in self.urls:
            try:
                self.wrapper(url)
            except:
                pass

if __name__ == '__main__':
    q=time.time()
    scraper = GILBlocking(["https://timesofindia.indiatimes.com/defaultinterstitial.cms",
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
"https://en.wikipedia.org/wiki/Zayn_Malik"])
    scraper.get_results()
    q1=time.time()
    for key,val in scraper.results.items():
        print(key+": "+val)
    print("The time taken to crawl the given web pages is: "+str(q1-q))
