import flask
import requests
from bs4 import BeautifulSoup
from slugify import slugify
from livereload import Server
from url_normalize import url_normalize
import url_transforms

app = flask.Flask(__name__)


@app.route('/')
def fetch():
    url = flask.request.args.get('q')

    if not url:
        return flask.render_template('no-url.html')

    try:
        res = requests.get(url_normalize(url))

        soup = BeautifulSoup(res.text)
        links = [anchor.get('href') for anchor in soup.find_all('a')]

    except Exception as e:
        return flask.render_template('error.html', error=str(e))

    sites = {}
    for raw_link in links:
        link = url_transforms.apply(raw_link)
        key = slugify(link)
        sites[key] = {}
        sites[key]['src'] = link
        sites[key]['title'] = raw_link
        sites[key]['raw_text'] = False

        user_agent = flask.request.user_agent

        try:
            ext_res = requests.get(link, headers={'user-agent': str(user_agent)})
            ext_res.raise_for_status()

            content_type = ext_res.headers.get('content-type')
            if content_type.startswith('text/html'):
                link_soup = BeautifulSoup(ext_res.text)
                sites[key]['title'] = ''.join(str(tag) for tag in link_soup.find('title'))
                sites[key]['body'] = ''.join(str(tag) for tag in link_soup.body)
            elif content_type.startswith('text/plain'):
                sites[key]['body'] = ext_res.text
                sites[key]['raw_text'] = True
            else:
                raise requests.HTTPError('Wrong content type')

            sites[key]['error'] = False
        except Exception as e:
            sites[key]['error'] = True
            sites[key]['body'] = str(e)

    return flask.render_template('index.html', sites=sites)


if __name__ == '__main__':
    app.debug = True
    server = Server(app.wsgi_app)
    server.serve()
