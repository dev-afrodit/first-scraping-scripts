# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductsdataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# https://www.skincarisma.com/products/analyze?utf8=%E2%9C%93&product%5Bingredient%5D=
# Organic+Rosa+Centifolia+%28Rose%29+Flower+Water%2C+Organic+Salvia+Hispanica+%28Chia%29+Seed+Oil%2C+Organic+Cocos+Nucifera+%28Coconut%29+Oil%2C+Organic+Opuntia+Ficus-Indica+%28Nopal+Cactus%29+Extract%2C+Xanthan+Gum%2C+Panthenol%2C+Sodium+PCA%2C+Hyaluronic+Acid%2C+Organic+Butyrospermum+Parkii+%28Shea+Butter%29%2C+Organic+Lonicera+Japonica+%28Honeysuckle%29+Flower+Extract%2C+Glyceryl+Stearate%2C+Cetearyl+Alcohol%2C+Sodium+Stearoyl+Lactylate%2C+Organic+Essential+Oils%2C+Citrus+Aurantium+Bergamia+%28Bergamot%29+Fruit+Oil%2C+Cedrus+Atlantica+%28Cedarwood%29+Bark+Oil%2C+Vetiveria+Zizanoides+%28Vetiver%29+Root+Oil%2C+Citrus+Sinensis+%28Blood+Orange%29+Oil%2C+Salvia+Officinalis+%28Sage%29+Oil%2C+Lavandula+Angustifolia+%28Lavender%29+Oil
# https://www.skincarisma.com/products/analyze?utf8=&product%5Bingredient%5D=Water%2C+Ethoxydiglycol

# %E2%9C%93&product%5Bingredient%5D
# &product%5Bingredient%5D
# https://www.skincarisma.com/products/analyze?utf8=%E2%9C%93&product%5Bingredient%5D=Water%2CEthoxydiglycol
# https://www.skincarisma.com/products/analyze?utf8=&product%5Bingredient%5D=
# Water%2CEthoxydiglycol
# Water, Ethoxydiglycol


#? getting progress bar dat
#a = response.xpath('//div[@class="progress progress-ewg mt-4"]/div/text()')
#*for i in a: data.append(i.get().strip())