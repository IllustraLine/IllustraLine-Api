FROM python 

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

CMD ["flask", "run", "--host=0.0.0.0"]
