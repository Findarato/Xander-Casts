import os,random
from datetime import datetime
import requests, json
import feedparser

class Update_feeds:
    def __init__(self,feed):
        self.feed=feed
        now = datetime.now()
        self.timestamp = datetime.timestamp(now)

    @staticmethod
    def getFeeds(url):
        feed_data = []

        try:
            r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0'}, timeout=60)
            feed_result = feedparser.parse(r.text)
            for item in feed_result.entries:
                url = ""
                for link in item.links:
                    if link.rel == "enclosure":
                        url_to_play = link.href

                feed_data.append({
                    "content_type": "audio/mp3",
                    "title": item.title.encode('utf-8', 'surrogateescape').decode('ISO-8859-1'),
                    "url": url_to_play,
                    "thumb": feed_result.feed.image.href
                })
            return feed_data
        except:
            print("failed: " + url)

    @staticmethod
    def writeFeeds(feed_data):
        with open('podcasts.json', 'w') as outfile:
            json.dump(feed_data, outfile, indent=4)
