import  scrapy

class postScrapy(scrapy.Spider):
    name = 'products'
    allowed_domains = ['www.incidecoder.com']

    start_urls = [
        # 'https://incidecoder.com/products/all?offset=1/'
        'https://incidecoder.com/products/100-pure-deep-hydration-sheet-mask'
    ]

# getting file name
#response.url.split('?')[0].split('/')[-1]
    def parse(self, response):
        # products = response.xpath('//div[@class="paddingb60"]//a/@href').getall()

        # for product in products:
        #     product_link = 'https://incidecoder.com'+product  
        #     yield {
        #         'products_link':product_link
        #     }

        product_mark = response.xpath("//div[@class='fs21']//span//a/text()").get()
        product_name = response.xpath('//div[@class="klavikab lilac"]//span/text()').get()

        yield{
            'product_mark':product_mark
        }

        product_image = response.xpath('//div[@class="image imgborder"]/picture//img/@src').getall()
        yield response.follow(
            url = product_image,
            callback=self.img_scrape
        )
    def img_scrape(self, response):

        filename = response.url.split('?')[0].split('/')[-1]
        print()
        with open(filename,'wb') as f:
            f.write(response.body)

        
        # filename = 'posts.html'

        # with open(filename, 'wb') as f:
        #     f.write(response.body)


# response.css('title::text').get()