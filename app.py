import flask 
import os
from nytapi import get_article_data

app = flask.Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

@app.route("/", methods = ["GET", "POST"])
def main():
    query = flask.request.form.get("query")
    # query_word = "Trees"
    headlines, snippet, length = get_article_data(query)

    

    # print(list(article_data))

    return flask.render_template(
        "index.html",
        num_articles = length,
        topic = query,
        headlines = headlines,
        snippet = snippet
    )

app.run(
    host=os.getenv("IP", "0.0.0.0"),
    port=int(os.getenv("PORT", 8080)),
    debug = True
)

