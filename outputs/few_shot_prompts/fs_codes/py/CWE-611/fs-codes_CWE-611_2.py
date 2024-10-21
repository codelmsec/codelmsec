first:
    xml_src = request.get_data()
    doc = lxml.etree.fromstring(xml_src)
    return lxml.etree.tostring(doc)
second:
from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.post("/upload")
def upload():
    '''
    get the xml_src from the request, parse it and return it as string
    '''

###
first:
    xml = request.files['xml']
    root = lxml.etree.fromstring(xml.read())
    userid = root.find('userid').text
    password = root.find('password').text
    if checkPassword(userid, password):
        return "OK"
    else:
        return "ERROR"
    
second:
from flask import Flask, request
import lxml.etree

app = Flask(__name__)

def checkPassword(userid, password):
    pass

@app.post("/upload")
def upload():
    '''
    get the xml file from the request and check if the userid and password are correct
    '''

###
first:
    parser = etree.XMLParser(resolve_entities=True)
    treexsd = etree.parse('ressources/xxe.xsd', parser)
    rootxsd = treexsd.getroot()
    schema = etree.XMLSchema(rootxsd)
    return schema

second:
from lxml import etree
def get_root():
    '''
    create a XML parser, parse from a file, validate the XML and return the schema
    '''

###
first:
    parser = etree.XMLParser(resolve_entities=True)
    tree = etree.parse('ressources/xxe.xml', parser)
    root = tree.getroot()
    return root
second:
from lxml import etree