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
        key = slugify(link)
        sites[key] = {}
        sites[key]['src'] = link

        user_agent = flask.request.user_agent

        try:
            ext_res = requests.get(link, headers={'user-agent': str(user_agent)})
            ext_res.raise_for_status()

            content_type = ext_res.headers.get('content-type')
            if not content_type.startswith('text/html'):
                raise requests.HTTPError('Wrong content type')

            link_soup = BeautifulSoup(ext_res.text)
            sites[key]['body'] = ''.join(str(tag) for tag in link_soup.body)
        except (requests.ConnectionError, requests.HTTPError) as e:
            sites[key]['body'] = 'Failed to load with error {}.'.format(e)

    return flask.render_template('index.html', sites=sites)
