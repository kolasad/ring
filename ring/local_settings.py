from ring.settings import *

DEBUG = True
SECRET_KEY = 'test'



EMAIL_HOST = ''
EMAIL_FROM = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_FROM = 'email@gmail.com'
# EMAIL_HOST_USER = 'email@gmail.com'
# EMAIL_HOST_PASSWORD = 'haslo'
# EMAIL_PORT = 587