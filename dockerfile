FROM python:3.10

WORKDIR /app
COPY . .
RUN curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-17.04.0-ce.tgz \
  && tar xzvf docker-17.04.0-ce.tgz \
  && mv docker/docker /usr/local/bin \
  && rm -r docker docker-17.04.0-ce.tgz
RUN pip install flask
EXPOSE 5000
ENV FLASK_APP=main.py

CMD ["flask", "run", "--host", "0.0.0.0"]
