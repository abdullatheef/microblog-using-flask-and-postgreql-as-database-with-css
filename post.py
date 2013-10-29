#import sqlite3
import psycopg2
import os
#from functools import wraps
from flask import *
#from flask.ext.sqlalchemy import SQLAlchemy
import db
import urlparse
#DATABASE = 'a'

app=Flask(__name__)
app.config.from_object(__name__)


#def connect_db():
#	return sqlite3.connect(app.config['DATABASE'])


@app.route('/')

def a():
	return render_template('new.html')

@app.route('/new1')
def b():
	return render_template('new1.html')

@app.route('/post',methods=['POST'])
def add_entry():
	urlparse.uses_netloc.append("postgres")
	url = urlparse.urlparse(os.environ["DATABASE_URL"])
	con = psycopg2.connect(database=url.path[1:],user=url.username,password=url.password,host=url.hostname,port=url.port)
#	con = psycopg2.connect(database='db') 
    	cur = con.cursor()

#	cur.execute("insert into posts (title, text) values ('sdfsff','fhjfjjj')")
	cur.execute("insert into posts (title, text) values (%s, %s)",[request.form['title'],request.form['text']])
	con.commit()
	cur.close()
	con.close()
	return redirect(url_for('show_entries'))


@app.route('/post',methods=['GET'])
def show_entries():
#	con = psycopg2.connect(database='db')
	urlparse.uses_netloc.append("postgres")
	url = urlparse.urlparse(os.environ["DATABASE_URL"])
	con = psycopg2.connect(database=url.path[1:],user=url.username,password=url.password,host=url.hostname,port=url.port)
    	cur = con.cursor()
	cur.execute('select title, text from posts order by id desc')
	posts = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
	return render_template('post.html',posts=posts)

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
    	app.run(host='0.0.0.0', port=port)
#
#
