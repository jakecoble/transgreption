import re
from url_normalize import url_normalize

# Prefix your string with 'r' to create a string literal that does not require
# escaping. Note that such strings cannot end with a single backslash. See
# https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals
# for more information

TRANSFORMS = [
    {
        'find': r'/d/([0-9a-zA-Z-_]+)/edit.*$',
        'replace': r'/d/\1/export?format=txt'
    }
]


def apply(url):
    new_url = url_normalize(url)

    for t in TRANSFORMS:
        new_url = re.sub(t['find'], t['replace'], url)
        if new_url != url:
            break

    return new_url
