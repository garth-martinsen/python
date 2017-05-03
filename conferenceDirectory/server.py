import os
from bottle import route, run, static_file,TEMPLATE_PATH,template

TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "views")))


@route('/')
@route('/display')
def grid():
    return static_file('grid.html', root= '/Users/garth/TryRitzman/python/conferenceDirectory')

@route('/hello')
def hello():
    return "Hello Bottle World!"

@route('/hello/<name>')
def views(name='Garth'):
    return template('This is {{name}}, how are you?', name=name)

@route('/views/<img>')
def server_static(img):
     return static_file(img, root='/Users/garth/TryRitzman/python/conferenceDirectory/views')

run(host='192.168.1.10',port=8080,debug=True)    

