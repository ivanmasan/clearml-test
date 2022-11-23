FROM python:3

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .
COPY /conf .

CMD ["python3", "main.py"]
