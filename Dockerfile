FROM python:3

WORKDIR /usr/src/app

COPY requirements_docker.txt ./
RUN pip install --no-cache-dir -r requirements_docker.txt

COPY . .

CMD [ "python", "./main.py" ]
