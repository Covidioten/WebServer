FROM python:3.6-stretch
ADD . /app
WORKDIR /app
ENV FLASK_APP=project
RUN pip install -e .
RUN flask init-db
CMD flask run --host=0.0.0.0