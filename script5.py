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
"https://www.amazon.jobs/en-gb/"],5)
    async_example.eventloop()
    q1=time.time()
    for key,val in async_example.results.items():
        print(str(key)+": "+str(val))
print("Time taken to crawl the pages: "+ str(q1-q))
