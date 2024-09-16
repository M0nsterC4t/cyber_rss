from rss.rss_socradar_io import *
from rss.rss_cyware_com import *
from loader.plugin_loader import PluginLoader
import asyncio
import schedule
import time
import os
def get_all():
    datas = open('cyber_rss/data.csv', 'r').readlines()
    sources = []
    for data in datas:
        tmp = data.split(',')
        if len(tmp) < 2:
            continue
        sources.append({"url": tmp[0].strip(), "parser": tmp[1].strip()})
    return sources

async def get_rss():
    plugin_loader = PluginLoader(os.path.join(os.path.dirname(__file__), 'rss'))
    plugin_loader.load_plugins()
    sources = get_all()
    for source in sources:
        url = source["url"]
        parser = source["parser"]
        parser_class = plugin_loader.get_plugin(parser)
        print(f"{url} {parser} {parser_class}")
        if parser_class:
            temp = parser_class(url)
            await temp.parse_data()



def main():
    def run_async_hourly():
        asyncio.run(get_rss())
    
    run_async_hourly()

if __name__ == '__main__':
    main()