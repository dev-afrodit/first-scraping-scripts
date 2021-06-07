from scrapy import Spider
from scrapy.http import Request
import w3lib.html
import re
import unicodedata

class ProductSpider(Spider):
    name ="products_2"
    allowed_domains = ['incidecoder.com']
    start_urls = ['https://incidecoder.com/products/all?offset=1']

    def parse(self, response):
        products = response.xpath('//div[@class="paddingb60"]//a/@href').extract()
        # absolute_url = response.urljoin(products[0])
        # yield Request(absolute_url, callback=self.parse_products)
        for product in products:
            # product_link = 'https://incidecoder.com'+product
            absolute_url = response.urljoin(product)
            yield Request(absolute_url, callback=self.parse_products, errback=self.handdleErrors)
        
        #proccessing to next page
        next_page = response.xpath("//div[@class='center fs16']//a[2]/@href").extract_first()
        absolute_next_url = response.urljoin(next_page)
        yield Request(absolute_next_url)

    def parse_products(self, response):

        # & Prodcuts
        title = response.xpath('.//span[@id="product-title"]/text()').extract_first()
        mark = response.xpath('.//a[@class="underline"]/text()').extract_first()
        image = response.xpath('.//div[@id="product-main-image"]//img/@src').extract_first()

        #!ingridients
        # # ingridients name
        # ingridient_names= {}
        ingridients_list = response.xpath("//span[@role='listitem']/a/text()").extract()
        # ingridient_names[title] = ingridients
        # yield{
        #     'product_name':title,
        #     'ingridients_list':ingridients
        # }
        ingridient_details= []
        # ingridients_name_list = response.xpath('//a[@class="product-long-ingred-link cardingtitle klavikab fs22 lilac"]/text()').extract()
        # for ingr in ingridients_name_list:
        #     ingridient_names.append(ingr)
        ingridients_details = response.xpath('//*[@class="ingreddescbox"]')
        details = {}
        for data in range(len(ingridients_details)):
            datas = ingridients_details[data].extract()
            remove_Tag = w3lib.html.remove_tags(datas)
            de_encode = unicodedata.normalize("NFD",remove_Tag);
            x = re.findall("\r\n\r\n|\r\n|\n|\r|Expand to read more  ", de_encode)
            clean = ''
            for pattern in x:
                clean = de_encode.replace(pattern,'')
            details[ingridients_list[data]]= " ".join(clean.split())
        # join_ingridients = list(zip(ingridient_names, details))
        yield{
            'product_name':title,
            'product_mark':mark,
            'image_url':image,
            'ingridients_list':ingridients_list,
            'ingridients_details':details

        }
        # for ingridient in ingridients_details:
        #     p_tags = ingridient.xpath('.//p').extract()
        #     detail = ''
        #     for p in p_tags:
        #         detail += w3lib.html.remove_tags(p.strip())
        #     details.append(detail)
        # ingridient_details.append(details)

        # # print("#######")
        # # print(ingridient_names)
        # # print(ingridient_details)
        # join_ingridients = list(zip(ingridient_names, ingridient_details))
        # # yield {
        # #             # 'product_name':title,
        # #             # 'mark':mark,
        # #             # 'image_url':image,
        # #             'ingridients':join_ingridients
        # #         }
        # yield{
        #     'ingridients':join_ingridients
        # }
        # ingridient_name_url = response.xpath('.//a[@class="product-long-ingred-link cardingtitle klavikab fs22 lilac"]/@href').extract()
        
        # for ingridient in ingridient_name_url:
        #     absolute_ing_url = response.urljoin(ingridient)
            # ingridient_name = ingridient
            # details = response.xpath('.//div[@class="ingreddescbox"]//p').getall()
            # for detail in details:

                # yield {
                #     # 'product_name':title,
                #     # 'mark':mark,
                #     # 'image_url':image,
                #     # 'ingridients':{
                #     #     'ingridient_name':ingridient_name,

                #     # }
                #     'details':detail.get()
                # }
            # yield Request(absolute_ing_url, callback=self.ingridient_parse, 
            # meta={
            #     'data' : {
            #     'product_name':title,
            #     'mark':mark,
            #     'image':image
            #     }
                
            # })
    def handdleErrors(self, response):
        f = open('collectErrors.txt','a',encoding="utf-8")
        f.write(response.url)
        f.write('\n')
        f.close()
        pass
    # def ingridient_parse(self, response):
    #     product_details = response.meta['data']
    #     name = response.xpath('//h1[@class="klavikab lilac "]/text()').get().strip()
    #     details = response.xpath('.//*[@id="showmore-section-details"]/div[1]//p').extract_first()
    #     details = ''.join(details)
    #     ingridients =  {
    #         'ingridient_name': name,
    #         'details':details
    #     }
    #     product_details['ingridients'] = ingridients
    #     yield{
    #         'product_details':product_details
    #     }
        
        
    
    
    # //a[contains(text(),'Next')]
    # //a[contains(text(),'Next')]//@href