# -*- coding: utf-8 -*-
import scrapy


class EastasiaegSpider(scrapy.Spider):
    name = 'eastasiaeg'
    allowed_domains = ['eastasiaeg.com']
    page_num = 1
    start_first_page = 'false'
    payload = '{"categoryId":"4","manufacturerId":"0","vendorId":"0","priceRangeFilterModel7Spikes":{"CategoryId":"4","ManufacturerId":"0","VendorId":"0","SelectedPriceRange":{},"MinPrice":"1800","MaxPrice":"13750"},"specificationFiltersModel7Spikes":{"CategoryId":"4","ManufacturerId":"0","VendorId":"0","SpecificationFilterGroups":[{"Id":27,"FilterItems":[{"Id":"103","FilterItemState":"Unchecked"},{"Id":"104","FilterItemState":"Unchecked"},{"Id":"110","FilterItemState":"Unchecked"},{"Id":"3854","FilterItemState":"Unchecked"},{"Id":"2626","FilterItemState":"Unchecked"}]},{"Id":20,"FilterItems":[{"Id":"90","FilterItemState":"Unchecked"},{"Id":"92","FilterItemState":"Unchecked"},{"Id":"93","FilterItemState":"Unchecked"},{"Id":"99","FilterItemState":"Unchecked"}]},{"Id":11,"FilterItems":[{"Id":"302","FilterItemState":"Unchecked"},{"Id":"2494","FilterItemState":"Unchecked"}]},{"Id":6,"FilterItems":[{"Id":"2461","FilterItemState":"Unchecked"},{"Id":"21","FilterItemState":"Unchecked"},{"Id":"24","FilterItemState":"Unchecked"},{"Id":"25","FilterItemState":"Unchecked"},{"Id":"26","FilterItemState":"Unchecked"}]},{"Id":7,"FilterItems":[{"Id":"5346","FilterItemState":"Unchecked"}]},{"Id":5,"FilterItems":[{"Id":"2742","FilterItemState":"Unchecked"},{"Id":"2743","FilterItemState":"Unchecked"},{"Id":"3493","FilterItemState":"Unchecked"}]},{"Id":2,"FilterItems":[{"Id":"8","FilterItemState":"Unchecked"},{"Id":"1451","FilterItemState":"Unchecked"},{"Id":"1123","FilterItemState":"Unchecked"}]},{"Id":8,"FilterItems":[{"Id":"61","FilterItemState":"Unchecked"},{"Id":"3458","FilterItemState":"Unchecked"},{"Id":"3719","FilterItemState":"Unchecked"}]},{"Id":334,"FilterItems":[{"Id":"2489","FilterItemState":"Unchecked"},{"Id":"2488","FilterItemState":"Unchecked"},{"Id":"2487","FilterItemState":"Unchecked"}]},{"Id":628,"FilterItems":[{"Id":"5413","FilterItemState":"Unchecked"},{"Id":"5079","FilterItemState":"Unchecked"},{"Id":"5080","FilterItemState":"Unchecked"}]},{"Id":680,"FilterItems":[{"Id":"4935","FilterItemState":"Unchecked"}]}]},"manufacturerFiltersModel7Spikes":{"CategoryId":"4","ManufacturerFilterItems":[{"Id":"2","FilterItemState":"Unchecked"},{"Id":"1","FilterItemState":"Unchecked"},{"Id":"6","FilterItemState":"Unchecked"},{"Id":"44","FilterItemState":"Unchecked"},{"Id":"108","FilterItemState":"Unchecked"}]},"pageNumber":' + str(page_num) + ',"orderby":"10","viewmode":"grid","pagesize":0,"queryString":"","shouldNotStartFromFirstPage":' + start_first_page + ',"keyword":"","searchCategoryId":"0","searchManufacturerId":"0","searchVendorId":"0","priceFrom":"","priceTo":"","includeSubcategories":"False","searchInProductDescriptions":"False","advancedSearch":"False","isOnSearchPage":"False"}'

    def start_requests(self):
        yield scrapy.Request(url='https://eastasiaeg.com/21/getFilteredProducts',
                             method='POST', body=self.payload)

    def parse(self, response):

        products = response.xpath('//div[@class = "product-item"]')
        for product in products:
            name = product.xpath('.//h2/a/text()').get()
            yield{
                'name': name
                }

        if len(products) > 0:
            self.page_num += 1
            self.start_first_page = 'true'
            self.payload = '{"categoryId":"4","manufacturerId":"0","vendorId":"0","priceRangeFilterModel7Spikes":{"CategoryId":"4","ManufacturerId":"0","VendorId":"0","SelectedPriceRange":{},"MinPrice":"1800","MaxPrice":"13750"},"specificationFiltersModel7Spikes":{"CategoryId":"4","ManufacturerId":"0","VendorId":"0","SpecificationFilterGroups":[{"Id":27,"FilterItems":[{"Id":"103","FilterItemState":"Unchecked"},{"Id":"104","FilterItemState":"Unchecked"},{"Id":"110","FilterItemState":"Unchecked"},{"Id":"3854","FilterItemState":"Unchecked"},{"Id":"2626","FilterItemState":"Unchecked"}]},{"Id":20,"FilterItems":[{"Id":"90","FilterItemState":"Unchecked"},{"Id":"92","FilterItemState":"Unchecked"},{"Id":"93","FilterItemState":"Unchecked"},{"Id":"99","FilterItemState":"Unchecked"}]},{"Id":11,"FilterItems":[{"Id":"302","FilterItemState":"Unchecked"},{"Id":"2494","FilterItemState":"Unchecked"}]},{"Id":6,"FilterItems":[{"Id":"2461","FilterItemState":"Unchecked"},{"Id":"21","FilterItemState":"Unchecked"},{"Id":"24","FilterItemState":"Unchecked"},{"Id":"25","FilterItemState":"Unchecked"},{"Id":"26","FilterItemState":"Unchecked"}]},{"Id":7,"FilterItems":[{"Id":"5346","FilterItemState":"Unchecked"}]},{"Id":5,"FilterItems":[{"Id":"2742","FilterItemState":"Unchecked"},{"Id":"2743","FilterItemState":"Unchecked"},{"Id":"3493","FilterItemState":"Unchecked"}]},{"Id":2,"FilterItems":[{"Id":"8","FilterItemState":"Unchecked"},{"Id":"1451","FilterItemState":"Unchecked"},{"Id":"1123","FilterItemState":"Unchecked"}]},{"Id":8,"FilterItems":[{"Id":"61","FilterItemState":"Unchecked"},{"Id":"3458","FilterItemState":"Unchecked"},{"Id":"3719","FilterItemState":"Unchecked"}]},{"Id":334,"FilterItems":[{"Id":"2489","FilterItemState":"Unchecked"},{"Id":"2488","FilterItemState":"Unchecked"},{"Id":"2487","FilterItemState":"Unchecked"}]},{"Id":628,"FilterItems":[{"Id":"5413","FilterItemState":"Unchecked"},{"Id":"5079","FilterItemState":"Unchecked"},{"Id":"5080","FilterItemState":"Unchecked"}]},{"Id":680,"FilterItems":[{"Id":"4935","FilterItemState":"Unchecked"}]}]},"manufacturerFiltersModel7Spikes":{"CategoryId":"4","ManufacturerFilterItems":[{"Id":"2","FilterItemState":"Unchecked"},{"Id":"1","FilterItemState":"Unchecked"},{"Id":"6","FilterItemState":"Unchecked"},{"Id":"44","FilterItemState":"Unchecked"},{"Id":"108","FilterItemState":"Unchecked"}]},"pageNumber":' + str(self.page_num) + ',"orderby":"10","viewmode":"grid","pagesize":0,"queryString":"","shouldNotStartFromFirstPage":' + self.start_first_page + ',"keyword":"","searchCategoryId":"0","searchManufacturerId":"0","searchVendorId":"0","priceFrom":"","priceTo":"","includeSubcategories":"False","searchInProductDescriptions":"False","advancedSearch":"False","isOnSearchPage":"False"}'
            yield scrapy.Request(url='https://eastasiaeg.com/21/getFilteredProducts',
                             method='POST', body=self.payload, callback=self.parse)
