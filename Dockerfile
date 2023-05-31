FROM python:3.9-bullseye

COPY ["powercasts","cast.py","player.py","update_feeds.py", "requirements.txt", "podcasts.xml", "./"]

RUN echo '[]' > podcasts.json;

RUN pip install -r requirements.txt

CMD [ "python", "cast.py" ]