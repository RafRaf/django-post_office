VERSION = (2, 0, 7)

from .backends import EmailBackend, SSLEmailBackend

default_app_config = 'post_office.apps.PostOfficeConfig'
