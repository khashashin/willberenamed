"""
WSGI config for treichle_cup project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""
from __future__ import absolute_import, unicode_literals

import os
from django.core.wsgi import get_wsgi_application

# Handling Key Import Errors
def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)

locale_env = get_env_variable('IM_LOCALE')

if locale_env == 'YES':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "treichle_cup.settings.dev")
    application = get_wsgi_application()
else:
    from dj_static import Cling
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "treichle_cup.settings.production")
    application = Cling(get_wsgi_application())
