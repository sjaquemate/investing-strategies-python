from flask import make_response


def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return make_response({'m': 'return from args'})
    elif request_json and 'message' in request_json:
        return make_response({'m': 'return from json'})
    else:
        return make_response({'echo': 'Hello World!'})
    
