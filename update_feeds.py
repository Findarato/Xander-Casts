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
            feedResult = feedparser.parse(r.text)
            # print(feedResult)
            # print(json.dumps(feedResult, indent=4, separators=(". ", " = ")))
            for item in feedResult.entries:
                url = ""
                for link in item.links:
                    if link.rel == "enclosure":
                        url = link.href

                feed_data.append({
                    "content_type": "audio/mp3",
                    "title": item.title.encode('utf-8', 'surrogateescape').decode('ISO-8859-1'),
                    "url": url,
                    "thumb": feedResult.feed.image.href
                })
            return feed_data
        except:
            print("failed: " + url)

    @staticmethod
    def writeFeeds(feed_data):
        with open('podcasts.json', 'w') as outfile:
            json.dump(feed_data, outfile, indent=4)
