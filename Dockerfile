FROM --platform=linux/amd64 python:3.11

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

CMD ["python3", "main.py"] 