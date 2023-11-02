from parsel import Selector
import requests

class MoviesScraper:

  URL = "https://doramy.club/filmy"
  LINK_XPATH = '//section[@class="post-list"]/div/a/@href'
  PlUS_URL = 'https://doramy.club/'
  def parse_date(self):
    html = requests.get(url=self.URL).text
    tree = Selector(text=html)
    links = tree.xpath(self.LINK_XPATH).extract()
    for link in links:
      print(link)
    return links[:5]




if __name__ == "__main__":
    scraper = MoviesScraper()
    scraper.parse_date()


