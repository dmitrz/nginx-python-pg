FROM python:3.8.1
WORKDIR /usr/src/app
RUN pip install psycopg2-binary flup
COPY . .
CMD [ "python", "./start.py" ]
