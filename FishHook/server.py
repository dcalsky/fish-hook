from sanic import Sanic
from sanic.response import json

app = Sanic()


def errorHandler(msg):
    return json({'message': msg})


@app.route("/lovesome")
async def test(request):
    headers = request.headers
    if not check_header(headers):
        return json({"message": "Lack of some special fields in request header"})
    return json({"ok": "true"})

def check_header(headers):
    required_headers = (
        'X-GitHub-Event', 'X-Hub-Signature', 'X-GitHub-Delivery')
    return False not in [(lambda header: header in headers)(header) for header in required_headers]