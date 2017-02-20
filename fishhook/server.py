from sanic import Sanic
from sanic.response import json
from hashlib import sha1
from .handler import Handler
from .settings import REQUIRED_HEADERS
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
    if loss_header(headers):
        return json({"message": "Lack of some special fields in request header!"}, status=400) # Status: 400

    # Check signature
    correct_signature = headers['x-hub-signature']
    if signature != correct_signature:
      return json({'message': "Wrong secret!"}, status=400) # Status: 400

    # Get the event from Github
    event = headers['x-github-event']

    # If event is `ping`, ignore it
    if event != 'ping':
        handler.launch(event) # Distribute event to handler

    return json({'message': 'ok!'})

def loss_header(headers):
    return len(REQUIRED_HEADERS - headers.keys()) != 0
