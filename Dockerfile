FROM python:3.11-bullseye

# COPY ["powercasts","cast.py","player.py","update_feeds.py", "requirements.txt", "podcasts.xml", "./"]
COPY [ \
    "cast.py", \
    "podcast_player.py", \
    "book_player.py", \
    "player.py", \
    "update_feeds.py",  \
    "requirements.txt", \
    "podcasts.xml", \
    "./" \
    ]

ENV CAST_NAME='Xander Room'
ENV TOTAL_PODCASTS_TO_PLAY=5
ENV PLAYER_TYPE='Podcast'
ENV BOOK_URL="http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"


RUN echo '[]' > podcasts.json;

RUN pip install -r requirements.txt

CMD [ "python", "cast.py" ]