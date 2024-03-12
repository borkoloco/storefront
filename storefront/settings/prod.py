from .common import *
import os
import dj_database_url


SECRET_KEY = os.environ['SECRET_KEY']


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False



ALLOWED_HOSTS = ['borkbuy-prod-9b1273118507.herokuapp.com']


DATABASES = {
    'default': dj_database_url.config()
}

REDISCLOUD_URL = os.environ['REDIS_URL']

CELERY_BROKER_URL = REDISCLOUD_URL


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDISCLOUD_URL,
        "TIMEOUT": 10*60,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

EMAIL_HOST= os.environ['MAILGUN_SMTP_SERVER']
EMAIL_HOST_USER=os.environ['MAILGUN_SMTP_LOGIN']
EMAIL_HOST_PASSWORD=os.environ['MAILGUN_SMTP_PASSWORD']
EMAIL_PORT=os.environ['MAILGUN_SMTP_PORT']
# DEFAULT_FROM_EMAIL='from@borkbuy.com'