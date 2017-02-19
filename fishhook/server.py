from sanic import Sanic
from sanic.response import json
from hashlib import sha1
from .handler import Handler
import hmac

server = Sanic()

def sign(secret, body):
    hashed = hmac.new(secret, body, sha1)
    return hashed.hexdigest()


def errorHandler(msg):
    return json({'message': msg})


@server.post("/<name>")
async def serve(request, name):
    headers = request.headers
    body = request.body
    handler = Handler(name)
    secret = handler.config.get('secret', '') # todo: if no secret field, throw error

    signature = 'sha1=' + sign(secret.encode(encoding='utf-8'), body)
    # Check headers
    if not check_header(headers):
        return json({"message": "Lack of some special fields in request header!"}, 400) # Status: 400
    # Check signature
    if signature != headers['X-Hub-Signature']:
      return json({'message': "Wrong secret!"}, 400) # Status: 400

    event = headers['X-GitHub-Event']
    handler.launch(event)
    return json({'message': 'ok!'})


def check_header(headers):
    required_headers = (
        'X-GitHub-Event', 'X-Hub-Signature', 'X-GitHub-Delivery')
    return len(required_headers - headers.keys()) == 0
