import os,random
from datetime import datetime
import requests, json

class Update_feeds:
    def __init__(self,feed):
        self.feed=feed
        now = datetime.now()
        self.timestamp = datetime.timestamp(now)

    @staticmethod
    def getFeeds(url):
        feed_data = []

        try:
            r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0'}, timeout=15)
            feedResult = feedparser.parse(r.text)
            for item in feedResult.entries:
                feed_data.append({
                    "content_type": "audio/mp3",
                    "title": item.itunes_title.encode('utf-8', 'surrogateescape').decode('ISO-8859-1'),
                    "url": item.links[1].href,
                    "thumb": feedResult.feed.image.href
                })
            return feed_data
        except:
            print("failed: " + url)

    @staticmethod
    def writeFeeds(feed_data):
        with open('podcasts.json', 'w') as outfile:
            json.dump(feed_data, outfile, indent=4)
