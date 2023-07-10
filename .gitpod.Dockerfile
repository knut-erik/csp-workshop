# You can find the new timestamped tags here: https://hub.docker.com/r/gitpod/workspace-full/tags
FROM python:3.9.17-slim-bullseye

# Install custom tools, runtime, etc.
RUN apt-get update && apt-get -y upgrade
RUN apt-get install python3 -y
RUN apt-get install python3-flask -y
RUN pip3 install flask

WORKDIR /tmp/flaskapp
ENV FLASK_APP=vuln_app.py
ENV FLASK_ENV=development
EXPOSE 8080

CMD [ "flask", "run" ]
