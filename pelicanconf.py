#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Bonnie Chan'
SITENAME = u'bonnie.io'
TAGLINE = 'Weaving codes and yarn'
SITEURL = 'http://bonnie.io'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

TYPOGRIFY = True

# Date Format
DATE_FORMATS = {
    'en': '%a, %d %b %Y',
}

LOCALE = ('en_GB')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Menu
MENUITEMS = (
    ("About", "about"),
    ("Posts", "archives.html"),
    ("Projects", "projects"),
    ("Contact", "contact"),
)


# Blogroll
# LINKS =  (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('github', 'http://github.com/livinghood'),
          ('linkedin-square', 'https://www.linkedin.com/pub/bonnie-chan/27/368/a99'),
          ('twitter', 'http://twitter.com/livinghood'),
          ('rss-square', 'http://www.bonnie.io/feeds/all.atom.xml'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = False


THEME = "themes/pure-single"
COVER_IMG_URL = "/images/bg.jpg"
PROFILE_IMG_URL = "/images/profile02.png"

STATIC_PATHS = ['CNAME', 'images',]

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

PYGMENTS_RST_OPTIONS = {'classprefix': 'pgcss', 'linenos': 'table'}
