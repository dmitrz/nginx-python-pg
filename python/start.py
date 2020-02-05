#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import cgi
import psycopg2
import sys, os
from flup.server.fcgi import WSGIServer

def app(environ, start_response):
    form = cgi.FieldStorage(fp = environ['wsgi.input'], environ = environ)
    start_response('200 OK', [('Content-Type', 'text/html')])
    con = psycopg2.connect(
      database="docker",
      user="docker",
      password='docker',
      host="db",
      port="5432")
    cur = con.cursor()
    for item in form:
      cur.execute('INSERT INTO postdata (key, value) VALUES (%s, %s)', (item, form.getvalue(item)))
    con.commit()
    yield 'OK'

bindAddress = ('0.0.0.0', int(8888))
WSGIServer(app,bindAddress=bindAddress).run()
