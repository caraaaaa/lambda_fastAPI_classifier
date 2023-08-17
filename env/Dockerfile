FROM python:3.7.5-slim

RUN pip install --upgrade pip
WORKDIR /code

COPY ./env/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src ./src/
COPY ./src/main.py ./src/main.py
COPY ./src/app/app.py ./src/app/app.py

CMD ["python", "/src/main.py"]
