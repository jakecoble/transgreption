import re
from url_normalize import url_normalize

# Prefix your string with 'r' to create a string literal that does not require
# escaping. Note that such strings cannot end with a single backslash. See
# https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals
# for more information.
#
# Regexes are applied to a url in order until one of them matches.

TRANSFORMS = [
  { # plain text version of Google Docs
    'find':    r'/d/([0-9a-zA-Z-_]+)/edit.*$',
    'replace': r'/d/\1/export?format=txt'
  },
  { # plain text version of Etherpads
    'find':    r'/padm\.us/(\w+).*$',
    'replace': r'/padm.us/\1/export/txt',
  },
  { # Anti-Inception Hack! Intentionally break links to megadoc...
    'find':    r'transgreption\.jakecoble\.repl\.co',
    'replace': r'antiinception',
  }
]


def apply(url):
    new_url = url_normalize(url)

    for t in TRANSFORMS:
        new_url = re.sub(t['find'], t['replace'], url)
        if new_url != url:
            break

    return new_url
