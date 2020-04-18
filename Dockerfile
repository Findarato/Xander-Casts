FROM alpine-python3

COPY ["powercasts","cast.py","player.py","update_feeds.py", "requirements.txt", "podcasts.json", "podcasts.xml", "./"]

RUN pip install -r requirements.txt

CMD [ "python", "cast.py" ]
