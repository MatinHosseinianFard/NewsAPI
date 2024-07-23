import scrapy
from scrapy_splash import SplashRequest

import re


class ZoomitSpider(scrapy.Spider):
    name = "zoomit"
    results = []

    def start_requests(self):
        yield SplashRequest('https://www.zoomit.ir/feed/', self.parse, args={'wait': 0.5})

    def parse(self, response):
        for new in response.css('item'):
            title = new.css('title::text').get()
            description = new.css('description::text').get()
            link = re.search(r'href="([^"]+)"', description)
            if link:
                link = link.group(1)
            tags = new.css('category::text').getall()

            yield SplashRequest(link, self.parse_details, args={'wait': 0.5}, meta={
                'title': title,
                'link': link,
                'description': description,
                'tags': tags
            })

    def parse_details(self, response):

        title = response.meta['title']
        tags = response.meta['tags']

        content = response.css('.hXzioD *')
        body_parts = []

        for tag in content:
            if tag.root.tag == 'p':
                body_parts.append(''.join(tag.css('::text').extract()))
            elif tag.root.tag == 'ul':
                list_items = tag.css('li::text').extract()
                body_parts.extend(list_items)

        body = '\n'.join(body_parts)
        source = 'zoomit'

        ZoomitSpider.results.append({
            'title': title,
            'body': body,
            'tags': tags,
            'source': source,
        })
