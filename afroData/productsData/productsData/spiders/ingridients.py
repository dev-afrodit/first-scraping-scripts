import  scrapy
import pandas as pd
import json
import os
from scrapy import Request
class postScrapy(scrapy.Spider):
    name = 'ingridients'
    allowed_domains = ['https://www.skincarisma.com']
    # start_urls = handle_startRequest()

    # def handle_startRequest(self):
    #     base_url = "https://www.skincarisma.com/products/analyze?utf8=%E2%9C%93&product%5Bingredient%5D="
    #     df = pd.read_csv('first200.csv')
    #     start_urls = []
    #     for data in df['ingridients_list']:
    #         # data = df[i]
    #         transfrom_to_json = json.loads(data)
    #         # get this json data keys(it has one)
    #         key = list(transfrom_to_json.keys())[0]
    #         d = ','.join(transfrom_to_json[key])
    #         full_link = base_url+d
    #         start_urls.append(full_link)
    #         # product_name = key
    #     return start_urls
            # yield Request(base_url+d, self.parse,dont_filter=True, meta={'product_name':product_name})  
    def start_requests(self):
        # config of path
        json_data = None
        base_url = "https://www.skincarisma.com/products/analyze?utf8=%E2%9C%93&product%5Bingredient%5D="
        # df = pd.read_json('ProductsWithIngridients.json').to_dict()
        with open('ProductsWithIngridients.json', encoding='utf8') as f:
            #? to json
            data = json.load(f)
            for row in data:
                link = ','.join(row['ingridients_list'])
                if link:
                    url_format = base_url+link
                    image_url = row['image_url']
                    yield Request(url_format, self.parse,dont_filter=True, meta={'image_url':image_url}, errback=handdleErrors)
                else: # not runned yet
                    yield{
                        'image_url':row['image_url'],
                        'IngredientAnalysisResults':"Not result found",
                        'IngredientSafetyBreakdown':"Not result found",
                        'url':','.join(row['ingridients_list'])
                    }
        # df = pd.read_csv('test_dat.csv')
        # for i in len(df['first200.csv']):
        # for key, data in df.items():
        #     if data:
        #         url_format = base_url+data
        #         product_name = key
        #         yield Request(base_url+url_format, self.parse,dont_filter=True, meta={'product_name':product_name})
        #     else: # not runned yet
        #         yield{
        #             'product_name':key,
        #             'IngredientAnalysisResults':"Not result found",
        #             'IngredientSafetyBreakdown':"Not result found",
        #             'url':response.url
        #         }
        # for data in df.items():
        #     # data = df[i]
        #     try:
        #         transfrom_to_json = json.loads(data)
        #         # get this json data keys(it has one)
        #         key = list(transfrom_to_json.keys())[0]
        #         d = ','.join(transfrom_to_json[key])
        #         product_name = key
        #         yield Request(base_url+d, self.parse,dont_filter=True, meta={'product_name':product_name})
        #     except:
        #         error = data
        #         with open('notFoundDatas.txt', 'a') as f:
        #             f.write("%s" % error)

    def parse(self, response):
        image_url = response.meta['image_url'] 

        # Ingredient Safety Breakdown (EWG Health Ratings)
        progress_results = response.xpath('//div[@class="progress progress-ewg mt-4"]/div/text()')
        progresses = []
        keys = ['Low Risk','Moderate Risk','High Risk','Unknown']
        for i, value in enumerate(progress_results):
            progress = value.extract().strip()
            # progresses[keys[i]]= progress
            progresses.append((keys[i],progress))
        
        # getting Ingredient Analysis Results
        analyze_results = response.xpath('.//div[@class="col-md-3 my-2"]/a')
        in_ingridient = 'fa fa-check-square green-icon font-095'
        not_in_ingridient = 'fa fa-times grey-icon font-095'
        IngridientsAnalysisResults = []
        for result in analyze_results:
            result_text = result.xpath('./span/text()').extract()[0]
            result_contain= result.xpath('./i/@class').extract()[0]

            if result_contain==in_ingridient:
                IngridientsAnalysisResults.append((1,result_text))
            elif result_contain==not_in_ingridient:
                IngridientsAnalysisResults.append((0,result_text))


        yield {
            'image_url':image_url,
            'IngredientAnalysisResults':IngridientsAnalysisResults,
            'IngredientSafetyBreakdown':progresses

            
        }

def handdleErrors(self, response):
        f = open('collectErrors.txt','a',encoding="utf-8")
        f.write(response.url)
        f.write('\n')
        f.close()
        pass