#!/usr/bin/python3
from flask import Flask
app=Flask(__name__)

@app.route('/')
def helloword():
    return 'hello world flask!\n'

@app.route('/name/<name>')
def name_param(name):
    return 'you name is {}\n'.format(name)

#if __name__=='__main__':
#    print('hello')
