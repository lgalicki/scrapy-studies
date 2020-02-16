# -*- coding: utf-8 -*-
import json
import logging
import scrapy


class WebmotorsSpider(scrapy.Spider):
    name = 'webmotors'
    allowed_domains = ['www.webmotors.com.br']
    page = 1

    def start_requests(self):
        self.brand = self.marca
        yield scrapy.Request(url=f'https://www.webmotors.com.br/api/search/car?url=https://www.webmotors.com.br/carros%2Festoque%2F{self.brand}&actualPage={self.page}&displayPerPage=24&order=1&showMenu=true&showCount=true&showBreadCrumb=true&testAB=false&returnUrl=false', callback=self.parse)
        
    def parse(self, response):
        data = json.loads(response.body)
        cars = data.get('SearchResults')
        total_qt_cars = data.get('Count')

        for car in cars:
            try:
                unique_id = car.get('UniqueId')
                title = car.get('Specification').get('Title').title()
                brand = car.get('Specification').get('Make').get('Value').title()
                model = car.get('Specification').get('Model').get('Value').title()
                version = car.get('Specification').get('Version').get('Value').title()
                year_fabrication = int(car.get('Specification').get('YearFabrication'))
                year_model = int(car.get('Specification').get('YearModel'))
                odometer = int(car.get('Specification').get('Odometer'))
                transmission = car.get('Specification').get('Transmission')
                doors = int(car.get('Specification').get('NumberPorts'))
                armored = car.get('Specification').get('Armored')
                color = car.get('Specification').get('Color').get('Primary')
                city = car.get('Seller').get('City')
                state = car.get('Seller').get('State').split()[-1].rstrip(')').lstrip('(')
                price = float(car.get('Prices').get('Price'))
                comment = car.get('LongComment')
                fipe_percent = car.get('FipePercent')
                
                if year_fabrication == year_model:
                    year_url = year_fabrication
                else:
                    year_url = f'{year_fabrication}-{year_model}'
                
                url = f'https://www.webmotors.com.br/comprar/{brand.lower()}/{model.lower()}/{version.lower()}/{doors}-portas/{year_url}/{unique_id}?pos=a{unique_id}m:&np=1'
                url = url.replace(' ', '-')

                yield{
                    'title': title,
                    'brand': brand,
                    'model': model,
                    'version': version,
                    'year_fabrication': year_fabrication,
                    'year_model': year_model,
                    'odometer': odometer,
                    'transmission': transmission,
                    'doors': doors,
                    'armored': armored,
                    'color': color,
                    'city': city,
                    'state': state,
                    'price': price,
                    'comment': comment,
                    'fipe_percent': fipe_percent,
                    'url': url
                }

            except ValueError:
                logging.error(f'Problem with data format: {unique_id}')

        if len(cars) != 0:
            self.page += 1
            yield scrapy.Request(url=f'https://www.webmotors.com.br/api/search/car?url=https://www.webmotors.com.br/carros%2Festoque%2F{self.brand}&actualPage={self.page}&displayPerPage=24&order=1&showMenu=true&showCount=true&showBreadCrumb=true&testAB=false&returnUrl=false', callback=self.parse)
