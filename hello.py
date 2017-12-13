#encoding:utf8
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def hello_world():
    content = 'Hello Xxbao!'
    return render_template('hello.html', content = content)

if __name__ == '__main__':
    app.run('0.0.0.0')
