import requests
import json

def request_endpoint():

    body = {}
    body["question"] = "What is Python"
    body_json = json.dumps(body)

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post("http://localhost:5001/suggest", data=body_json, headers=headers)
    return response

def test_suggest_endpoint():

    response = request_endpoint()
    assert response.status_code == 200

def test_response_format():
    response = request_endpoint()
    assert 'tags' in response.json().keys()