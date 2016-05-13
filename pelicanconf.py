#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'qxh'
SITENAME = u"def qxh():"
SITEURL = 'http://qxh.im'
SITESUBTITLE = '&nbsp;&nbsp;&nbsp;&nbsp;return <a href="/category/python.html">Pythoner()</a>, <a href="/category/ios.html">IOSdev()</a>'

RECENT_POST_COUNT = 5
EXPAND_LATEST_ON_INDEX = True
OPEN_GRAPH = True
OPEN_GRAPH_IMAGE = True

SHARE = True
SITELOGO = '/images/logo.png'
SITELOGO_SIZE = 200
HIDE_SITENAME = True
DISPLAY_RECENT_POSTS_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_TAGS_ON_MENU = True

TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 20
TAG_CLOUD_SORTING = 'random'
TAG_CLOUD_BADGE = True

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
         ('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
)

# Social widget
SOCIAL = (
        ('Github', 'https://github.com/holyq'),
)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Disqus
#DISQUS_SITENAME = u"qxh"
DUOSHUO_SITENAME = u"qxh"

# Content path
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['images', 'files']
EXTRA_PATH_METADATA = {
    'files/robots.txt': {'path': 'robots.txt'},
    'images/favicon.ico': {'path': 'favicon.ico'},
}

COVER_IMG_URL = '/images/cover.jpg'
PROFILE_IMAGE_URL = '/images/avatar.jpg'
ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
PAGE_LANG_SAVE_AS = False
# Feed
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
# Theme
THEME = 'pelican-themes/pelican-twitchy'
DEFAULT_PAGINATION = 10
MD_EXTENSIONS = (['codehilite(css_class=highlight)', 'extra',
                  'fenced_code', 'tables', 'sane_lists'])
# Plugin
PLUGIN_PATHS = ['/Users/qxh/pelican-plugins']
PLUGINS = [ 'sitemap', 'gravatar', ]
# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'pages': 0.9,
        'indexes': 0.8,
    },
    'changefreqs': {
        'indexes': 'daily',
        'articles': 'daily',
        'pages': 'weekly'
    }
}

