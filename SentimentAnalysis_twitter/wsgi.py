"""
WSGI config for SentimentAnalysis_twitter project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""


import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SentimentAnalysis_twitter.settings")

application = get_wsgi_application()

# (heroku config:set DISABLE_COLLECTSTATIC=1 --app sentiment-analysis-tweet-insta)
