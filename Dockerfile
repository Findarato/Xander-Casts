FROM python:buster

COPY ["powercasts","cast.py","player.py", "requirements.txt", "podcasts.json", "podcasts.xml", "./"]

RUN pip install -r requirements.txt

CMD [ "python", "cast.py" ]