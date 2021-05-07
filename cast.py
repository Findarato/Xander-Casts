import json
import os
import random
import time
import opml
import pychromecast
import logging

from datetime import datetime

from player import Player

from update_feeds import Update_feeds


logging.basicConfig(filename='xandercast.log', encoding='utf-8')

def getUpdate():
    json_data = []

    outline = opml.parse("podcasts.xml")

    logging.info("Getting Feeds")
    # try:
    if outline[0].text == "feeds":  # This is a pocket casts feed
        for podcast_feed in outline[0]:
            json_data.extend(Update_feeds.getFeeds(podcast_feed.xmlUrl))
    else:
        for podcast_feed in outline:
            json_data.extend(Update_feeds.getFeeds(podcast_feed.xmlUrl))

    # print("Writting JSON data")
    Update_feeds.writeFeeds(json_data)


now = datetime.now()
timestamp = datetime.timestamp(now)
st = os.stat('podcasts.json')
mtime = st.st_mtime

timeDiff = (timestamp - mtime)

if os.getenv('total_podcast_to_play') is None:
    total_podcast_to_play = 20
else:
    total_podcast_to_play = int(os.getenv('total_podcast_to_play'))

chromecast_name = "Xander Room"

if os.getenv('chromecast_name') is not None:
    chromecast_name = ios.getenv('chromecast_name')

if timeDiff >= 604800 or True:
    getUpdate()

with open('podcasts.json') as json_file:
    podcast_data = json.load(json_file)

if len(podcast_data) == 0:
    getUpdate()
    with open('podcasts.json') as json_file:
        podcast_data = json.load(json_file)

podcasts_to_play = []

logging.info(f'Going to play: {total_podcast_to_play}')
logging.info(f'Chromecast: {chromecast_name}')

logging.info("Selecting Podcasts")

count=0

while len(podcasts_to_play) < total_podcast_to_play:
    podCast_selected = random.choice(podcast_data)
    podcasts_to_play.append(podCast_selected)
    podcast_title = podCast_selected['title']
    logging.info(f'{count} : {podcast_title}')
    count=count+1

ChromeCasts,browser = pychromecast.get_listed_chromecasts(friendly_names=[chromecast_name])


ChromeCast = next(ChromeCast for ChromeCast in ChromeCasts )
ChromeCast.wait()

p = Player(ChromeCast)
p.play(podcasts_to_play)