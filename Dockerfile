FROM python:3.6-alpine
ADD . /app
WORKDIR /app
ENV FLASK_APP=project
RUN python3 setup.py install
RUN flask init-db
CMD flask run --host=0.0.0.0
