"""
Project specific settings
"""
from .defaults import *

# Admins receive 500 errors, managers receive 404 errors.
ADMINS = (
    ('{{ project_name }}', 'fhpt@yandex.ru'),
)
MANAGERS = ADMINS

DEFAULT_FROM_EMAIL = 'sysadmin@default.com'
EMAIL_SUBJECT_PREFIX = '[Django][{{ project_name }}] '

# Database to use
DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.mysql',
        'NAME':     '{{ project_name }}',
        'USER':     '{{ project_name }}',
        'PASSWORD': '',
        'OPTIONS':  {'autocommit': True,},   # Stop that "current transaction is aborted" error
    },
}

SECRET_KEY = '{{ secret_key|safe }}'

# Apps to use
INSTALLED_APPS += (
    # Site parts
    'frontend',

    # Support libs
    'google_analytics',
    'crispy_forms',
    #django-cms
    'menus',
    'sekizai',
    'filer',
    'mptt',
    'easy_thumbnails',
    'cms',
    'cms.plugins.text',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',

    'django.contrib.admin',
)

MIDDLEWARE_CLASSES += (
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'frontend.context_processors.site',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)

# Consistent date formatting
FORMAT_MODULE_PATH = '{{ project_name }}.settings.locale'

# App specific settings


#site name used in <title>
SITE_VERBOSE_NAME = '{{ project_name }}'
SITE_TAGLINE = '{{ project_name }}'

USE_LESS = False

#django-cms
CMS_TEMPLATES = (
    ('cms_template.html', 'Default cms_template'),
)

# django-filer installation:
# https://django-filer.readthedocs.org/en/latest/installation.html
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
