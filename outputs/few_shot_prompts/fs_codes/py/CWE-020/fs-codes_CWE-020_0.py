first:
    raw_data = request.args.get("data").encode('utf-8')
    data = base64.decodebytes(raw_data)
    obj = pickle.loads(data)
    return obj
second:
import base64
import pickle

from flask import Flask, request
app = Flask(__name__)

@app.route("/example")
def profile():
    '''
    get raw_data from request with utf-8 encoding and decode it with base64
    load the decoded data with pickle and store it in a variable and return it
    '''

###
first:
    target = request.args.get('target', '')
    if "example.com" in target:
        return redirect(target)
second:
from flask import Flask, redirect

app = Flask(__name__)

@app.route('/app')
def redirect_it(request):
    '''
    get target from request and check if it contains a valid domain
    then redirect to the target
    '''

###
first:
    regex = re.compile("(www|beta).example.com/")
    if regex.match(target):
        return redirect(target)
second:
from flask import Flask, redirect
import re

app = Flask(__name__)

@app.route('/some/path')
def targetRedirection(request):
    '''
    get target from request
    use a reqular expression to check if it is a valid target
    then redirect to the target
    '''
    target = request.args.get('target')

###
first:
    regex = re.compile("(www|beta).example.com/")

    if regex.match(url):
        return True
    else:
        return False
second:
import re