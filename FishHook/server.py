from sanic import Sanic
from sanic.response import json
from hashlib import sha1
import hmac

app = Sanic()


def sign(secret, body):
    hashed = hmac.new(secret, body, sha1)
    return hashed.hexdigest()


def errorHandler(msg):
    return json({'message': msg})


@app.post("/lovesome")
async def test(request):
    headers = request.headers
    body = request.body
    secret = 'react'
    signature = 'sha1=' + sign(secret.encode(encoding='utf-8'), body)
    print(signature)
    # Check headers
    if not check_header(headers):
        return json({"message": "Lack of some special fields in request header!"}, 400)
    # Check signature
    if signature != headers['X-Hub-Signature']:
      return json({'message': "Wrong secret!"}, 400)

    return json({'message': 'Ok!'})


def check_header(headers):
    required_headers = (
        'X-GitHub-Event', 'X-Hub-Signature', 'X-GitHub-Delivery')
    return False not in [(lambda header: header in headers)(header) for header in required_headers]
