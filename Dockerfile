FROM python:buster

RUN echo '[]' > podcasts.json; pip install -r requirements.txt

COPY ["powercasts","cast.py","player.py","update_feeds.py", "requirements.txt", "podcasts.xml", "./"]

CMD [ "python", "cast.py" ]