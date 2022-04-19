import asyncio
import aiohttp 
from bs4 import BeautifulSoup
import time 
import logging
class AsnycGrab(object):
    # Constructor function for Async Grab.
    # Initializes the URLS of an object of Async Grab to the list of URLS P
    # called Name of the List of URLS: url_list
    # Maximum number of threads are set by the paraneter: max_threads The results of the crawl aro added to a dictionary: results
    def __init__(self, url_list, max_threads):
        self.urls = url_list
        self.results = {}
        self.max_threads = max_threads
    # -parse_results will use Beautifulsoup which is a scraping module
    # Beautiful Soup will scrape the content of the html document mentioned
    def __parse_results(self, url, html):
        try:
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.find('title').get_text()
        except Exception as e:
            raise e
        if title:
            self.results[url] = title
    # ...
    # getbody (set.url) is an asynchronous coroutine that will create a cli The session will fetch the URL with timeout set as 3 asynchronously.
    # get bady (self.url) is an asynchronous coroutine that will create a client session. The session will fetch the URL with timeout set as 3s asynchronously The event loop can go on to execute other threads while the coroutine anais for reading the Return values: URL for response and HTML content for body.
    # ... 
    async def get_body(self, url): 
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=30) as response: 
                assert response.status == 200
                html = await response.read()
                return response.url, html
    # ...
    # get reaultsiself, url) is an asynchronous function that awaits for self.get body to return the After returning the HTML und URL, 1 returns 'Completed as a sign for completing the Crawling ..
    # handle tasks is also an asynchronous function that fetches the first task from the work If the result of self.get results(url) is Completed then we store it in zask status Els the exception is logged.
    # ...
    async def get_results(self, url):
        url, html = await self.get_body(url) 
        self.__parse_results(url, html) 
        return 'Completed'
    async def handle_tasks(self, task_id, work_queue): 
        while not work_queue.empty(): 
            current_url = await work_queue.get()
            try: 
                task_status = await self.get_results(current_url) 
            except Exception as e:
                logging.exception('Error for {}'.format(current_url),exc_info=True)
    
    #event loop( creates a queue and adds the tasks to the queen the loop will keep on running till all the taskS are executed.
    
    def eventloop(self):
        q = asyncio.Queue()
        [q.put_nowait(url) for url in self.urls]
        loop = asyncio.get_event_loop()
        tasks= [self.handle_tasks(task_id, q, ) for task_id in range(self.max_threads)] 
        loop.run_until_complete(asyncio.wait(tasks)) 
        loop.close()
    #Main Function
if __name__ == '__main__':
    q=time.time()
    async_example = AsnycGrab([
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
    async_example.eventloop()
    q1=time.time()
    for key,val in async_example.results.items():
        print(str(key)+": "+str(val))
print("Time taken to crawl the pages: "+ str(q1-q))
