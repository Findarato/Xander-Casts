
#!/usr/bin/env python

import os,random
import pychromecast
from datetime import datetime
from player import Player

now = datetime.now()
timestamp = datetime.timestamp(now)
st = os.stat('./podcasts.txt')
mtime = st.st_mtime

timeDiff = (timestamp - mtime)

if os.getenv('total_podcast_to_play') == None:
    total_podcast_to_play = 20
else:
    total_podcast_to_play = int(os.getenv('total_podcast_to_play'))


if os.getenv('chromecast_name') == None:
    chromecast_name = "Xander Room"
else:
    chromecast_name = ios.getenv('chromecast_name')

if timeDiff >=604800:
# if timeDiff >=10:
    import powercasts.opml_parser_2 as parser2
    parser2.main("podcasts.xml")


countLines = len(open("podcasts.txt").readlines(  ))
Xander_podcasts = [0 for i in range(int(countLines))]
podcasts_to_play = [0 for i in range(total_podcast_to_play)]
podcastList = 1
counter = 0
with open("podcasts.txt") as podcasts:
    for line in podcasts:
        Xander_podcasts[int(counter)] = dict( content_type="audio/mp3", url=line,title="Princess and the Dragon", thumb="https://secureimg.stitcher.com/feedimagesplain328/71464.jpg")
        counter = counter + 1
# Lets just make sure He has the princess and the dragon
podcasts_to_play[0] = dict( content_type="audio/mp3", url="https://chtbl.com/track/11GGG/media.blubrry.com/storytime/media.bedtime.fm/story-time_90.mp3" title="Princess and the Dragon", thumb="https://secureimg.stitcher.com/feedimagesplain328/71464.jpg")

while podcastList < total_podcast_to_play:
    podcasts_to_play[podcastList] = random.choice(Xander_podcasts)
    podcastList = podcastList +1

ChromeCasts=pychromecast.get_chromecasts()
ChromeCast = next(ChromeCast for ChromeCast in ChromeCasts if ChromeCast.device.friendly_name == chromecast_name)

# print(ChromeCasts)

p=Player(ChromeCast)
p.play( podcasts_to_play )