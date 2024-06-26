FROM python:latest

WORKDIR /app 

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


COPY . .

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_DEBUG=1
ENV POSTGRESQL_URL=postgresql://postgres:postgres@db:5432/IllustraLine

EXPOSE 5000

CMD ["flask", "run"]
