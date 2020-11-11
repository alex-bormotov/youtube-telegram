FROM python:3.8.5-slim-buster
ENV LD_LIBRARY_PATH /usr/local/lib
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
WORKDIR /youtube-telegram
COPY . /youtube-telegram
RUN pip3 install -r requirements.txt --no-cache-dir
CMD [ "python3", "./app.py" ]