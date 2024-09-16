from abc import ABC, abstractmethod
import requests
import xml.etree.ElementTree as ET
from urllib.parse import urlparse

class RSSBase(ABC):
    
    _name = "BaseName"

    def __init__(self, rss_link) -> None:
        self._rss_link = rss_link
        temp = urlparse(self._rss_link)
        self._name = temp.hostname

    @property
    def rss_link(self) -> str:
        return self._rss_link

    @rss_link.setter
    def rss_link(self, rss_link) -> None:
        self._rss_link = rss_link

    def get_rss_data(self):
        headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
                    }
        response = requests.get(self._rss_link, headers=headers, timeout=30)
        # print(response.text)
        return response.content.decode('utf-8')
    @abstractmethod
    def parse_data(self):
        pass
    
    @abstractmethod
    def is_one_hour(self, date_str, deta_time=1):
        pass
