import flask
import requests
from bs4 import BeautifulSoup
from slugify import slugify
from urllib.parse import urlparse
import cssutils

app = flask.Flask(__name__)


def relative_to_absolute(host, url):
    if url.startswith('http'):
        return url

    sep = ''
    if not url.startswith('/') and not url.endswith('/'):
        sep = '/'

    return host + sep + url


def inline_css(slug, host, html):
    soup = BeautifulSoup(html)
    style_links = soup.find_all('link', rel='stylesheet')

    for link in style_links:
        url = link.get('href')
        res = requests.get(relative_to_absolute(host, url))
        style_tag = soup.new_tag('style')
        css = res.text
        sheet = cssutils.parseString(css)

        for rule in sheet:
            if rule.type == rule.STYLE_RULE:
                for selector in rule.selectorList:
                    selector.selectorText = '#{} {}'.format(slug, selector.selectorText)

        style_tag.string = str(sheet.cssText, encoding="utf-8")
        style_tag['data-sandwich'] = "source:" + url
        link.replace_with(style_tag)

    return soup


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
        parsed_link = urlparse(link)
        sites[key] = inline_css(key,
                                '{uri.scheme}://{uri.netloc}'.format(uri=parsed_link),
                                ext_res.text)

    return flask.render_template('index.html', sites=sites)
