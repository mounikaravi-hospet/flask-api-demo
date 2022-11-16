import flask 
import os
from nytapi import get_article_data

app = flask.Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

@app.route("/")
def main():
    query_word = "Georgia"
    article_data = get_article_data(query_word)

    # print(list(article_data))

    return flask.render_template(
        "index.html",
        topic = query_word,
        headlines = article_data["headlines"],
        snippet = article_data["snippet"]
    )

app.run(
    host=os.getenv("IP", "0.0.0.0"),
    port=int(os.getenv("PORT", 8080)),
    debug = True
)

