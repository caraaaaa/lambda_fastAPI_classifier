import sys
import os
sys.path.insert(0, os.getcwd())
import random

from src.utils.test_images import image_links
import json
from src.schemas.image_schema import Img

def predict_test(client, api_url):
    sample = Img(img_url=random.choice(image_links)['url'])
    headers = {'Accept': 'application/json',
               'Content-Type': 'application/json'}
    res = client.post(api_url,
                      data=json.dumps(sample.dict()),
                      headers=headers)
    return res.json()
