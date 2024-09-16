from rss.rss_socradar_io import *
from rss.rss_cyware_com import *
from loader.plugin_loader import PluginLoader
import asyncio
import schedule
import time
import os
from models import get_or_create, Sources, get_all

async def get_rss():
    # rss_socradar = RssSocRadar("https://socradar.io/feed/")
    # await rss_socradar.parse_data()
    # blog_checkpoint = RssSocRadar("https://blog.checkpoint.com/feed/")
    # await blog_checkpoint.parse_data()
    # cyberware = RssCyware("https://cyware.com/allnews/feed")
    # await cyberware.parse_data()
    # rusianpanda = RssSocRadar("https://russianpanda.com/feed")
    # await rusianpanda.parse_data()
    # zscaler = RssSocRadar("https://www.zscaler.com/blogs/feeds")
    # await zscaler.parse_data()
    # zscaler = RssSocRadar("https://viettelcybersecurity.com/feed/")
    # await zscaler.parse_data()
    # cyble = RssSocRadar("https://cyble.com/feed/")
    # await cyble.parse_data()
    # cybersecuritynews = RssSocRadar("https://cybersecuritynews.com/feed/")
    # await cybersecuritynews.parse_data()
    # thn = RssSocRadar("https://feeds.feedburner.com/TheHackersNews")
    # await thn.parse_data()
    # exploitreversing = RssSocRadar("https://exploitreversing.com/feed/")
    # await exploitreversing.parse_data()
    # opendatasecurity = RssSocRadar("https://opendatasecurity.co.uk/feed/")
    # await opendatasecurity.parse_data()
    # securityaffairs = RssSocRadar("https://securityaffairs.com/feed")
    # await securityaffairs.parse_data()
    # iototsecnews = RssSocRadar("https://iototsecnews.jp/feed/")
    # await iototsecnews.parse_data()
    # # ctfiot = RssSocRadar("https://www.ctfiot.com/feed")
    # # await ctfiot.parse_data()
    # industrialcyber = RssSocRadar("https://industrialcyber.co/feed/")
    # await industrialcyber.parse_data()
    # rcp = RssSocRadar("https://research.checkpoint.com/feed/")
    # await rcp.parse_data()
    # sentinelone = RssSocRadar("https://www.sentinelone.com/feed/")
    # await sentinelone.parse_data()
    # # detect = RssSocRadar("https://detect.fyi/feed")
    # # await detect.parse_data()
    # sophos = RssSocRadar("https://news.sophos.com/en-us/feed/")
    # await sophos.parse_data()
    plugin_loader = PluginLoader(os.path.join(os.path.dirname(__file__), 'rss'))
    plugin_loader.load_plugins()
    sources = get_all(Sources)
    for source in sources:
        url = source.url
        parser = source.parser
        parser_class = plugin_loader.get_plugin(parser)
        print(f"{url} {parser} {parser_class}")
        if parser_class:
            temp = parser_class(url)
            await temp.parse_data()



def main():
    def run_async_hourly():
        asyncio.run(get_rss())

    schedule.every(1).hours.do(run_async_hourly)
    while True:
        schedule.run_pending()
        time.sleep(1)

async def main_test():
    rss_socradar = RssSocRadar("https://socradar.io/feed/")
    await rss_socradar.parse_data()
    blog_checkpoint = RssSocRadar("https://blog.checkpoint.com/feed/")
    await blog_checkpoint.parse_data()
    cyberware = RssCyware("https://cyware.com/allnews/feed")
    await cyberware.parse_data()
    rusianpanda = RssSocRadar("https://russianpanda.com/feed")
    await rusianpanda.parse_data()
    zscaler = RssSocRadar("https://www.zscaler.com/blogs/feeds")
    await zscaler.parse_data()
    zscaler = RssSocRadar("https://viettelcybersecurity.com/feed/")
    await zscaler.parse_data()
    cyble = RssSocRadar("https://cyble.com/feed/")
    await cyble.parse_data()
    cybersecuritynews = RssSocRadar("https://cybersecuritynews.com/feed/")
    await cybersecuritynews.parse_data()
    thn = RssSocRadar("https://feeds.feedburner.com/TheHackersNews")
    await thn.parse_data()
    exploitreversing = RssSocRadar("https://exploitreversing.com/feed/")
    await exploitreversing.parse_data()
    opendatasecurity = RssSocRadar("https://opendatasecurity.co.uk/feed/")
    await opendatasecurity.parse_data()
    securityaffairs = RssSocRadar("https://securityaffairs.com/feed")
    await securityaffairs.parse_data()
    iototsecnews = RssSocRadar("https://iototsecnews.jp/feed/")
    await iototsecnews.parse_data()
    ctfiot = RssSocRadar("https://www.ctfiot.com/feed")
    await ctfiot.parse_data()
    industrialcyber = RssSocRadar("https://industrialcyber.co/feed/")
    await industrialcyber.parse_data()

#asyncio.run(main_test())
if __name__ == '__main__':
    main()