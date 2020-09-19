import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html', js_file=flask.url_for('static', filename='script.js'))
