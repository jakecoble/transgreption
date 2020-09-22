import flask
import requests
from bs4 import BeautifulSoup
from slugify import slugify

app = flask.Flask(__name__)


def html_or_object(link, res):
    soup = BeautifulSoup()

    if res.headers.get('content-type').startswith('text/html'):
        page = BeautifulSoup(res.text)
        soup.append(page.body)
    else:
        object_tag = soup.new_tag('object', data=link)
        soup.append(object_tag)

    return ''.join(str(tag) for tag in soup)


@app.route('/')
def fetch():
    url = flask.request.args.get('q')
    res = requests.get(url)

    soup = BeautifulSoup(res.text)
    links = [anchor.get('href') for anchor in soup.find_all('a')]

    sites = {}
    for link in links:
        key = slugify(link)
        sites[key] = {}
        sites[key]['src'] = link

        try:
            ext_res = requests.get(link)
            sites[key]['body'] = html_or_object(link, ext_res)
        except Exception as e:
            sites[key]['body'] = 'Failed to load with error {}.'.format(e)

    return flask.render_template('index.html', sites=sites)
