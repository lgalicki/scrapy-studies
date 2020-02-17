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

        self.req_headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,gl;q=0.8,pt;q=0.7',
            'cookie': 'check=true; AMCVS_3ADD33055666F1A47F000101%40AdobeOrg=1; AMCV_3ADD33055666F1A47F000101%40AdobeOrg=1075005958%7CMCIDTS%7C18309%7CMCMID%7C40423812149329860441064399821999867366%7CMCAAMLH-1582461986%7C4%7CMCAAMB-1582461986%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1581864386s%7CNONE%7CvVersion%7C4.4.1; WebMotorsVisitor=1; __gads=ID=e558721fab2fb31d:T=1581857187:S=ALNI_MbXJ-xMWGT-dWxjbJbmJerGEGwodw; s_cc=true; blueID=dade9f9b-b80c-49a5-858b-f39d12fad9e8; _fbp=fb.2.1581857187408.2063044714; mboxEdgeCluster=17; _gcl_aw=GCL.1581857187.EAIaIQobChMI1PiXm43W5wIVxR6tBh1EHgiIEAAYASAAEgJlTPD_BwE; _st_ses=22056107186307017; _st_cart_script=helper_webmotors.js; _st_cart_url=/; _sptid=70; _spcid=80; _pxvid=59095cbd-50ba-11ea-9c26-0242ac12000a; _st_no_user=1; _hjid=c90320a0-32c9-41b6-9c45-366bad71e351; _hjIncludedInSample=1; _tggcid=06010043-e474-40a2-ac00-1f225e4939a4; _tgclid=EAIaIQobChMI1PiXm43W5wIVxR6tBh1EHgiIEAAYASAAEgJlTPD_BwE; _tgrsid=EAIaIQobChMI1PiXm43W5wIVxR6tBh1EHgiIEAAYASAAEgJlTPD_BwE; sback_browser=0-87622100-158185718791bbf3131904ec61117470cf7bd40344b7e820a819792960215e4939a3d5ecc4-08788464-13820426137,1301764087-1581857187; _cm_ads_activation_retry=false; _tgsource=www.google.com; sback_client=56d484398a20ed6d221e935d; sback_customer=$2wdxEXV4ckWOVTNz0UWUZzTZhGcSFDRR1kZ0gWWrJzTZlmeD1EWygnTqtGbKpFVy5ENyoXSxJzaNpUbXZEayclT2$12; sback_access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuc2JhY2sudGVjaCIsImlhdCI6MTU4MTg1NzE4OCwiZXhwIjoxNTgxOTQzNTg4LCJhcGkiOiJ2MiIsImRhdGEiOnsiY2xpZW50X2lkIjoiNTZkNDg0Mzk4YTIwZWQ2ZDIyMWU5MzVkIiwiY2xpZW50X2RvbWFpbiI6IndlYm1vdG9ycy5jb20uYnIiLCJjdXN0b21lcl9pZCI6IjVlNDkzOWE0MDhmYzNjN2QyNTZiM2ZhNyIsImN1c3RvbWVyX2Fub255bW91cyI6dHJ1ZSwiY29ubmVjdGlvbl9pZCI6IjVlNDkzOWE0MDhmYzNjN2QyNTZiM2ZhOCIsImFjY2Vzc19sZXZlbCI6ImN1c3RvbWVyIn19.AoYqW3_d8GbgF6C5VFEH3rMcdSoZ42JoNWJVprzxx9I.WrWrDriYWriYDrEiWriYiY; sback_partner=false; sback_current_session=1; sback_total_sessions=1; sb_days=1581857189017; sback_customer_w=true; sback_refresh_wp=no; WebMotorsCardPreferences=%221%22; gpv_v39=%2Fwebmotors%2Fcomprar%2Fresultado; s_sq=%5B%5BB%5D%5D; WMLastFilterSearch=%7B%22car%22%3A%22carros%2Festoque%2Fvolkswagen%3Fmarca1%3DVOLKSWAGEN%22%2C%22bike%22%3A%22motos%2Festoque%22%2C%22estadocidade%22%3A%22estoque%22%2C%22lastType%22%3A%22car%22%2C%22cookie%22%3A%22v3%22%2C%22ano%22%3A%7B%7D%2C%22preco%22%3A%7B%7D%2C%22marca%22%3A%22VOLKSWAGEN%22%2C%22modelo%22%3A%22%22%7D; _spl_pv=4; _px3=8c6217bdedd269a474a33a278a49fcaa86a248da0cbcd42adfcdfbb8f53c68ad:3V3epJ7RdQtjcwIpsQgA1T2SUwdTRbwq+j9aJWJ2WA60THBvh9LYD34ag/yHGpNRdw3SdamZYNF4BnDSVRd5cw==:1000:/llHpEnVN5Cj9FDCcWRJ8QveFO+B+fpa7LM9vkR+TJqSkho4BBGte2UkYCTfXJXbCIyGUGofCfcyGLI70D9CpbjEy7lbyz39FDYfO/fMx7ODFPPwmlhwu0JpzR5EQLuDwrmtJwSk5VMeOgy58Y9Vch4amSfi26Qltkaa36oj2FM=; smeventssent_558d6270794b42c3be036d07cf2129c7=true; WebMotorsSearchDataLayer=%7B%22search%22%3A%7B%22nmEstado%22%3A%22estoque%22%2C%22nmCidade%22%3A%22nao%22%2C%22sortimento%22%3A%22a30479105g%2Cb31346454g%2Cc31668701g%2Cd30877342g%2Ce31633383g%2Cf31496623m%2Cg30939761g%2Ch31405620g%2Ci31402423g%2Cj31507735g%2Ck31707304m%2Cl31652502m%2Cm31692622m%2Cn29659334g%2Co31287515g%2Cp31717428g%2Cq31279437m%2Cr31519310g%2Cs31615873g%2Ct31278858m%2Cu31527805m%2Cv30186183m%2Cw30432738g%2Cx31643676m%22%2C%22ordenacao%22%3A1%2C%22paginacao%22%3A3%2C%22termoAutocomplete%22%3A%22nao%22%2C%22raio%22%3A%22nao%22%7D%7D; mbox=session#bc8aadc6d0a64a5d840960b6b4bc7970#1581859047|PC#bc8aadc6d0a64a5d840960b6b4bc7970.17_0#1645102225',
            'referer': f'https://www.webmotors.com.br/carros/estoque/{self.marca}',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/80.0.3987.100 Chrome/80.0.3987.100 Safari/537.36'
            }

        self.cookies = {
            'check': 'true',
            'AMCVS_3ADD33055666F1A47F000101%40AdobeOrg': '1',
            'AMCV_3ADD33055666F1A47F000101%40AdobeOrg': '1075005958%7CMCIDTS%7C18309%7CMCMID%7C40423812149329860441064399821999867366%7CMCAAMLH-1582461986%7C4%7CMCAAMB-1582461986%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1581864386s%7CNONE%7CvVersion%7C4.4.1',
            'WebMotorsVisitor': '1',
            '__gads': 'ID=e558721fab2fb31d:T=1581857187:S=ALNI_MbXJ-xMWGT-dWxjbJbmJerGEGwodw; s_cc=true',
            'blueID': 'dade9f9b-b80c-49a5-858b-f39d12fad9e8',
            '_fbp': 'fb.2.1581857187408.2063044714',
            'mboxEdgeCluster': '17',
            '_gcl_aw': 'GCL.1581857187.EAIaIQobChMI1PiXm43W5wIVxR6tBh1EHgiIEAAYASAAEgJlTPD_BwE',
            '_st_ses': '22056107186307017',
            '_st_cart_script': 'helper_webmotors.js',
            '_st_cart_url': '/',
            '_sptid': '70',
            '_spcid': '80',
            '_pxvid': '59095cbd-50ba-11ea-9c26-0242ac12000a',
            '_st_no_user': '1',
            '_hjid': 'c90320a0-32c9-41b6-9c45-366bad71e351',
            '_hjIncludedInSample': '1',
            '_tggcid': '06010043-e474-40a2-ac00-1f225e4939a4',
            '_tgclid': 'EAIaIQobChMI1PiXm43W5wIVxR6tBh1EHgiIEAAYASAAEgJlTPD_BwE',
            '_tgrsid': 'EAIaIQobChMI1PiXm43W5wIVxR6tBh1EHgiIEAAYASAAEgJlTPD_BwE',
            'sback_browser': '0-87622100-158185718791bbf3131904ec61117470cf7bd40344b7e820a819792960215e4939a3d5ecc4-08788464-13820426137,1301764087-1581857187',
            '_cm_ads_activation_retry': 'false',
            '_tgsource': 'www.google.com',
            'sback_client': '56d484398a20ed6d221e935d',
            'sback_customer': '$2wdxEXV4ckWOVTNz0UWUZzTZhGcSFDRR1kZ0gWWrJzTZlmeD1EWygnTqtGbKpFVy5ENyoXSxJzaNpUbXZEayclT2$12',
            'sback_access_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuc2JhY2sudGVjaCIsImlhdCI6MTU4MTg1NzE4OCwiZXhwIjoxNTgxOTQzNTg4LCJhcGkiOiJ2MiIsImRhdGEiOnsiY2xpZW50X2lkIjoiNTZkNDg0Mzk4YTIwZWQ2ZDIyMWU5MzVkIiwiY2xpZW50X2RvbWFpbiI6IndlYm1vdG9ycy5jb20uYnIiLCJjdXN0b21lcl9pZCI6IjVlNDkzOWE0MDhmYzNjN2QyNTZiM2ZhNyIsImN1c3RvbWVyX2Fub255bW91cyI6dHJ1ZSwiY29ubmVjdGlvbl9pZCI6IjVlNDkzOWE0MDhmYzNjN2QyNTZiM2ZhOCIsImFjY2Vzc19sZXZlbCI6ImN1c3RvbWVyIn19.AoYqW3_d8GbgF6C5VFEH3rMcdSoZ42JoNWJVprzxx9I.WrWrDriYWriYDrEiWriYiY',
            'sback_partner': 'false',
            'sback_current_session': '1',
            'sback_total_sessions': '1',
            'sb_days': '1581857189017',
            'sback_customer_w': 'true',
            'sback_refresh_wp': 'no',
            'WebMotorsCardPreferences': '%221%22',
            'gpv_v39': '%2Fwebmotors%2Fcomprar%2Fresultado',
            's_sq': '%5B%5BB%5D%5D',
            'WMLastFilterSearch': '%7B%22car%22%3A%22carros%2Festoque%2Fvolkswagen%3Fmarca1%3DVOLKSWAGEN%22%2C%22bike%22%3A%22motos%2Festoque%22%2C%22estadocidade%22%3A%22estoque%22%2C%22lastType%22%3A%22car%22%2C%22cookie%22%3A%22v3%22%2C%22ano%22%3A%7B%7D%2C%22preco%22%3A%7B%7D%2C%22marca%22%3A%22VOLKSWAGEN%22%2C%22modelo%22%3A%22%22%7D',
            '_spl_pv': '4',
            '_px3': '8c6217bdedd269a474a33a278a49fcaa86a248da0cbcd42adfcdfbb8f53c68ad:3V3epJ7RdQtjcwIpsQgA1T2SUwdTRbwq+j9aJWJ2WA60THBvh9LYD34ag/yHGpNRdw3SdamZYNF4BnDSVRd5cw==:1000:/llHpEnVN5Cj9FDCcWRJ8QveFO+B+fpa7LM9vkR+TJqSkho4BBGte2UkYCTfXJXbCIyGUGofCfcyGLI70D9CpbjEy7lbyz39FDYfO/fMx7ODFPPwmlhwu0JpzR5EQLuDwrmtJwSk5VMeOgy58Y9Vch4amSfi26Qltkaa36oj2FM=',
            'smeventssent_558d6270794b42c3be036d07cf2129c7': 'true',
            'WebMotorsSearchDataLayer': '%7B%22search%22%3A%7B%22nmEstado%22%3A%22estoque%22%2C%22nmCidade%22%3A%22nao%22%2C%22sortimento%22%3A%22a30479105g%2Cb31346454g%2Cc31668701g%2Cd30877342g%2Ce31633383g%2Cf31496623m%2Cg30939761g%2Ch31405620g%2Ci31402423g%2Cj31507735g%2Ck31707304m%2Cl31652502m%2Cm31692622m%2Cn29659334g%2Co31287515g%2Cp31717428g%2Cq31279437m%2Cr31519310g%2Cs31615873g%2Ct31278858m%2Cu31527805m%2Cv30186183m%2Cw30432738g%2Cx31643676m%22%2C%22ordenacao%22%3A1%2C%22paginacao%22%3A3%2C%22termoAutocomplete%22%3A%22nao%22%2C%22raio%22%3A%22nao%22%7D%7D',
            'mbox': 'session#bc8aadc6d0a64a5d840960b6b4bc7970#1581859047|PC#bc8aadc6d0a64a5d840960b6b4bc7970.17_0#1645102225'
            }

        yield scrapy.Request(url=f'https://www.webmotors.com.br/api/search/car?url=https://www.webmotors.com.br/carros%2Festoque%2F{self.brand}&actualPage={self.page}&displayPerPage=24&order=1&showMenu=true&showCount=true&showBreadCrumb=true&testAB=false&returnUrl=false',
                             callback=self.parse, headers=self.req_headers, cookies=self.cookies)

    def parse(self, response):
        data = json.loads(response.body)
        cars = data.get('SearchResults')

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
            yield scrapy.Request(url=f'https://www.webmotors.com.br/api/search/car?url=https://www.webmotors.com.br/carros%2Festoque%2F{self.brand}&actualPage={self.page}&displayPerPage=24&order=1&showMenu=true&showCount=true&showBreadCrumb=true&testAB=false&returnUrl=false',
                                 callback=self.parse, headers=self.req_headers, cookies=self.cookies)
