#import psycopg2
import sys

import os
import psycopg2
import urlparse

'''con = psycopg2.connect(database='a') 
cur = con.cursor()
cur.execute("create table posts(title TEXT,text INT)")
con.commit()
con.close()
'''
'''
from flask import *
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
db.create_all()
'''
con = None
urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

con = psycopg2.connect(database=url.path[1:],user=url.username,password=url.password,host=url.hostname,port=url.port)


#con = psycopg2.connect(database='db') 
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS posts")
cur.execute("CREATE TABLE posts(id  serial,title TEXT,text TEXT)")
#	cur.execute("insert into posts (title, text) values ('sdfsff','fhjfjjj')")
con.commit()
con.close()
#	cur.execute("create table posts(title TEXT,text INT)")
#except psycopg2.DatabaseError, e:
#    	print 'Error %s' % e    
#    	sys.exit(1)
    
    
#finally:
#    
#    	if con:
#       	con.close()
#	cur.executemany("INSERT INTO sale VALUES(?,?)",[a['title'],a['text']])

