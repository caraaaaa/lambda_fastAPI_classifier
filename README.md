# Serving ML Model with FastAPI

### Model Deployment
- Serve ML model using FastAPI
- Containarize ML application using Docker/ docker-compose
- Conduct performance test using Locust

## DEMO
Testing image
![](https://www.southernliving.com/thmb/Rz-dYEhwq_82C5_Y9GLH2ZlEoYw=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/gettyimages-837898820-1-4deae142d4d0403dbb6cb542bfc56934.jpg)

Inference UI
![](images/image_classifier_demo.gif)

Performace test with Lucust
![](images/performance_test_demo.gif)


## Quick Start
#### With Conda
```bash
conda env create -f env/environment.yml
conda activate FastAPI_classifier
python3 src/main.py
```
#### With Docker
```bash
docker build -f env/Dockerfile -t fastapiimage .
docker run --name fastapicontainer -p 8000:8000 fastapiimage
```
#### With Docker-compose
```bash
docker-compose -f env/docker-compose.yml up --build
```
- To stop Docker-compose (inside the project directory)
```bash
docker-compose -f env/docker-compose.yml down
```

## Inference
#### In terminal
```
curl -X 'POST' \
  'http://127.0.0.1:8000/predict/torch_model/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"img_url": "<image_url>"}'
```
#### In webpage 
Inference UI can be accessed at `http://127.0.0.1:8000/docs`


## Performance Test for the End-point(s)
#### Running Unit Tests
```bash
pytest
```

#### Running the performance Tests using Locust
```bash
locust -f tests/performance_test.py
```
* Testing monitor UI can be accessed at `http://127.0.0.1:8089/`
* In this case, set the host to be `http://127.0.0.1:8000`to test


## Models Used
- Pretrained MobileNet_V2 (Tensorflow)
- Pretrained AlexNet (Pytorch)