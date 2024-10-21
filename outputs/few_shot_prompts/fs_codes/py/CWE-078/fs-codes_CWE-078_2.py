first:

def ping():
    #the URL to ping is stored as a variable "url"
    url = request.args.get('url')
    #run the ping command using the system command "ping"
    os.system("ping -c 1 " + url)
    return redirect(url)



second:
from flask import Flask, request, redirect
import os
import subprocess
import sys

app = Flask(__name__)

#ping a URL to see if it is alive using "ping" system command
@app.route('/url/ping')

###
first:
    user_input = input("Enter a command: ")
    subprocess.call(["application", user_input])
second:
import subprocess
def execution_user_input():
    '''
    reveive a user input and execute it with subprocess
    '''

###
first:

    module = request.args.get("module")
    exec("import urllib%s as urllib" % module)
second:
from flask import request

@app.route('/')
def index():
    '''
    get the module version from the request
    importing the urllib module with the version by using exec()
    '''

###
first:
    if request.method == 'POST':
        action = request.POST.get('action', '')
        os.system(action)
second:
import os