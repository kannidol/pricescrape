from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem


class HpPatronen(BasePortiaSpider):
    name = "HP_patronen"
    allowed_domains = [u'www.hq-patronen.de']
    start_urls = [u'https://www.hq-patronen.de/']
    rules = [
        Rule(
            LinkExtractor(
                allow=('.*'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [[Item(PortiaItem,
                   None,
                   u'#cphMain_spanPrice',
                   [Field(u'price',
                          'span *::text',
                          [Price()]),
                       Field(u'article',
                             'meta[itemprop="productID"]::attr(content)',
                             [Text()])])]]
