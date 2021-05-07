FROM python:buster

COPY ["powercasts","cast.py","player.py","update_feeds.py", "requirements.txt", "podcasts.xml", "./"]

RUN echo '[]' > podcasts.json; pip install -r requirements.txt

CMD [ "python", "cast.py" ]