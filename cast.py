import json
import os
import random
from datetime import datetime

import opml
import pychromecast

from player import Player
from update_feeds import Update_feeds


def getUpdate():
    json_data = []

    outline = opml.parse("podcasts.xml")

    print("Getting Feeds")
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

if os.getenv('chromecast_name') is None:
    chromecast_name = "Xander Room"
else:
    chromecast_name = ios.getenv('chromecast_name')

if timeDiff >= 604800 or True:
    getUpdate()

with open('podcasts.json') as json_file:
    podcast_data = json.load(json_file)

if len(podcast_data) == 0:
    getUpdate()
    with open('podcasts.json') as json_file:
        podcast_data = json.load(json_file)

# print(json.dumps(data, indent=4))

podcasts_to_play = []


podcastList = 0

while len(podcasts_to_play) < total_podcast_to_play:
    podCast_selected = random.choice(podcast_data)

ChromeCasts = pychromecast.get_chromecasts()
ChromeCast = next(ChromeCast for ChromeCast in ChromeCasts if ChromeCast.device.friendly_name == chromecast_name)

p = Player(ChromeCast)
p.play(podcasts_to_play)
