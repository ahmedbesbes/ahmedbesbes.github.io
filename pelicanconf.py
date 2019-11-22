#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime
import os
import sys

sys.path.append('./content/pelican-plugins/')

from liquid_tags import notebook
import related_posts
import better_code_samples


# manage pelican-plugins
PLUGINS = [notebook, related_posts, "render_math", better_code_samples]

JINJA_ENVIRONMENT = {'extensions': [
    'jinja2.ext.autoescape',
    'jinja2.ext.with_']}

MATH_JAX = {'color': 'dark', 'align': 'center'}

# Set the theme name
THEME = "Flex"
SUMMARY_MAX_LENGTH = 141

DEFAULT_DATE = 'fs'
AUTHOR = u'Ahmed Besbes'
SITEDESCRIPTION = u'Data science and programming'
SITETITLE = u'Ahmed BESBES'
SITESUBTITLE = u'Data scientist in the making'
SITENAME = 'Ahmed BESBES - Data Science Portfolio'

PATH = 'content'

CUSTOM_CSS = True
# tell Flex them where your custom.css file is in your content folder
STATIC_PATHS = ['extras/custom.css', 'images', 'extras/favicon.ico']

# tell pelican where it should copy that file to in your output folder
EXTRA_PATH_METADATA = {
    'extras/custom.css': {'path': 'static/custom.css'},
    'extras/favicon.ico': {'path': 'favicon.ico'}
}
# FAVICON = 'favicon.ico'

# tell Flex theme where to find the custom.css file in your output folder
CUSTOM_CSS = 'static/custom.css'
RELATIVE_URLS = True

SITEURL = u'http://localhost:8000'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'en'

USE_FOLDER_AS_CATEGORY = True
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = 10
MAIN_MENU = True

# PAGINATION_PATTERNS = (
#     (1, '{base_name}/', '{base_name}/index.html'),
#     (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
# )

SOCIAL = (
    ('linkedin', 'https://fr.linkedin.com/in/ahmed-besbes-99a91661'),
    ('github', 'https://github.com/ahmedbesbes'),
    ('twitter', 'https://twitter.com/ahmed_besbes_?lang=fr'),
    ('quora', 'https://www.quora.com/profile/Ahmed-Besbes'),
    ('stack-overflow', 'https://stackoverflow.com/users/4583959/ahmed-besbes'),
    ('youtube', 'https://www.youtube.com/channel/UCP1M7FpkpNljH4r6ORiRg6g?view_as=subscriber')
)

MENUITEMS = (
            ('Archives', '/archives.html'),
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html'))


#  to show the author of the article at the top of the article and in the index of articles.
SHOW_ARTICLE_AUTHOR = True

#  to show the Category of each article
SHOW_ARTICLE_CATEGORY = True

# to True to show the article modified date next to the published date.
SHOW_DATE_MODIFIED = True

# inverse nav bar
BOOTSTRAP_NAVBAR_INVERSE = False

# notebook setup
NOTEBOOK_DIR = 'notebooks'
PYGMENTS_STYLE = 'monokai'

if not os.path.exists('_nb_header.html'):
    import warnings
    warnings.warn("_nb_header.html not found.  "
                  "Rerun make html to finalize build.")
else:
    EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

# Disqus setup
DISQUS_SITENAME = True
DISQUS_NO_ID = True
DISQUS_SITENAME = "ahmedbesbes"
DISQUS_DISPLAY_COUNTS = True


# AddThis setup
ADD_THIS_ID = "ra-574974c2e12846a2"

# License and copyright
CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '1.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2019

# related posts setup

RELATED_POSTS_MAX = 10
RELATED_POSTS_SKIP_SAME_CATEGORY = True

# Google analytics
GOOGLE_ANALYTICS = "UA-79148290-1"
