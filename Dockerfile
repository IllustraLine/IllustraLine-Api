FROM python:latest

WORKDIR /app 

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


COPY . .

ENV POSTGRESQL_URL=postgresql://postgres:postgres@db:5432/IllustraLine

EXPOSE 5000

CMD ["flask", "run"]
