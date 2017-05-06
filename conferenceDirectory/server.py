#server.py
""" Bottle Web server to serve up conference Directory"""
import os
from bottle import route, run, static_file,TEMPLATE_PATH
TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "views")))

rootDir = '/Users/garth/Programming/Python/python3/ritzman'
ipAddress = '192.168.1.10'
viewDir = rootDir + '/views'

@route('/')

@route('/display')
def grid():
    return static_file('grid.html', root= rootDir) 

@route('/views/<img>')
def server_static(img):
     return static_file(img, root= viewDir )

run(host=ipAddress,port=8080,debug=True)    

