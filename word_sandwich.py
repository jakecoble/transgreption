import flask
import requests
from bs4 import BeautifulSoup
from slugify import slugify

app = flask.Flask(__name__)

@app.route('/')
def fetch():
    url = flask.request.args.get('q')
    res = requests.get(url)

    soup = BeautifulSoup(res.text)
    links = [anchor.get('href') for anchor in soup.find_all('a')]

    sites = {}
    for link in links:
        ext_res = requests.get(link)
        key = slugify(link)
        sites[key] = ext_res.text

    return flask.render_template('index.html', sites=sites)
