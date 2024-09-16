from rss.rss_base import RSSBase
import xml.etree.ElementTree as ET
from bot import TelegramBot
import time
from datetime import datetime, timedelta
import pytz

class RssSocRadar(RSSBase):
    _name = "socradar.io"
    def __init__(self, rss_link) -> None:
        super().__init__(rss_link)

    def is_one_hour(self, date_str, delta_time=1):
        now = datetime.now(pytz.timezone('Asia/Ho_Chi_Minh'))
        date_format = "%a, %d %b %Y %H:%M:%S %z"
        dt = datetime.strptime(date_str, date_format)
        now_in_pubdate_tz = now.astimezone(dt.tzinfo)
        one_hour_before = now_in_pubdate_tz - timedelta(hours=delta_time)
        return  one_hour_before <= dt
    
    async def parse_data(self):
        data = self.get_rss_data()
        # print(data)
        bot = TelegramBot()
        try:
            tree = ET.ElementTree(ET.fromstring(data))
            root = tree.getroot()
            items = root.findall("./channel/item")
            for item in items:
                title = item.find('title').text
                link = item.find('link').text
                pubDate = item.find('pubDate').text
                #description = item.find('description').text[:256] if item.find('description') is not None else "N/A"
                category = item.find('category').text if item.find('category') is not None else "N/A"
                
                msg = f"[{self._name}][{category}]\n{title}\n{pubDate}\n{link}\n"
                print(msg)
                if self.is_one_hour(pubDate):
                    await bot.send_message(msg)
                    time.sleep(4)
        except Exception as e:
            print(e)
            

