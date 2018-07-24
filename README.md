# Sentiment Analysis on Social Media

Here is an app able to search for recent tweets based on a keyword. User can view analysed tweets as positive, negative or neutral, along with relevant polarities (Sentiment Analysis with Spacy, emoji are also used). In addition, User can download csv version of tweets and sentiments. 
Application deployed with Heroku and Django is the framework used.

Here is the link: [https://sentiment-analysis-tweet-insta.herokuapp.com/](https://sentiment-analysis-tweet-insta.herokuapp.com/)

[![](https://preview.ibb.co/kiffTo/screen.png)](https://{https://ibb.co/c0huoo})


## Development Guide

1. Create a virtualenv. `virtualenv somename`
2. cd into somename/
3. Activate the virtualenv. `source bin/activate`
4. cd into src/
5. Install the requirements. `pip install -r requirements.txt`
6. Make sure to enter the `ACCESS_TOKEN`, `ACCESS_TOKEN_SECRET`, `CONSUMER_KEY`, `CONSUMER_SECRET` variables in the views.py file inside search/.
7. Run the server as localhost. `python manage.py runserver`
