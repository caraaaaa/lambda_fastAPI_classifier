FROM python:3.7.5-slim

RUN pip install --upgrade pip
WORKDIR /code

COPY ./env/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src ./src/
RUN python ./src/pred/models/torch_pred.py

CMD ["python", "./src/main.py"]