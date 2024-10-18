import requests
import random
import json
EMBEDDER_DIMENSIONS = 512

def request_endpoint():
    embedding = []
    i = 0
    while i < EMBEDDER_DIMENSIONS:
        embedding.append(random.randint(0, 1))
    
    body = {}
    body["question"] = embedding
    body_json = json.dumps(body)
    response = requests.post("localhost://5000/suggest", body=body_json)
    return response

def test_suggest_endpoint():

    response = request_endpoint()
    assert response.status_code == 200

def test_response_format():
    response = request_endpoint()
    assert response.json()