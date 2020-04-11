#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Tema
THEME = 'themes/startbootstrap-business-frontpage'

# Para desarrollo, los vinculos son relativos
SITEURL = ''
RELATIVE_URLS = True

# Metadatos de todo el sitio web
SITENAME = 'COVID-19 Laguna'
SITELOGO = 'theme/images/covid19laguna.png'
SITEDESCRIPTION = 'Sitio web de COVID-19 Laguna'
SITETWITTER = ''

# Autor por defecto
AUTHOR = 'webmaster'

# Directorio donde esta el contenido
PATH = 'content'

# Directorios que tienen los articulos
ARTICLE_PATHS = ['comunicados']

# Directorios que tienen páginas fijas, no artículos
PAGE_PATHS = ['quienes-somos']

# Directorios y archivos que son fijos
# Agregue también los directorios que tienen archivos para artículos y páginas
STATIC_PATHS = ['comunicados', 'quienes-somos', 'favicon.ico', 'LICENSE', 'README.md', 'robots.txt']

# NO usar el directorio como la categoria
USE_FOLDER_AS_CATEGORY = False

# Los artículos van en directorios por categoria/titulo/
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'

# Las páginas fijas van en directorios categoria/titulo/
PAGE_URL = '{category}/{slug}/'
PAGE_SAVE_AS = '{category}/{slug}/index.html'

# Lenguaje y zona horaria
DEFAULT_LANG = 'es'
TIMEZONE = 'America/Mexico_City'

# Para desarrollo se desactiva la generacion de feeds
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

# NO BORRAR de output los siguientes directorios y archivos
OUTPUT_RETENTION = ['.git', '.gitignore']

# Para desarrollo DESACTIVAR la paginacion
DEFAULT_PAGINATION = False

# Para desarrollo BORRAR todo el directorio de salida
DELETE_OUTPUT_DIRECTORY = True

# Para desarrollo DESACTIVAR el caché
LOAD_CONTENT_CACHE = False

# Habilita Font Awesome desde Internet
USE_REMOTE_SERVICES = True
