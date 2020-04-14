FROM python:3


COPY ["powercasts","cast.py","player.py", "requirements.txt", "podcasts.xml", "podcasts.txt", "./"]

RUN pip install -r requirements.txt

CMD [ "python", "cast.py" ]