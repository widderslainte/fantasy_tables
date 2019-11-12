from glob import glob

from flask import Flask, escape, request, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    tables = glob("*.table")
    return render_template('index.html', tables=tables)


if __name__ == '__main__':
    app.run()
