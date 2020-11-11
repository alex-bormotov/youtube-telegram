FROM python:3.8.5-slim-buster

ENV LD_LIBRARY_PATH /usr/local/lib

WORKDIR /youtube-telegram

COPY . /youtube-telegram

RUN pip3 install -r requirements.txt --no-cache-dir

CMD [ "python3", "./app.py" ]