# Serving ML Model with FastAPI

### Models
- Tensorflow MobileNet_V2 (Pretrained)
- Pytorch AlexNet (Pretrained)

## Pre-requisites
* Python (3.6+)

## Folder structure
```bash
fastAPI_object_classifier
├── env
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── environment.yml
│   └── requirements.txt
├── src
│   ├── app
│   │   └── app.py
│   ├── pred
│   │   ├── models
│   │   │   ├── tf_pred.py
│   │   │   └── torch_pred.py
│   │   └── image_classifier.py
│   ├── schemas
│   │   └── image_schema.py
│   ├── utils
│   │   ├── test_images.py
│   │   └── utilities.py
│   └── main.py
└── tests
    ├── performance-tests
    ├── unit-tests
    └── helpers.py

```

## Running the Code
* Server should be running at `http://127.0.0.1:8000/docs`
### With Conda
```bash
conda env create -f env/environment.yml
conda activate FastAPI_classifier
python3 src/main.py
```
### With Docker
```bash
docker build -f env/Dockerfile -t fastapiimage .
docker run --name fastapicontainer -p 8000:8000 fastapiimage
```
### With Docker-compose
```bash
docker-compose -f env/docker-compose.yml up --build
```
- To stop Docker-compose (inside the project directory)
```bash
docker-compose down
```

## Testing Result
### In terminal
```
curl -X 'POST' \
  'http://127.0.0.1:8000/predict/torch_model/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"img_url": "<image_url>"}'
```
### In webpage 
`http://127.0.0.1:8000/docs`
![Alt text](images/webpage_outlook.png) 
- Insert image url to `string`, then hit `Excecute`

![Alt text](images/webpage_testing.png)

## Testing the End points (TBC)

### Simple Testing
```bash
python3 test-api.py
```

### Running Unit Tests
```bash
pytest
```

### Running the performance Tests using Locust
```bash
locust -f tests/performance_test.py
```
* Tests should appear at `http://127.0.0.1:8089/`