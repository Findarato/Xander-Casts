FROM python:3


COPY ["powercasts","cast.py", "requirements.txt", "podcasts_xander.xml", "podcasts_xander.txt", "./"]

RUN pip install -r requirements.txt

CMD [ "python", "./cast.py" ]