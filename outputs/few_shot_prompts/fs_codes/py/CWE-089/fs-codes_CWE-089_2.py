first:
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cur = db.cursor()
    cur.execute("INSERT INTO buy_orders VALUES('"+stock_name+"','"+stock_quantity+"','"+username+"')")
    db.commit()
    db.close()

    #call the order_filled script
    args = ['python', 'order_filled.py']
    proc = subprocess.Popen(args)
    proc.communicate()

    return redirect("http://127.0.0.1:8078/home")


second:
from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

@app.route('/buy_order', methods=['POST'])

def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    #insert the buy order in the database

###
first:
	email = request.args.get('email')
	db = MySQLdb.connect(user=os.environ['C9_USER'], passwd=os.environ['DB_PASS'], db=os.environ['DB_NAME'])
	c = db.cursor()
	try:
		c.execute("DELETE FROM users WHERE email='" + email + "'")
		c.execute("DELETE FROM subscriptions WHERE email='" + email + "'")
		db.commit()
	except:
		pass
	finally:
		c.close()
		db.close()

second:
from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

#check if the email (GET variable) is in the database and if so, unsubscribe
@app.route('/unsubscribe')

def unsubscribe_user():

###
first:

def show_user(request, username):
    with connection.cursor() as cursor:
        # BAD -- Using string formatting
        cursor.execute("SELECT * FROM users WHERE username = '%s'" % username)
        user = cursor.fetchone()

urlpatterns = [url(r'^users/(?P<username>[^/]+)$', show_user)]
second:
from django.conf.urls import url
from django.db import connection

def show_user(request, username):
    '''
    create a cursor to get user info from users table and return it
    '''

###
first:
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE username = '%s'" % username)
    
urlpatterns = [url(r'^remove/(?P<username>[^/]+)$', remove_user)]
second:
from django.conf.urls import url
from django.db import connection