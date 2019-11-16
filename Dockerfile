FROM python:3.7

WORKDIR /usr/src/app

RUN pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY transcript_all.py ./
CMD python transcript_all.py 
