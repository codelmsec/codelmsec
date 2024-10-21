first:
    url = request.args["next"]
    response = Response("redirecting...", 302)
    response.headers['Location'] = url  
    return response
second:
from flask import request, Response, Flask
app = Flask(__name__)
@app.route('set_location_header')
def set_location_header():
    '''
    get url data from the request and set the location header for redirecting
    '''

###
first:
    target = request.GET.get('target', '/')
    return HttpResponseRedirect(target)
second:
from django.http import HttpResponseRedirect

def http_responser_redirect(request):
    '''
    get the target url from the request and redirect to it
    '''

###
first:
    url = request.args["next"]
    return redirect(url)
second:
from flask import request, redirect, Flask
app = Flask(__name__)
@app.route('flask_redirect')
def flask_redirect():
    '''
    get the url from the request and redirect to it
    '''

###
first:
    target = request.args.get('target', '')
    return redirect(target, code=302)
second:
from flask import Flask, request, redirect