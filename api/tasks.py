from scraper.scraper.spiders.zoomit import ZoomitSpider
from scrapy.crawler import CrawlerProcess
from multiprocessing import Process
from api.models import New, Tag
from core.celery import app


@app.task
def crawl_task():
    # Use multiprocessing to run the spider in a separate process.
    p = Process(target=run_spider)
    p.start()
    p.join()

    return "done"


def run_spider():
    # Create a CrawlerProcess instance to run the spider.
    process = CrawlerProcess()
    process.crawl(ZoomitSpider)
    process.start()
    process.join()

    # Get the results collected by the spider.
    results = ZoomitSpider.results
    for result in results:
        # Create or retrieve a New instance based on the title.
        new_object, created = New.objects.get_or_create(
            title=result['title'],
            defaults={'body': result['body'], 'source': result['source']}
        )

        for tag_name in result['tags']:
            # Create or retrieve a Tag instance based on the tag name.
            tag, created = Tag.objects.get_or_create(name=tag_name)
            # Add the tag to the New instance's tags.
            new_object.tags.add(tag)

        new_object.save()

    print("=" * 30)
    print("success")
    print("=" * 30)
