from parsel import Selector
import requests

class NewsScraper:
  URL = "https://www.prnewswire.com/news-releases/news-releases-list/"
  LINK_XPATH = '//div[@class="row newsCards"]/div/a@href'
  PLUS_URL = 'https://www.prnewswire.com'

  def parse_date(self):
    html = requests.get(url=self.URL).text
    tree = Selector(text=html)
    links = tree.xpath(self.LINK_XPATH).extract()
    for link in links:
      print(self.PLUS_URL + link)



if __name__ == "__main__":
    scraper = NewsScraper()
    scraper.parse_date()
