first:
    try:
        userInput = input("Enter a number: ")
        userInput = int(userInput)
    except ValueError:
        logging.error("The input was not a number: " + userInput)
    return userInput
second:
import logging
def inputConversion():
    '''
    take a string input from the user
    convert it to an integer within try-except block and log the error
    return the user input after converting it to an integer
    '''

###
first:
    input = request.args.get('input')
    current_app.logger.error("%s", input)
second:
from flask import request, current_app, Flask

app = Flask(__name__)
@app.route('/log')
def log():
    '''
    get the input from the request and log it as an error
    '''

###
first:
    oldContent = ""
    while oldContent != content:
        oldContent = content
        content = re.sub(r'<script.*?>.*?</script>', '', content, flags= re.DOTALL | re.IGNORECASE)
    return content
second:
import re

def filterScriptTags(content): 
    '''
    remove script tags from content argument
    '''

###
first:
    name = request.args.get('name')
    app.logger.info('User name: ' + name) 
second:
from flask import Flask
from flask import request
import logging