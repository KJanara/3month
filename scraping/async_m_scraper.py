# import httpx
# from parsel import Selector
# import asyncio
#
#
# class NewMoviesScraper:
#   HEADERS = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
#     'Accept-Language': 'en-GB,en;q=0.5',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Connection': 'keep-alive'
#   }
#   URL = "https://doramy.club/filmy/page/{page}"
#   LINK_XPATH = '//section[@class="post-list"]/div/a/@href'
#   PlUS_URL = 'https://doramy.club/'
#   PAGE = '//a[@class="page-numbers"]/@href'
#
#   async def async_generator(self, limit):
#     for page in range(1, limit + 1):
#       yield page
#
#   async def parse_page(self):
#     async with httpx.AsyncClient(headers=self.HEADERS) as client:
#       async for page in self.async_generator(limit=5):
#         await self.get_url(
#           client=client,
#           url=self.URL.format(page=page)
#         )
#
#   async def get_url(self, client, url):
#     response = await client.get(url)
#     print(response.url)
#     await self.scraper_link(html=response.text, client=client)
#
#   async def scraper_link(self, html, client):
#     tree = Selector(text=html)
#     links = tree.xpath(self.LINK_XPATH).extract()
#     for link in links:
#       print(link)
#     return links[:5]
#
#
# if __name__ == "__main__":
#   scraper = NewMoviesScraper()
#   asyncio.run(scraper.parse_page())
