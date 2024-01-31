from fastapi import FastAPI, HTTPException
from src.pred.image_classifier import *
from fastapi.middleware.cors import CORSMiddleware
from src.schemas.image_schema import Img
from mangum import Mangum

app = FastAPI(title="Image Classifier API")
handler = Mangum(app) # Wrap the API with a handler that we will package and deploy as a Lambda function

origins = [
    "http://localhost:3000",  # to download torch model online??
    "localhost:3000",
    "*",
    "http://127.0.0.1:8089/",
]

# To allow cross-origin requests
# Used when backend is in a different "origin" than the frontend.
    # backend must have a list of "allowed origins".
# More at https://fastapi.tiangolo.com/tutorial/cors/
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def read_main():
    return {"msg": "Hello World !!!!"}


@app.post("/predict/torch_model", status_code=200)
async def predict_torch(request: Img):
    prediction = torch_run_classifier(request.img_url)
    if not prediction:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail="Image could not be downloaded"

        )

    return {"status_code": 200,
            "predicted_label": prediction[0],
            "probability": prediction[1]}


@app.post("/predict/tf", status_code=200)
async def predict_tf(request: Img):
    prediction = tf_run_classifier(request.img_url)
    if not prediction:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail="Image could not be downloaded"

        )

    return prediction
