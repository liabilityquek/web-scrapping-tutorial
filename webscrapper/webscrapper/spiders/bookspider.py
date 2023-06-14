import scrapy
from webscrapper.items import BookItem
import random
import os
from dotenv import load_dotenv
from urllib.parse import urlencode
load_dotenv()

API_KEY = os.getenv('API_KEY')

class BookspiderSpider(scrapy.Spider):
    name = 'bookspider'
    allowed_domains = ['books.toscrape.com', 'proxy.scrapeops.io']
    start_urls = ['https://books.toscrape.com/']
    
    # saving data into a json format
    custom_settings = {
        'FEEDS': { 'bookdata.json': { 'format': 'json',}}
        }
    
    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)
   

    def parse(self, response):
        books = response.css('article.product_pod')
        for book in books:
            individual_book_url = book.css('h3 a ::attr(href)').get()
            
            if 'catalogue/' in individual_book_url:
                book_url = 'https://books.toscrape.com/' + individual_book_url
            else:
                book_url = 'https://books.toscrape.com/catalogue/' + individual_book_url
            yield scrapy.Request(url=book_url, callback=self.parse_book_page)
        
        next_page = response.css('li.next a ::attr(href)').get()
        
        if next_page is not None:
            if 'catalogue/' in next_page:
                next_page_url = 'https://books.toscrape.com/' + next_page
            else:
                next_page_url = 'https://books.toscrape.com/catalogue/' + next_page
            yield scrapy.Request(url=next_page_url, callback=self.parse)
            
    def parse_book_page(self, response):
        table_row = response.css("table tr")
        book_item = BookItem()
        
        book_item['url'] = response.url
        book_item['title'] = response.css('.product_main h1::text').get()
        book_item['upc'] = table_row[0].css('td ::text').get()
        book_item['product_type'] = table_row[1].css('td ::text').get()
        book_item['price_excl_tax'] = table_row[2].css('td ::text').get()
        book_item['price_incl_tax'] = table_row[3].css('td ::text').get()
        book_item['tax'] = table_row[4].css('td ::text').get()
        book_item['availability'] = table_row[5].css('td ::text').get()
        book_item['num_reviews'] = table_row[6].css('td ::text').get()
        book_item['stars'] = response.css("p.star-rating").attrib['class']
        book_item['category'] = response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get()
        book_item['description'] = response.xpath("//div[@id='product_description']/following-sibling::p/text()").get()
        book_item['price'] = response.css('p.price_color ::text').get()
            
        yield book_item

        
