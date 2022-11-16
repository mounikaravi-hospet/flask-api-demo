# import flask

# app = flask.Flask(__name__)


# @app.route("/")
# def index():
#     return flask.render_template("index.html")


# app.run(debug=True)

import requests
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

BASE_URL = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'




def get_article_data(query):

    query_params = {
        "api-key" : os.getenv("NYT_KEY"),
        "q" : query
    }

    response = requests.get(BASE_URL, query_params)
    articles = response.json()["response"]["docs"]

    def get_article_headline(article):
        return article["headline"]["main"]


    def get_article_snippet(article):
        return article["snippet"]

    headlines = map(get_article_headline, articles)
    snippet = map(get_article_snippet, articles)

    return {
        "headlines": list(headlines),
        "snippet": list(snippet)
    }





# print(list(headlines))
# for article in articles:
#     print(article["headline"]["main"])


