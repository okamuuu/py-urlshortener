# -*- coding:utf-8 -*-
from bottle import  get, post, request, redirect, run, view
import sys
sys.path.append("./app/lib")
import db
import base62
import time

@get('/')
@view("index")
def get_index():
    urls = db.find({});
    return dict(urls=urls)

@post('/')
def post_index():
    url = request.forms.get('url')
    short = base62.base62_encode(int(time.time())) 
    result = db.find_and_modify({'url':url}, {'url':url,'short':short})
    redirect("/")

@get('/url/<short>')
def get_url(short):

    result = db.find_one({'short':short})
    redirect(result['url'])

run(host='localhost', port=8080, debug=True)

