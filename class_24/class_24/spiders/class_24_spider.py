# -*- coding: utf-8 -*-
import scrapy
from class_24.items import Class24Item
import json


class Class24SpiderSpider(scrapy.Spider):
    name = 'class_24_spider'
    allowed_domains = ['https://www.rentingcarfacil.com/trh/']
    start_urls = ['https://www.rentingcarfacil.com/trh//']

    def parse(self, response):
        items = Class24Item()

        titulos_con_retorno = response.xpath('//h1/a/text()').extract()
        items['titulos'] = [
            model for model in titulos_con_retorno if model != '\n']
        items['precios'] = response.xpath(
            '//h1/a/span/strong/text()').extract()

        result = [{'titulo': titulo, 'precio': items.get(
            'precios')[index]} for index, titulo in enumerate(items.get('titulos'))]

        self._compare_data(result)
        print('ASERREJE', result)

        # yield {"result":result}

    def _create_json(self, data):
        with open('data.json', 'w') as fp:
            json.dump(data, fp)

    def _compare_data(self, result):
        with open('data.json', 'r') as old_data:
            yesterdaty_data = json.load(old_data)
            if yesterdaty_data == result:
                print('SON IGUALES')
            else:
                print('NO LO SON')
                self._create_json(result)
