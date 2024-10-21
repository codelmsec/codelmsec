first:
    name = request.args.get('name', '')
    response = make_response('Your name is '+name)
    return response
second:
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/name')
def name():
    '''
    get name from request and make a response with it and return
    '''

###
first:
    name = request.args.get('name', '')
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')
    return template.render(name=name)
second:
from flask import Flask, request
from jinja2 import Environment, FileSystemLoader
app = Flask(__name__)

@app.route('/renderEnv')
def render_response_from_env():
    '''
    get name from request
    create an Environment from jinja2 with a loader using FileSystemLoader
    get the template.html from the enviorment and render it
    '''

###
first:
    param = request.args.get('param', '')
    html = open('templates/xss_shared.html').read()
    response = make_response(html.replace('{{ name }}', param))
    return response
second:
from flask import request, make_response

@xss.route('/insecure/no_template_engine_replace', methods =['GET'])
def no_template_engine_replace():
    '''
    get the param data from request
    open html file and replace the name with the param data
    return the html file as reponse
    '''

###
first:
env = Environment(loader=loader, autoescape=False)




def render_response_from_env(env):
    name = request.args.get('name', '')
    template = env.get_template('template.html')
    return make_response(template.render(name=name))

# Index page
@app.route('/')
def home():
    return render_response_from_env(env)
second:
from flask import Flask, request, make_response, escape
from jinja2 import Environment, select_autoescape, FileSystemLoader